from EXPRESSION.db import students, conn, addresses   
from sqlalchemy import select, and_, or_, asc, desc, between

def run(): 
    query = students.select().where(and_(students.c.name == 'Ravi', students.c.lastname == 'Sattar')) 
    query = select(students.c.name, students.c.lastname).where(or_(students.c.name == 'Ravi', students.c.lastname == 'Sattar')) 
    query = select(students.c.id).order_by(desc(students.c.id))  
    query = select(students.c.id).where(between(students.c.id, 1, 3))
    result = conn.execute(query) 
    for row in result: 
        print(row)

    print(result)

if __name__ == '__main__': 
    run()
