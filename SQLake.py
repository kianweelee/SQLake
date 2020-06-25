def main():
	# Importing required packages 
	import PySimpleGUI as sg
	from database import database_connector as dc
	import pandas as pd
	import numpy as np

	# Setting theme for GUI
	sg.theme('TanBlue')

	# Create a GUi with input request
	## A radio button for type of file data
	## Create a text input for file input path
	## A radio button for type of RDBMS
	## Create a text input for username and password

	layout = [ 
	    [sg.Frame(layout=[[sg.Radio('CSV', "file_format", default=True, size=(10,1)), sg.Radio('XLS', "file_format")]], title='File Format',title_color='blue', relief=sg.RELIEF_SUNKEN)],
	    [sg.Text('File path', size=(8, 1)), sg.Input(), sg.FileBrowse()],
	    [sg.Frame(layout=[
	    [sg.Radio('MySQL', "database_type"), sg.Radio('PostgreSQL', "database_type"), sg.Radio('SQLite', "database_type")]], title='Database Type',title_color='blue', relief=sg.RELIEF_SUNKEN)],
	    [sg.Text('Name of database:',size = (14,1)), sg.InputText()],
	    [sg.Text('Table name:',size = (10,1)), sg.InputText()],
	    [sg.Text('Username:',size = (8,1)), sg.InputText()],
	    [sg.Text('Password:', size=(8, 1)), sg.InputText('', key='Password', password_char='*')],
	    [sg.Submit(), sg.Cancel()]
			]

	window = sg.Window('SQLake', layout, default_element_size=(40, 1), grab_anywhere=False)
	event, values = window.read()
	window.close()
	csv_choice, xls_choice, file_path, mysql_choice, postgresql_choice,sqlite_choice,database_name, table_name,username, password = values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values["Password"]

	# Process csv file
	if csv_choice:
	    end_file = pd.read_csv(file_path)
	else:
	    end_file = pd.read_excel(file_path, index_col=None)

	# Convert NaN values to "NULL". SQL queries take in NaN/missing values as NULL
	end_file.fillna("NULL", inplace = True)

	# Identify data type for each variable. This will help us decide the data type when we create an SQL table.
	data_type = end_file.dtypes
	dtype_lst = []
	# Replace spaces in column names with "_"
	end_file.columns = end_file.columns.str.replace(' ', '_')

	cols = end_file.columns

	if mysql_choice or postgresql_choice:
	    for i in range(0, len(cols)):
	        if data_type[i] == "object":
	            dtype_lst.append("varchar(255)")
	        elif data_type[i] == "datetime64[ns]":
	            dtype_lst.append("Date")
	        elif data_type[i] == "int64":
	            dtype_lst.append("int")
	        elif data_type[i] == "float64":
	            dtype_lst.append("float")
	        elif data_type[i] == "datetime64":
	            dtype_lst.append("datetime")

	else:
	    for i in range(0, len(cols)):
	        if data_type[i] == "object":
	            dtype_lst.append("text")
	        elif data_type[i] == "datetime64[ns]":
	            dtype_lst.append("text")
	        elif data_type[i] == "int64":
	            dtype_lst.append("integer")
	        elif data_type[i] == "float64":
	            dtype_lst.append("real")
	        elif data_type[i] == "datetime64":
	            dtype_lst.append("text")
	        
	result = zip(cols, dtype_lst)
	result_lst = list(result)

	dc.connector(end_file ,username, password, database_name, table_name, mysql_choice, postgresql_choice, sqlite_choice, result_lst)

if __name__ == '__main__':
	main()