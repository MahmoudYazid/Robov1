import sqlite3
from model.config import *
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_dir = (BASE_DIR + '//rdb.db')
GeneralConnection = sqlite3.connect(db_dir)



#  'ADB'  active database
# 'BDB' blocks database
#  'EDB'   EFFECTORs DB
# 'ODB' organs database
# 'QDB'   Questions DataBase



