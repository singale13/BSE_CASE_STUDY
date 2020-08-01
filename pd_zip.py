import pandas as pd
import psycopg2

def db_operation():
	data = pd.read_csv(r'EQ310720.CSV')   

	new_df=data.drop(['SC_GROUP','SC_TYPE','LAST','PREVCLOSE','NO_TRADES','NO_OF_SHRS','NET_TURNOV','TDCLOINDI'], axis=1)
	df = pd.DataFrame(new_df)
	print("Dtaframe required",df)

	conn = psycopg2.connect(database = "mydb", user = "myuser", password = "mypass", host = "127.0.0.1", port = "5432")
	print("Opened database successfully")
	print("-------------------------------------------------------")
	print("Creating the table in database")
	if conn:
		cursor = conn.cursor()
		queery="""CREATE TABLE bse_share_table(
    		code integer,
    		name CHAR(20),
    		open float(6),
		high float(6),
		low float(6),
		close float(6)
		);"""
		cursor.execute(queery)	
		conn.commit()
		print("Inserting required columns from csv into the database")
		# creating column list for insertion
		cols = ",".join([str(i) for i in df.columns.tolist()])

		# Insert DataFrame recrds one by one.
		for i,row in df.iterrows():
			sql = "INSERT INTO bse_share_table(code,name,open,high,low,close) VALUES (" + "%s,"*(len(row)-1) + "%s)"
			cursor.execute(sql, tuple(row))
			conn.commit()
    
		queery="""SELECT * FROM bse_share_table ORDER BY close DESC LIMIT 10;"""
		cursor.execute(queery)	
		conn.commit()
		myresult = cursor.fetchall()
		print("-------------------------------------------------------")

		print("Displaying Top 10 values based on Close value:",myresult)
	else:
		print("Not able to connect to the Databse, Please try again")

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    db_operation()
