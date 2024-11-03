from db import students, conn, addresses   
from sqlalchemy import select

def run(): 
    j = students.join(addresses) 
    query = select(addresses.c.email_add, addresses.c.postal_add).select_from(j).where(students.c.name == 'Ravi')
    rows = conn.execute(query)  
    for row in rows: 
        print(row) 

if __name__ == '__main__': 
    run()
