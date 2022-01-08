# Storing patient names and insurance costs
medical_costs = {}
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
medical_costs["Vinay"] = 3325.0
total_cost = 0
for cost in medical_costs.values():
      total_cost += cost
average_cost = total_cost / len(medical_costs)
print(f"Average Insurance Cost: {average_cost}")

# List Comprehension to Dictionary
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]
names_to_ages = {key: value for key, value in zip(names, ages)}
marina_age = names_to_ages.get("Marina", None)
print(f"Marina's age is {marina_age}")

# Using a Dictionary to create a medical database
medical_records = {}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}
print(f"Connie's insurance cost is {medical_records['Connie']['Insurance_cost']} dollars.")
medical_records.pop("Vinay")
for name, record in medical_records.items():
      print(f"{name} is a {record['Age']} year old {record['Sex']} {record['Smoker']} with a BMI of {record['BMI']} and insurance cost of {record['Insurance_cost']}")
