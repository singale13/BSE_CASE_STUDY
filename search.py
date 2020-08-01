import psycopg2

option= input("Select Number which you want to perform: 1. Want to search the record, 2. Don't want to search the reord: ")
if option == "1":
	sc_name= input("Provide Script Name:")
	conn = psycopg2.connect(database = "mydb", user = "myuser", password = "mypass", host = "127.0.0.1", port = "5432")
	print("Opened database successfully")

	cursor = conn.cursor()
	cursor.execute("SELECT * FROM bse_share_table WHERE name=%s", (sc_name,))
	data = cursor.fetchall()
	print("Displaying Record:",data)
else:
	print("Thank you")
	
