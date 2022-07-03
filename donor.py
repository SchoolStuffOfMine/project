import mysql.connector
def RegisterDonor():
    cn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = "CHANGEME")
    cur = cn.cursor()
    dob = input('Enter DOB (i.e. YYYY-MM-DD): ')
    fname = input("First Name:")
    lname = input("Last Name:")
    blood = input("Blood Group: \n Choose from 'O+','O-','A+','A-','B+','B-','AB+','AB-':")
    while True:
        if blood not in ['O+','O-','A+','A-','B+','B-','AB+','AB-']:
            print("Invalid blood!")
            blood = input("Blood Group: \n Choose from 'O+','O-','A+','A-','B+','B-','AB+','AB-':")
        else:
            break     
    note = input("Any note:")
    query = "INSERT INTO DONORS (DOB,FName,LName,BloodType,Note) VALUES (%s, %s, %s, %s, %s)"
    values = (dob,fname,lname,blood,note)
    cur.execute(query,values)
    cur.execute("SELECT * FROM donors WHERE donors.dob > DATE_SUB(CURDATE(), INTERVAL 18 YEAR);")
    data = cur.fetchall()
    if data != []:
        print("The donor was less than 18 years so could not be registered!")
        cur.execute("DELETE FROM donors WHERE donors.dob > DATE_SUB(CURDATE(), INTERVAL 18 YEAR);")
    else:
        cur.execute("SELECT last_insert_id();")
        did = cur.fetchall()
        print(f"Successfully Registered! \nYour donor ID is {did[0][0]}")
    cn.commit()
    cn.close()
def ViewDonor():
    cn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = "CHANGEME")
    cur = cn.cursor()
    did = input("Enter Donor ID:")
    query = "SELECT * FROM DONORS WHERE DID= %s"
    value = did,
    cur.execute(query,value)
    data = cur.fetchall()
    if data == []:
        print("No record with matching Donor ID found!")
    else:
        print(f"""
            Donor ID: {data[0][0]}
            DOB: {data[0][1]} 
            First Name: {data[0][2]} 
            Last Name: {data[0][3]} 
            Blood Group: {data[0][4]} 
            Total times you have donated blood: {data[0][5]}
            Last donated blood on: {data[0][6]}
            Note: {data[0][7]}
        """)
    cn.commit()
    cn.close()
def KillDonor():
    cn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = "CHANGEME")
    cur = cn.cursor()
    did = input("Enter Donor ID:")
    query = "DELETE FROM DONORS WHERE DID = %s"
    cur.execute(query,(did,))
    cn.commit()
    cn.close()
    print(f"Record of user with Donor ID - {did} successfully deleted")
