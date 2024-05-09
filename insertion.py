import cx_Oracle
from flask import request 
cx_Oracle.init_oracle_client(lib_dir=r"E:\instantclient-basic-windows.x64-21.13.0.0.0dbru\instantclient_21_13")

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
completes_data = [
  (1, "2024-04-26", 600, 600, 1002),
  (2, "2024-04-27", 1200, 1199, 1003),
  (3, "2024-04-28", 1800, 1800, 1004),
  (4, "2024-04-29", 2400, 2400, 1005),
  (5, "2024-04-30", 3000, 3000, 1006),
  (6, "2024-05-01", 3600, 3600, 1007),
  (7, "2024-05-02", 4200, 4200, 1008),
  (8, "2024-05-03", 4800, 4800, 1009),
  (9, "2024-05-04", 5400, 5400, 1010),
  (10, "2024-05-05", 6000, 6000, 1011)
]
transaction_data =[
  (1, "2024-04-26", 600, 600),
  (2, "2024-04-27", 1200, 1199),
  (3, "2024-04-28", 1800, 1800),
  (4, "2024-04-29", 2400, 2400),
  (5, "2024-04-30", 3000, 3000),
  (6, "2024-05-01", 3600, 3600),
  (7, "2024-05-02", 4200, 4200),
  (8, "2024-05-03", 4800, 4800),
  (9, "2024-05-04", 5400, 5400),
  (10, "2024-05-05", 6000, 6000)
]
request_rollback_data = [
  (1, "ALEX SMITH", "alexsmith@email@example.com", 1002),
  (2, "William Johnson", "williamjohn@example.com", 1003),
  (3, "Emma Davis", "emmadavis@example.com", 1004),
  (4, "Oliver Brown", "olivierbrown@example.com,", 1005)
]


# Connection details (replace with your actual credentials)
username = "PG"
password = "people"
dsn = "localhost:1521/XE"

connection = cx_Oracle.connect(username, password, dsn)
cursor = connection.cursor()



# Insert data using executemany (more efficient for multiple inserts)
insert_query_Customer = """
INSERT INTO CUSTOMER (C_ID, C_NAME, C_EMAIL, C_PHONENUMBER, C_DOB, C_AGE)
VALUES (:1, :2, :3, :4, TO_DATE(:5, 'YYYY-MM-DD'), :6)
"""
# cursor.executemany(insert_query_Customer, customer_data)

#insert for completes
insert_query_Completes = """
INSERT INTO COMPLETES(T_ID, T_DATE, FEES, AMOUNT, C_ID)
VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD'), :3, :4, :5)
"""
cursor.executemany(insert_query_Completes, completes_data)




# Commit changes
connection.commit()

# Close connection
cursor.close()
connection.close()

print("Data inserted successfully!")
