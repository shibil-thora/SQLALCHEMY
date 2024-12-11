from db import students, conn  

def run(): 
    update_query = students.update().where(students.c.name == 'sathar').values(lastname='nejjapp')
    conn.execute(update_query)  
    conn.commit()


if __name__ == '__main__': 
    run()
