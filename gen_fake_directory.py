from faker import Faker
import csv
import random
from io import StringIO

# Create a Faker instance
fake = Faker()

# Define the number of entries
num_entries = 50

# Generate data
data = []
for _ in range(num_entries):
    employee_id = fake.random_number(digits=4, fix_len=True)
    surname = fake.last_name()
    firstname = fake.first_name()
    section_id = fake.random_number(digits=3, fix_len=True)
    role = fake.job()
    department_id = section_id  # Simplified assumption
    employee_rank = random.choice(['Manager', 'Assistant Manager', 'Employee', 'Senior Employee'])
    phone1 = fake.phone_number()
    phone2 = fake.phone_number() if random.random() > 0.5 else ''
    email_address = f"{firstname[0]}{surname}@example.com".lower()
    number = '0'
    section_id_2 = section_id
    section_description = 'Department of ' + fake.word()
    department_id_2 = '1'
    department_description = 'Administration'
    
    data.append([
        employee_id, surname, firstname, section_id, role, department_id, employee_rank,
        phone1, phone2, email_address, number, section_id_2, section_description,
        department_id_2, department_description
    ])

# Save to a CSV file
output = StringIO()
csv_writer = csv.writer(output, delimiter=';')
header = ["employee_id", "surname", "firstname", "section_id", "role", "department_id", "employee_rank",
          "phone1", "phone2", "email_address", "number", "section_id_2", "section_description",
          "department_id_2", "department_description"]
csv_writer.writerow(header)

# Save the CSV data to a text file
file_path = '/mnt/data/Fake_Employee_Data.csv'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(output.getvalue())

file_path

csv_writer.writerows(data)

output.getvalue()[:1000]  # Show a sample of the data to verify before saving as a file
