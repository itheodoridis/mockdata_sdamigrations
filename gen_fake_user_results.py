# Setting up to generate the fake employee results
num_employee_records = 60

# Defining new fictional departments
fictional_departments = [
    "Department of Futuristic Studies",
    "Institute of Virtual Realities",
    "Bureau of Strategic Innovations",
    "Office of Cybernetic Advancement"
]

# Regenerating the employee results with fictional departments
fictional_employee_results = []

for _ in range(num_employee_records):
    hostname = f"wks-{fake.random_number(digits=4)}-{fake.random_number(digits=2)}.example.com"
    username = fake.user_name()
    full_name = fake.name().upper()
    email = f"{username}@example.com".lower()
    phone_number = f"210 {fake.random_number(digits=6)}"
    department = random.choice(fictional_departments)
    
    record = f"{hostname} {username} {full_name} {email} {phone_number} {department}"
    fictional_employee_results.append(record)

# Joining fictional employee records with newline to prepare for file writing
fictional_employee_output = "\n".join(fictional_employee_results)

# Save the fictional employee data to a text file
fictional_employee_data_path = '/mnt/data/Fictional_Employee_Results.txt'
with open(fictional_employee_data_path, 'w', encoding='utf-8') as file:
    file.write(fictional_employee_output)

fictional_employee_data_path
