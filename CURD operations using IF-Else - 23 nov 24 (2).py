## Console based project

import mysql.connector
import sys
# # connection established between py and sql db.
try :
    connection = mysql.connector.connect( user = 'root',
                                        password = 'root',
                                        host = 'localhost',
                                        database = 'dbproject'
                                        )
    if connection.is_connected:
        print('Connected created successfully.')

except Exception as e:
    print (e)

# # CREATE Table  query
try:
    create_table_query = '''
    create table IF NOT EXISTS employee (Id INT PRIMARY KEY,
    Name VARCHAR (50),
    Email VARCHAR (50) ,
    Designation VARCHAR (50),
    Salary INT not null
    )'''
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()       
    print('Table created successfully')
except Exception as e:
    print(e)

while(True):
    print("1.Insert values\n2.Show table\n3.Update Table\n4.Delete Record")
    choice = int(input('Enter your choice:'))

    if (choice==1):
    # INSERT  query
        try:
            insert_query = ''' insert into employee values (1,'Kajal','kajal@gmail.com','manager',36000),
                            (2,'Shakti','s@gmail.com','ceo', 50000),
                            (3, 'Sagar','Sagar@gmail.com', 'superviser',20000)
                            '''
            cursor = connection.cursor()
            cursor.execute(insert_query)
            connection.commit()       
            print('Values inserted successfully')

        except Exception as e:
            print(e)
    elif (choice==2):
        ## VIEW table -- SHOW query
        try :
            show_query=' select * from employee'
            cursor = connection.cursor()
            cursor.execute(show_query)
            rows = cursor.fetchall()
            
            print(f'Records in the table:')
            for row in rows:          # shows one row at a time.
                print(row)
        except Exception as e:
            print(e)

    elif(choice==3):
        # ## UPDATE query
        try:
            update_query = "update employee set salary = 22000 WHERE name = 'Sagar'"
            cursor = connection.cursor()
            cursor.execute(update_query)
            connection.commit()
            print(' Record Updated successfully.')
        except Exception as e:
            print(e)

    elif(choice==4):
        # DELETE query
        try :
            delete_query = "delete from employee WHERE name = 'Sagar'"
            cursor = connection.cursor()
            cursor.execute(delete_query)
            connection.commit()
            print('record deleted successfully')
        except Exception as e:
            print(e)

    elif(choice==5):
        print("Project terminated")
        sys.exit(0)
    
    else:
        print("INVALID INPUT")

# # DROP / Delete Table.
        # try:
        #     delete_table = "drop table employee"
        #     cursor = connection.cursor()
        #     cursor.execute(delete_table)
        #     connection.commit()
        #     print('Table deleted successfully')
        # except Exception as e:
        #     print(e)