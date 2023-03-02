
import pymongo

from model.config import *
SingletonConn = pymongo.MongoClient(connection['connectionstring'])
InstanseDb = SingletonConn['RoboDb']
InstanseADB = InstanseDb['ADB']  #active database
InstanseBDB = InstanseDb['BDB']  # blocks database
InstanseEDB = InstanseDb['EDB']  # EFFECTORs DB
InstanseODB = InstanseDb['ODB']  # organs database
InstanseQDB = InstanseDb['QDB']  # Questions DataBase



