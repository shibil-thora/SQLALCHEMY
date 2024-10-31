from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String  
import os 
from dotenv import load_dotenv 

load_dotenv()

engine = create_engine(os.environ.get('SQL_CONNECT_URL')) 
meta = MetaData() 

students = Table(
    'students', meta, 
    Column('id', Integer, primary_key=True), 
    Column('name', String, index=True), 
    Column('lastname', String),
) 
# #meta.create_all(engine) 

conn = engine.connect()

