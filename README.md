# SQLake
A python script that exports CSV or Excel file directly into a relational database management system.

## Table of contents
- **Getting Started**
  - [ Dependencies ](#dependencies)
  - [ Installation ](#installation)
  - [ Preview ](#preview)
- [Concept behind SQLake](#concept)
- [Target audience](#audience)
- [About me](#aboutme)
- [Contributing](#contributing)
- [License](#license)


## Getting Started
<a name="dependencies"></a>
### 1. Dependencies
```py
pandas==1.0.0
psycopg2==2.8.4
mysql_connector_repackaged==0.3.1
PySimpleGUI==4.19.0
```
<a name="installation"></a>
### 2. Installation
Prior to this installation, we assume that you have MySQL or PostgreSQL or SQLite3 installed on your local system. If you have not done so, please proceed to the following links to get them installed:
- [MySQL](https://www.sitepoint.com/how-to-install-mysql/)
- [PostgreSQL](https://www.2ndquadrant.com/en/blog/pginstaller-install-postgresql/)
- [SQLite3](https://www.servermania.com/kb/articles/install-sqlite/)

If you experience any issues, do feel free to [contact me](#aboutme).

After which, do the following:

1. You can clone or download my package.
2. Using terminal, move to the directory. 
   - Example for Mac OS users: 
   ```bash
   $ cd Downloads/SQLake
   ```
3. Install the required packages using:
   ```py
   pip install -r requirements.txt
   ```
4. Now, execute the main.py file by:
   ```py
   $ python main.py
   ```
5. You will see a GUI popping up.
  - Pick a file format (CSV or Excel)
  - Click on the browse button to choose the file
  - Choose your database type
  - Key in your database name. This database has to be created prior to the running of this script.
  - Key in the name of the table. My script will create this table for you.
  - Key in the Username and password. 
    - Default for MySQL is root and postgres for PostgreSQL. 
    - SQLite3 has no username and password requirement so leave those 2 fields blank.
  
<a name="preview"></a>
### 3. Preview
<img src="https://media.giphy.com/media/S8MxlxBk86XKktx0zQ/giphy.gif" alt="Animated GIF" style="width: 480px; height: 360px; left: 0px; top: 0px; opacity: 1;">

<a name="concept"></a>
## Concept behind SQLake
For start, SQLake utilises Pandas to identify data type of each column in the provided dataset. With the information of the data type, I was able to match the data type to the data type reflected on MySQL, PostgreSQL or SQLite3. I then use the for loops to loop through each row of the dataset and append them into a bunch of lists. At the end, I concatenate all the required list into one variable and execute this variable into the SQL connection.

<a name="audience"></a>
## Target Audience
I am aware that analysts are required to clean up data files and export those files into an SQL database. Imagine spending hours sitting in front of the computer doing that for the next 5 to 10 years of your career. Won't that scare you? Indeed, there are tons of websites out there that can take in your files and generate an SQL query for you but do you trust them with your client's details? How confident are you that they won't exploit those data for personal use? 

That is why my script can save you the trouble of going through all those risks! My script can be run on your local machine offline and every process is transparent to the end user. Feel free to drop in an issue if you encounter any and I will look into it! You can't get a better support that this! I have also added in a graphic user interface to cater to users with non-technical backgrounds. All they have to do is choose the file path, key in the names of the database, table, their usernames and password and bam! your work is done!

<a name="aboutme"></a>
## About me
I graduated from the University of New South Wales in 2018 with a Bachelor of Biotechnology (1st Class Hons). My honours project exposed me to the field of bioinformatics and I have fallen in love with it ever since. I realised that we can generate tons of insights just from data alone and this inspired me to venture into this field. I started the process of being a self-taught programmer in 2019 and I am glad I have made the right choice!

Feel free to reach out to me!
- [Linkedin](https://www.linkedin.com/in/kianweelee/)
- [Blog](https://coderkian.com/)
- [Github](https://github.com/kianweelee)
- [Twitter](https://twitter.com/CoderKianWee)

<a name="Contributing"></a>
## Contributing
I am open to any form of contribution but do take a look at the [Contribution.md](https://github.com/kianweelee/SQLake/blob/master/Contribution.md) document before contributing.

<a name="license"></a>
## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/kianweelee/SQLake/blob/master/LICENSE) file for details
