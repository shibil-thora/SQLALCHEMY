from sqlalchemy.sql import func  
from EXPRESSION.db import conn, students, addresses
from sqlalchemy import select

def run(): 
    query = select(students).where(students.c.id == select(func.max(students.c.id)).scalar_subquery()) 
    query = select(func.min(students.c.id))
    result = conn.execute(query) 
    print(list(result))

if __name__ == '__main__': 
    run() 