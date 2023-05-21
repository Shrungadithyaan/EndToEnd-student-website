import sqlite3
con = sqlite3.connect("SDM.db")
print("Database Opened Successfully")

con.execute("Create table Student(rollno integer primary key autoincrement, sname text not null, email text unique not null,mobile integer not null,dept text not null,year integer not null)")
print("table Created ")
