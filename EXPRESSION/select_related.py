from EXPRESSION.db import students, conn , addresses
from sqlalchemy import select

def run(): 
    select_query = select(students, addresses.c.postal_add, addresses.c.email_add)
    select_query = select_query.where(students.c.id == addresses.c.st_id) 

    result = conn.execute(select_query) 
    result_list = result.fetchall()
    for row in result_list: 
        print(row)

if __name__ == '__main__': 
    run()