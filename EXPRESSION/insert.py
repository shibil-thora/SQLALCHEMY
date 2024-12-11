from EXPRESSION.db import students, conn, addresses

def run(): 
    st_ins = students.insert() 
    addr_ins = addresses.insert() 

    result = conn.execute(st_ins, [
        {'name':'Ravi', 'lastname':'Kapoor'},
        {'name':'Rajiv', 'lastname' : 'Khanna'},
        {'name':'Komal','lastname' : 'Bhandari'},
        {'name':'Abdul','lastname' : 'Sattar'},
        {'name':'Priya','lastname' : 'Rajhans'},
    ]) 

    conn.commit()
    
    result = conn.execute(addr_ins, [
        {'st_id':1, 'postal_add':'Shivajinagar Pune', 'email_add':'ravi@gmail.com'},
        {'st_id':1, 'postal_add':'ChurchGate Mumbai', 'email_add':'kapoor@gmail.com'},
        {'st_id':3, 'postal_add':'Jubilee Hills Hyderabad', 'email_add':'komal@gmail.com'},
        {'st_id':5, 'postal_add':'MG Road Bangaluru', 'email_add':'as@yahoo.com'},
        {'st_id':2, 'postal_add':'Cannought Place new Delhi', 'email_add':'admin@khanna.com'},
    ]) 

    print(result.rowcount)
    conn.commit()


if __name__ == '__main__': 
    run()
