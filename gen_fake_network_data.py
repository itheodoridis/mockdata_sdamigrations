from faker import Faker

import random

# Create a Faker instance

fake = Faker()

# Setting up to generate the network device data

num_records = 200

vlan_range = range(2, 90)  # VLAN numbers from 2 to 89

# Re-generating the network data with updated switch name format
network_data_updated = []

for _ in range(num_records):
    mac_address = ':'.join(['{:02x}'.format(random.randint(0, 255)) for _ in range(6)])
    host_ip = fake.ipv4()
    
    # Randomly decide if the device is a printer or a workstation
    if random.random() > 0.8:  # 20% chance to be a printer
        host_name = f"prn-{fake.random_number(digits=4)}-{fake.random_number(digits=2)}.example.com"
    else:  # 80% chance to be a workstation
        host_name = f"wks-{fake.random_number(digits=4)}-{fake.random_number(digits=2)}.example.com"
    
    vlan = random.choice(vlan_range)
    port = f"Gi0/{random.randint(1, 48)}"
    switch_name = f"Sw-site1-{random.randint(10, 99)}"
    switch_address = fake.ipv4()
    switch_location = "site-1"
    
    record = f"mac-address: {mac_address},host_ip: {host_ip},host_name: {host_name},vlan: {vlan},port: {port},switch-name: {switch_name},switch-address: {switch_address},switch-location: {switch_location}"
    network_data_updated.append(record)

# Joining updated records with newline to prepare for file writing
network_output_updated = "\n".join(network_data_updated)

# Save the updated network device data to a text file
network_data_updated_path = '/mnt/data/Fake_Network_Data_Updated.txt'
with open(network_data_updated_path, 'w', encoding='utf-8') as file:
    file.write(network_output_updated)

network_data_updated_path
