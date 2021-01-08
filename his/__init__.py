from flask import Flask
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] =  '5791628bb0b13ce0c676dfde280ba245'

# init the database
conn = sqlite3.connect('database.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP DATABASE IF EXISTS HISDB;
CREATE DATABASE HISDB;
''')

script = '''
DROP TABLE IF EXISTS scans;
DROP TABLE IF EXISTS Accounts;
DROP TABLE IF EXISTS special_forms;
DROP TABLE IF EXISTS examinations;
DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS doctors;

CREATE TABLE special_forms(
    script TEXT,
    formID INT NOT NULL
);

CREATE TABLE doctors(
    doctorID INT NOT NULL UNIQUE
);

CREATE TABLE scans(
    scanID INT NOT NULL,
    state TEXT,
    date TEXT
);

CREATE TABLE patients(
    patientID INT NOT NULL UNIQUE,
    FscanID INT NOT NULL UNIQUE
);

CREATE TABLE examinations(
    FdoctorID INT NOT NULL,
    FpatientID INT NOT NULL
);

CREATE TABLE Accounts(
    name VARCHAR(50),
    phone VARCHAR(11),
    username VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(30) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    FformID INT UNIQUE,
    FdoctorID INT UNIQUE,
    FpatientID INT UNIQUE
);
'''

cur.executescript(script)

from his import routes
