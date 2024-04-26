import cx_Oracle 
cx_Oracle.init_oracle_client(lib_dir=r"E:\instantclient-basic-windows.x64-21.13.0.0.0dbru\instantclient_21_13")

# Connection details (replace with your actual credentials)
username = "PG"
password = "people"
dsn = "localhost:1521/XE"

connection = cx_Oracle.connect(username, password, dsn)
cursor = connection.cursor()

# Sample data as a list of tuples
customer_data = [
    (1002, "Jane Smith", "jane.smith@example.com", 2345678901, "1975-05-15", 49),
    (1003, "Michael Johnson", "michael.johnson@example.com", 3456789012, "1990-11-30", 33),
    (1004, "Emily Davis", "emily.davis@example.com", 4567890123, "1988-07-20", 35),
    (1005, "Daniel Brown", "daniel.brown@example.com", 5678901234, "1983-03-10", 41),
    (1006, "Sarah Wilson", "sarah.wilson@example.com", 6789012345, "1972-09-05", 52),
    (1007, "Matthew Taylor", "matthew.taylor@example.com", 7890123456, "1995-02-28", 29),
    (1008, "Olivia Martinez", "olivia.martinez@example.com", 8901234567, "1985-06-25", 39),
    (1009, "James Anderson", "james.anderson@example.com", 9012345678, "1977-12-12", 46),
    (1010, "Sophia Garcia", "sophia.garcia@example.com", 1234567890, "1982-08-18", 41),
    (1011, "David Rodriguez", "david.rodriguez@example.com", 2345678901, "1993-04-03", 31)
    
]

# Insert data using executemany (more efficient for multiple inserts)
insert_query = """
INSERT INTO CUSTOMER (C_ID, C_NAME, C_EMAIL, C_PHONENUMBER, C_DOB, C_AGE)
VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'), :6)
"""
cursor.executemany(insert_query, customer_data)

# Commit changes
connection.commit()

# Close connection
cursor.close()
connection.close()

print("Data inserted successfully!")
