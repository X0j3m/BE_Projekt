import mariadb
import sys
from itemadapter import ItemAdapter
class SaveToMariadb:
    def __init__(self):      
        conn = None
        cursor = None
        try:
            #Connecting to MariaDb
            print("Connecting to MariaDb -> Pancernik")
            conn = mariadb.connect(
                user = 'root',
                password = '12345',
                host = '127.0.0.1',
                port = 3306,
                database = 'pancernik'
            )
            print("Connection successful!")


            #Creating cursor object
            cursor = conn.cursor()
            
            #Trying to create a table "Product"
            try:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS products(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name varchar(255) NOT NULL
                    )
                """)
                conn.commit() #Commit the transaction
                print("Table product created!")
            except mariadb.Error as e:
                print(f"Error creatint table: {e}")
                conn.rollback()
        except mariadb.Error as e:
            print(f"An error occurred: {e}")
            sys.exit(1)
        finally:
            #Close Cursor and Connection
            if cursor:
                cursor.close()
                print("Cursor closed.")
            if conn:
                conn.close()
                print("Connection closed.")


    def process_item(self, item, spider):
        adapter = ItemAdapter(item)



