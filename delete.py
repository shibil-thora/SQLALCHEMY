from db import students, conn  
from sqlalchemy import update

def run(): 
    update_query = students.update().values(name='kunjippa') 
    conn.execute(update_query)  
    conn.commit()


if __name__ == '__main__': 
    run()
