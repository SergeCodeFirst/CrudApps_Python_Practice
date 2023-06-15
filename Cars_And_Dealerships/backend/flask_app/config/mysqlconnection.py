# a cursor is the object we use to interact with the database
import pymysql.cursors

# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'routeroute', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
                                    # establish the connection to the database
        self.connection = connection
        # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)

                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                elif query.lower().find("call") >= 0: # Change 'call' to 'exec' if you are using SQL Server
                    # CAll queries will run a store procedure. 
                    # It will return:
                    # 1 - The ID NUMBER of the row inserted or Updated (Select or Update)
                    # 2 - The data from the database as a LIST OF DICTIONARIES
                    # 3 - or nothing in case of a delete
                    result = {
                        'resultCT':self.connection.commit(), # this will return none if it's does not exist
                        'resultID': cursor.lastrowid, # this will return none if it's does not exist
                        'resultTB': cursor.fetchall() # this will return none if it's does not exist
                    }
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            # Commenting this out helps with error messages
            # except Exception as e:
            #     print("Something went wrong", e)
            #     return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)

