
# Q4:

import json

# Load the JSON data from the uploaded file
file_path ="C:/Users/Sanjana/Downloads/DataEngineeringQ2.json"

with open(file_path, 'r') as file:
    data = json.load(file)

# Initialize counters
total_records = len(data)
missing_first_name = 0
missing_last_name = 0
missing_dob = 0

# Count missing values for each field
for record in data:
    patient_details = record.get("patientDetails", {})
    # Check for missing firstName
    if not patient_details.get("firstName"):
        missing_first_name += 1
    # Check for missing lastName
    if not patient_details.get("lastName"):
        missing_last_name += 1
    # Check for missing birthDate (DOB)
    if not patient_details.get("birthDate"):
        missing_dob += 1

# Calculate percentages
missing_first_name_pct = (missing_first_name / total_records) * 100
missing_last_name_pct = (missing_last_name / total_records) * 100
missing_dob_pct = (missing_dob / total_records) * 100

# Round percentages to 2 decimal places
missing_first_name_pct = round(missing_first_name_pct, 2)
missing_last_name_pct = round(missing_last_name_pct, 2)
missing_dob_pct = round(missing_dob_pct, 2)

print(missing_first_name_pct, missing_last_name_pct, missing_dob_pct)




# Q5:

from collections import Counter
import json

# Load the JSON data from the uploaded file
file_path ="C:/Users/Sanjana/Downloads/DataEngineeringQ2.json"

with open(file_path, 'r') as file:
    data = json.load(file)

# Extract gender data and calculate mode
genders = [record.get("patientDetails", {}).get("gender", None) for record in data]
gender_counts = Counter(filter(None, genders))  # Exclude None or missing values

# Find mode (most common gender)
mode_gender = gender_counts.most_common(1)[0][0]

# Impute missing genders with the mode
imputed_genders = [gender if gender else mode_gender for gender in genders]

# Calculate the percentage of female gender after imputation
total_records = len(imputed_genders)
female_count = imputed_genders.count("F")
female_percentage = (female_count / total_records) * 100

# Round the percentage to 2 decimal places
female_percentage = round(female_percentage, 2)

print(female_percentage)

# Q6:

from datetime import datetime
import json

# Load the JSON data from the uploaded file (use your file path here)
file_path = "C:/Users/Sanjana/Downloads/DataEngineeringQ2.json"

with open(file_path, 'r') as file:
    data = json.load(file)

# Define a function to categorize age
def categorize_age(birth_date):
    if not birth_date:
        return None
    birth_date = datetime.strptime(birth_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    age = (datetime.now() - birth_date).days // 365  # Calculate age in years
    if age <= 12:
        return 'Child'
    elif age <= 19:
        return 'Teen'
    elif age <= 59:
        return 'Adult'
    else:
        return 'Senior'

# Add ageGroup column
for record in data:
    patient_details = record.get("patientDetails", {})
    birth_date = patient_details.get("birthDate")
    age_group = categorize_age(birth_date)
    patient_details["ageGroup"] = age_group

# Count the number of 'Adult' age groups
adult_count = sum(1 for record in data if record.get("patientDetails", {}).get("ageGroup") == "Adult")

# Print the count of adults
print(adult_count)

# Q7:

import json

# Load the JSON data from the uploaded file (use your file path here)
file_path = "C:/Users/Sanjana/Downloads/DataEngineeringQ2.json"

with open(file_path, 'r') as file:
    data = json.load(file)

# Calculate the total number of medicines prescribed
total_medicines = sum(len(record.get("consultationData", {}).get("medicines", [])) for record in data)

# Calculate the average number of medicines prescribed
average_medicines = total_medicines / len(data)

# Round the average to 2 decimal places
average_medicines = round(average_medicines, 2)

# Print the average number of medicines
print(average_medicines)

# Q8:

import json
from collections import Counter

# Load the JSON data
with open("C:/Users/Sanjana/Downloads/DataEngineeringQ2.json", 'r') as file:
    data = json.load(file)

# Extract all medicine names
medicine_names = []
for record in data:
    consultation_data = record.get("consultationData", {})
    medicines = consultation_data.get("medicines", [])
    medicine_names.extend([medicine["medicineName"] for medicine in medicines])

# Count occurrences of each medicine
medicine_counts = Counter(medicine_names)

# Get the 3rd most common medicine
third_most_common = medicine_counts.most_common(3)[2][0]
print(third_most_common)

# Q9:

import json

# Load the JSON data from the uploaded file (use your file path here)
file_path = "C:/Users/Sanjana/Downloads/DataEngineeringQ2.json"

with open(file_path, 'r') as file:
    data = json.load(file)

# Calculate the total number of active and inactive medicines
active_medicines = 0
inactive_medicines = 0

# Count the active and inactive medicines across all records
for record in data:
    medicines = record.get("consultationData", {}).get("medicines", [])
    for medicine in medicines:
        if medicine.get("isActive"):
            active_medicines += 1
        else:
            inactive_medicines += 1

# Calculate the total number of medicines
total_medicines = active_medicines + inactive_medicines

# Calculate the percentage distribution of active and inactive medicines
active_percentage = (active_medicines / total_medicines) * 100
inactive_percentage = (inactive_medicines / total_medicines) * 100

# Round the percentages to 2 decimal places
active_percentage = round(active_percentage, 2)
inactive_percentage = round(inactive_percentage, 2)

# Print the result as comma-separated values
print(f"{active_percentage},{inactive_percentage}")


# Q10:

import json
from collections import Counter
from datetime import datetime
# Load the JSON data from the uploaded file
file_path = "C:/Users/Sanjana/Downloads/DataEngineeringQ2.json"
with open(file_path, 'r') as file:
    data = json.load(file)
# Function to check if a phone number is valid
def is_valid_phone_number(phone_number):
    phone_number = str(phone_number).strip()  # Ensure the phone number is a string and remove any spaces
    if len(phone_number) > 10:
        if phone_number.startswith("+91"):
            phone_number = phone_number[3:]  # Remove the +91 prefix
        elif phone_number.startswith("91"):
            phone_number = phone_number[2:]  # Remove the 91 prefix
        else:
            return False  # Invalid if it doesn't start with +91 or 91
    # Check if the remaining part is exactly 10 digits and within valid range
    if len(phone_number) == 10 and phone_number.isdigit():
        return 6000000000 <= int(phone_number) <= 9999999999
    return False

# Add the "isValidMobile" column
valid_count = 0
for record in data:
    phone_number = record.get("phoneNumber", "")
    is_valid = is_valid_phone_number(phone_number)
    record["isValidMobile"] = is_valid
    if is_valid:
        valid_count += 1

# Save the updated JSON back to a file
output_path = "C:/Users/Sanjana/Downloads/DataEngineeringQ2.json"
with open(output_path, 'w') as file:
    json.dump(data, file, indent=4)

print(valid_count)

# Q11:


import json
from datetime import datetime
import numpy as np

# Load the JSON data
with open('C:/Users/Sanjana/Downloads/DataEngineeringQ2.json', 'r') as file:
    data = json.load(file)

# Initialize lists for patient age and number of medicines
ages = []
num_medicines = []

# Current year to calculate age
current_year = datetime.now().year

# Process each record
for record in data:
    # Calculate patient age
    birth_date = record.get("patientDetails", {}).get("birthDate")
    if birth_date:
        try:
            # Handle the ISO format with 'Z' suffix
            birth_year = datetime.strptime(birth_date, "%Y-%m-%dT%H:%M:%S.%fZ").year
            age = current_year - birth_year
            
            # Count the number of prescribed medicines
            medicines = record.get("consultationData", {}).get("medicines", [])
            num_meds = len(medicines)

            # Append to lists
            ages.append(age)
            num_medicines.append(num_meds)
        except ValueError:
            print(f"Invalid date format for record: {birth_date}")

# Calculate Pearson correlation
if len(ages) > 1 and len(num_medicines) > 1:
    correlation = np.corrcoef(ages, num_medicines)[0, 1]
    print(f"{correlation:.2f}")
else:
    print("Not enough data for correlation calculation.")






