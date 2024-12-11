from db import students, conn, addresses 
from sqlalchemy import select

def run(): 
    s = students.select().where(students.c.id > 11) # way 1
    s = select(students.c.name, students.c.lastname).where(students.c.id > 11) # way 2
    s = addresses.select().where(addresses.c.postal_add.ilike('___rch%')) # way 3
    result = conn.execute(s) 
    print(result.fetchall())

if __name__ == '__main__': 
    run()