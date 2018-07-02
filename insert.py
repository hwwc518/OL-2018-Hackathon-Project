from appdef import app, conn
from datetime import datetime, timedelta

ursor_two = conn.cursor()
"""
query = "CREATE TABLE Employee ( \
 EMPLID INT NOT NULL AUTO_INCREMENT, \
 title VARCHAR(100), \
 employee_name VARCHAR(255), \
 department VARCHAR(255), \
 groupname VARCHAR(255), \
 PRIMARY KEY(EMPLID) \
);"
ursor_two.execute(query)
conn.commit()
ursor_two.close()



ursor_two = conn.cursor()
query = "CREATE TABLE Ticket ( \
 ticket_id INT NOT NULL AUTO_INCREMENT, \
 idea TEXT, \
 why TEXT, \
 urgency INT, \
 resolution VARCHAR(255), \
 person_in_charge INT DEFAULT 0, \
 date_created DATETIME, \
 PRIMARY KEY (ticket_id), \
 FOREIGN KEY (person_in_charge) REFERENCES Employee(EMPLID) \
);"
ursor_two.execute(query)
conn.commit()
ursor_two.close()
"""

ursor_two = conn.cursor()
query = "INSERT INTO Employee (EMPLID, title, employee_name, department, groupname) VALUES ('12346', 'SPECIALIST', 'PEANUT BUTTER', 'FSQA', '1'), ('12347', 'SPECIALIST', 'SOUP DUMPLING', 'FSQA', '1'), ('12348', 'SPECIALIST', 'FRENCH FRIES', 'FSQA', '1'), ('12349', 'MANAGER', 'Spring Onion', 'FSQA', '1'), ('23456', 'RUNNER', 'BLUE CHEESE', 'KITCHEN', '2'), ('23457', 'RUNNER', 'BEEF JERKY', 'KITCHEN', '2'), ('23458', 'RUNNER', 'BITTER GOURD', 'KITCHEN', '2'), ('23459', 'RUNNER', 'BITTER MELON', 'KITCHEN', '2'), ('23450', 'MANAGER', 'BOK CHOY', 'KITCHEN', '2'), ('34567', 'CUSTODIAN', 'BUBBLE TEA', 'PACKING', '3'), ('34568', 'CUSTODIAN', 'POPCORN CHICKEN', 'PACKING', '3'), ('34569', 'CUSTODIAN', 'MANGO SLUSH', 'PACKING', '3'), ('34560', 'CUSTODIAN', 'APPLE PIE', 'PACKING', '3'), ('34561', 'MANAGER', 'CREAM CHEESE', 'PACKING', '3'), ('45678', 'QA ASSOCIATE', 'BANANA SPLIT', 'SANITATION', '4'), ('45679', 'QA ASSOCIATE', 'FRIED COKE', 'SANITATION', '4'), ('45670', 'QA ASSOCIATE', 'ROAST PORK', 'SANITATION', '4'), ('45671', 'QA ASSOCIATE', 'PASTA PRIMAVERA', 'SANITATION', '4'), ('45672', 'MANAGER', 'RIDGE GOURD', 'SANITATION', '4'), ('56789', 'TECH', 'APPLE CRISP', 'SHIPPING', '5'), ('56780', 'TECH', 'SPICY SHRIMP', 'SHIPPING', '5'), ('56781', 'TECH', 'BEEF BURGER', 'SHIPPING', '5'), ('56782', 'TECH', 'MISO-HONEY SALMON', 'SHIPPING', '5'), ('56783', 'MANAGER', 'TAHINI CHICKEN', 'SHIPPING', '5');"
ursor_two.execute(query)
conn.commit()
ursor_two.close()