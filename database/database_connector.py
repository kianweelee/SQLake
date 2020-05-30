#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:23:22 2020

@author: kianweelee
"""

def connector(data, username, password, database_name, table_name, mysql_choice, postgresql_choice, sqlite_choice, result_lst):
    
    # If user uses PostgreSQL
    if postgresql_choice:
        try:
            import psycopg2
            connection = psycopg2.connect(user = username, #Default username: postgres
                                          password = password,
                                          host = "127.0.0.1",
                                          port = "5432",
                                          database = database_name)
            # Creating a cursor object
            cursor = connection.cursor()
    
            # Dropping table if already exist
            cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
            
             # Creating the table
            front_statement = "Create table {} (".format(table_name)
            mid_statement = ""
            value_lst = []
            tup_lst = []
            str1 = ""
            str2 = ""
            rows = data.shape[0]
            cols = data.columns
            for i in range(0, len(result_lst)-1):
                mid_statement += result_lst[i][0] +" "+ result_lst[i][1] + ","
            end_statement = result_lst[-1][0] + " " + result_lst[-1][-1] + ")"
            for index in range(0, rows):
                value_lst.append(data.iloc[index].tolist())
            for lst in value_lst:
                tup_lst.append(tuple(lst))
            for index2 in range(0, len(cols)-1):
                str1 += cols[index2] + ","
            str2 = str1 + cols[-1]
            values = str(tup_lst).strip('[]')
            insert_statement = "Insert into {} ({}) Values {}".format(table_name, str2, values)
            full_statement = front_statement + mid_statement + end_statement
            cursor.execute(full_statement)
            cursor.execute(insert_statement)
            connection.commit()        


        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
                
    # If user uses MySQL
    elif mysql_choice:
        import mysql.connector
        # Establish connection
        connection = mysql.connector.connect(user = username, # Default: root
                                             password = password,
                                             host = '127.0.0.1',
                                             database = database_name)
        
        # Creating a cursor object
        cursor = connection.cursor()
        # Dropping table if already exists.
        cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))        
        
        # Creating the table
        front_statement = "Create table {} (".format(table_name)
        mid_statement = ""
        value_lst = []
        tup_lst = []
        str1 = ""
        str2 = ""
        rows = data.shape[0]
        cols = data.columns
        for i in range(0, len(result_lst)-1):
            mid_statement += result_lst[i][0] +" "+ result_lst[i][1] + ","
        end_statement = result_lst[-1][0] + " " + result_lst[-1][-1] + ")"
        for index in range(0, rows):
            value_lst.append(data.iloc[index].tolist())
        for lst in value_lst:
            tup_lst.append(tuple(lst))
        for index2 in range(0, len(cols)-1):
            str1 += cols[index2] + ","
        str2 = str1 + cols[-1]
        values = str(tup_lst).strip('[]')
        insert_statement = "Insert into {} ({}) Values {}".format(table_name, str2, values)
        full_statement = front_statement + mid_statement + end_statement
        cursor.execute(full_statement)
        cursor.execute(insert_statement)
        connection.commit()        

        # Closing connection
        connection.close()
        
    # If user uses SQLite
    else:
        try:
            import sqlite3
            connection = sqlite3.connect("{}.db".format(database_name))
           
            # Creating a cursor object
            cursor = connection.cursor()
        
    # Creating the table
            front_statement = "Create table {} (".format(table_name)
            mid_statement = ""
            value_lst = []
            tup_lst = []
            str1 = ""
            str2 = ""
            rows = data.shape[0]
            cols = data.columns
            for i in range(0, len(result_lst)-1):
                mid_statement += result_lst[i][0] +" "+ result_lst[i][1] + ","
            end_statement = result_lst[-1][0] + " " + result_lst[-1][-1] + ")"
            for index in range(0, rows):
                value_lst.append(data.iloc[index].tolist())
            for lst in value_lst:
                tup_lst.append(tuple(lst))
            for index2 in range(0, len(cols)-1):
                str1 += cols[index2] + ","
            str2 = str1 + cols[-1]
            values = str(tup_lst).strip('[]')
            insert_statement = "Insert into {} ({}) Values {}".format(table_name, str2, values)
            full_statement = front_statement + mid_statement + end_statement
            cursor.execute(full_statement)
            cursor.execute(insert_statement)
            connection.commit()
        
            # Closing connection
            connection.close()
    
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
        finally:
            if (connection):
                connection.close()
                print("The SQLite connection is closed")
