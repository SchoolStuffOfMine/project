import mysql.connector
def ViewDonation():
    cn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = "CHANGEME")
    cur = cn.cursor()
    did = input("Enter Transaction ID:")
    query = "SELECT TID, Donors.DID, DOA, Quantity, Donors.FName, Donors.Lname FROM Stock, Donors WHERE TID= %s"
    value = did,
    cur.execute(query,value)
    data = cur.fetchall()
    if data == []:
        print("No record with matching Transaction ID found!")
    else:
        print(f"""
            Tranaction ID: {data[0][0]}
            Donor ID: {data[0][1]}
            Donor Name: {data[0][4]} {data[0][5]}
            Date of Donation: {data[0][2]} 
            Quantity: {data[0][3]}ml 
        """)
    cn.commit()
    cn.close()
def RegisterDonation():
    cn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = "CHANGEME")
    cur = cn.cursor()
    did = input("Enter Donor ID of Donator:")
    doa = input("Enter date of donation [YYYY-MM-DD] For current date, enter c:")
    if doa == 'c':
        cur.execute("SELECT CURDATE();")
        doa = (cur.fetchall())[0][0]
    quantity = input("Enter quantity of blood donated (in ml):")
    cur.execute(f"SELECT BloodType FROM Donors WHERE DID = {did};")
    bt = (cur.fetchall())[0][0] #Returns Blood Type
    query = "INSERT INTO STOCK (DID, DOA, Quantity, BloodType) VALUES (%s, %s, %s, %s);"
    values = (did, doa, quantity, bt)
    cur.execute(query, values)
    cur.execute(f"UPDATE Donors SET TotalDonations = TotalDonations + 1 WHERE did = {did}")
    query = ('UPDATE Donors SET LastDonated = %s WHERE did = %s ')
    values = (str(doa), did)
    cur.execute(query, values)
    cn.commit()
    cur.execute("SELECT last_insert_id();")
    tid = cur.fetchall()
    print(f"Successfully Registered! \n The transaction ID is {tid[0][0]}")
    cn.close()
def DonationStats():
    cn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'root', database = "CHANGEME")
    cur = cn.cursor()
    bt = input("Which blood group's information do you need? Press a for all: ")
    if bt == 'a':
        btc = ''
    else:
        btc = f'HAVING BloodType = "{bt}"'
    cur.execute(f"SELECT sum(Quantity), avg(Quantity), min(Quantity), max(Quantity), min(DOA), max(DOA), BloodType\
        FROM Stock GROUP BY BloodType {btc};")
    data = cur.fetchall()
    for __ in data:
        print(f"""
        Blood Group: {__[6]}
        Total Qty. donated: {__[0]}ml
        Avg. Qty. donated: {__[1]}ml
        Min. Qty. donated: {__[2]}ml
        Max. Qty. donated: {__[3]}ml
        This blood type was first donated on {__[4]}
        This blood type was latest donated on {__[5]}    
        """)
    cn.close()