# Step 1: Import json module
import json

# Step 1: JSON string
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Load the JSON string into a Python dictionary
data = json.loads(sampleJson)

# Step 2: Access the nested "salary" key
salary = data["company"]["employee"]["payable"]["salary"]
print("Employee salary:", salary)

# Step 3: Add the "birth_date" key to the employee dictionary
# Replace "YYYY-MM-DD" with an actual date, e.g., "1990-05-12"
data["company"]["employee"]["birth_date"] = "1990-05-12"

# Optional: print updated dictionary to check
print("\nUpdated employee data:")
print(json.dumps(data, indent=4))

# Step 4: Save the modified JSON to a file
with open("modified_employee.json", "w") as f:
    json.dump(data, f, indent=4)

print("\nModified JSON saved to 'modified_employee.json'.")
