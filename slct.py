from db import students, conn 

def run(): 
    s = students.select() 
    result = conn.execute(s) 
    print(result.fetchall())

if __name__ == '__main__': 
    run()