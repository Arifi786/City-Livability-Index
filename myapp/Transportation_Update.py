import mysql.connector

# Connect to your MySQL database
conn = mysql.connector.connect(
    host="localHost",
    user="root",
    password="#Arifi786",
    database="Mohammad Arif"
)

# Create a cursor object
cursor = conn.cursor()

# Fetch the salary data from the City table
cursor.execute("SELECT Salary FROM myapp_city")
salaries = cursor.fetchall()

# Define the SQL UPDATE query template
update_query = """
    UPDATE myapp_city
    SET Transportation = 
        CASE
            WHEN Salary > 70000 THEN FLOOR(RAND() * (10-8+1) + 8)
            WHEN Salary BETWEEN 30000 AND 70000 THEN FLOOR(RAND() * (7-5+1) + 5)
            WHEN Salary BETWEEN 10000 AND 30000 THEN FLOOR(RAND() * (4-1+1) + 1)
        END
    WHERE Salary = %s
"""

# Update each row individually
for salary in salaries:
    cursor.execute(update_query, (salary[0],))

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
