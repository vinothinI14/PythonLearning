import pytest
from selenium import webdriver
import os

driver = None

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be execution at last")


@pytest.fixture()
def dataload():
    return ["Vino", "Thakshika", "Thashvanth", "Suviksha", "Samyuktha"]


@pytest.fixture(params=["Vino","Thakshika","Thashvanth","Suviksha","Samyuktha"])
def parameterization(request):
    return request.param

#Register options to use further in our code (Mandatory)
def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="Chrome", help="browser selection"
    )
@pytest.fixture(scope="function")
def launchbrowser(request): # Request to get browser options
    global driver
    browsername = request.config.getoption("browsername") #Getting config value at runtime using getoption
    if browsername == "Chrome":
        driver = webdriver.Chrome()

    if browsername == "FireFox":
        driver = webdriver.Firefox()

    if browsername == "Edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()


@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir,  "failScreen.png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)


