from db import students, conn  

def run(): 
    delete_query = students.delete().where(students.c.id == 4) 
    delete_all = students.delete()
    result = conn.execute(delete_all)  
    conn.commit() 
    print(result.rowcount, 'deleted')


if __name__ == '__main__': 
    run()
