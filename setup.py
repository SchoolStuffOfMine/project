def setup():
    '''A function to create the required tables and the database'''
    import mysql.connector
    cn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root')
    cur=cn.cursor()
    cur.execute("CREATE DATABASE CHANGEME")
    cur.execute("USE CHANGEME")
    cur.execute("CREATE TABLE DONORS (\
    DID INT NOT NULL AUTO_INCREMENT,\
    DOB DATE NOT NULL,\
    FName VARCHAR(200) NOT NULL,\
    LName VARCHAR(200),\
    BloodType CHAR(3) NOT NULL,\
    TotalDonations INTEGER DEFAULT 0,\
    LastDonated DATE NULL,\
    Note VARCHAR(255) NULL,\
    PRIMARY KEY (DID)\
    );")
    cur.execute("CREATE TABLE STOCK (\
    TID INTEGER NOT NULL AUTO_INCREMENT,\
    DID INTEGER,\
    DOA DATE ,\
    Quantity INTEGER NOT NULL,\
    BloodType CHAR(3) NOT NULL,\
    FOREIGN KEY (DID) REFERENCES DONORS(DID),\
    PRIMARY KEY (TID) \
    );")
    cn.commit()
    cn.close()
    print("Set-Up Successful!")

