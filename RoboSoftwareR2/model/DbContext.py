import pymongo as mongodb
from model.config import *
SingletonConn=mongodb.MongoClient(connection['connectionstring'])
InstanseDb = SingletonConn['RoboDb']
InstanseQdb = InstanseDb['QDB']
InstanseCDB = InstanseDb['CDB']
InstanseDIDB = InstanseDb['DIDB']
InstanseDRDB = InstanseDb['DRDB']
InstanseODB = InstanseDb['ODB']
InstanseSDB = InstanseDb['SDB']


