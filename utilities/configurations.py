import configparser
import mysql.connector

def getConfig():

    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def getPassword():
    password = 'CoolLearn@2025'
    return password

connect_config = {'user': getConfig()['SQL']['user'],
                  'password':getConfig()['SQL']['password'],
                  'host':getConfig()['SQL']['host'],
                  'database':getConfig()['SQL']['database']
}

def getConnection():
    con = mysql.connector.connect(**connect_config)
    print(con.is_connected())
    return con

def getQuery(query):
    con = getConnection();
    cursor = con.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    con.close()
    return row

def getQueryFetchAll(query):
    con = getConnection();
    cursor = con.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    con.close()
    return row
