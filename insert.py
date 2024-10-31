from db import students, conn 

def run(): 
    ins = students.insert()
    result = conn.execute(ins, [
        {'name': 'manoj', 'lastname': 'kumar'}, 
        {'name': 'sathar', 'lastname': 'kareem'}, 
        {'name': 'checku', 'lastname': 'latheef'}, 
        {'name': 'luttu', 'lastname': 'kujjapp'}, 
    ]) 
    conn.commit()
    print(result)


if __name__ == '__main__': 
    run()
