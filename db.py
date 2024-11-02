from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey  
import os 
from dotenv import load_dotenv 
import sys

load_dotenv()

engine = create_engine(os.environ.get('SQL_CONNECT_URL')) 
meta = MetaData() 

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True, autoincrement=True), 
   Column('name', String(255)), 
   Column('lastname', String(255)), 
)  

addresses = Table(
    'addresses', meta, 
    Column('id', Integer, primary_key = True, autoincrement=True), 
    Column('st_id', Integer, ForeignKey('students.id'), index=True), 
    Column('postal_add', String(255)), 
    Column('email_add', String(255)),
)

conn = engine.connect()

if __name__ == '__main__': 
    try:
        if sys.argv[1] == 'create': 
            meta.create_all(engine)   
            print('[done!]')
    except: 
        pass 