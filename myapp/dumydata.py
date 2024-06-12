import pandas as pd
import numpy as np

# Define the cities you want to prioritize
priority_cities = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad",
    "Chennai", "Kolkata", "Surat", "Pune", "Jaipur", "Lucknow",
    "Kanpur", "Nagpur", "Visakhapatnam", "Bhopal", "Patna",
    "Ludhiana", "Agra", "Nashik", "Vadodara", "Gorakhpur",
    "Rajkot", "Meerut", "Varanasi", "Amritsar", "Srinagar",
    "Asansol", "Dhanbad", "Faridabad", "Jamshedpur", "Allahabad",
    "Aligarh", "Jalandhar", "Gwalior", "Vijayawada", "Jabalpur",
    "Kota", "Ranchi", "Madurai", "Raipur", "Chandigarh",
    "Solapur", "Trivandrum", "Salem", "Dehradun", "Hubli-Dharwad",
    "Moradabad", "Mysore", "Guwahati", "Tiruchirappalli"
]

# Read the existing CSV file
existing_data = pd.read_csv('/Users/arif/Downloads/archive-2/census2011.csv')

# Create a priority column based on the index of the cities
existing_data['Priority'] = existing_data['District'].apply(lambda x: priority_cities.index(x) if x in priority_cities else len(priority_cities))

# Sort the DataFrame based on the priority column
existing_data.sort_values(by='Priority', inplace=True)

# Define the additional data, generating Salary first
additional_data = {
    "Salary": np.random.randint(15000, 100000, len(existing_data))
}

# Use Salary to create other columns with np.where
additional_data["Living_Cost"] = np.where(additional_data["Salary"] > 80000,
                                          np.random.randint(25000, 40000, len(existing_data)),
                                          np.random.randint(10000, 15000, len(existing_data)))
additional_data["Health_Facility"] = np.where(additional_data["Salary"] > 70000,
                                              np.random.randint(7, 10, len(existing_data)),
                                              np.random.randint(4, 7, len(existing_data)))
additional_data["Transportation"] = np.where(additional_data["Salary"] > 70000,
                                             np.random.randint(7, 10, len(existing_data)),
                                             np.random.randint(4, 7, len(existing_data)))
additional_data["Education"] = np.where(additional_data["Salary"] > 70000,
                                        np.random.randint(7, 10, len(existing_data)),
                                        np.random.randint(4, 7, len(existing_data)))
additional_data["Job_Opportunities"] = np.where(additional_data["Salary"] > 50000,
                                                np.random.choice(["IT", "Business", "Engineering"], len(existing_data)),
                                                np.random.choice(
                                                    ["Agriculture", "Labour", "Construction", "Small business"],
                                                    len(existing_data)))
additional_data["Pollution"] = np.random.uniform(1, 100, len(existing_data))
additional_data["Crime"] = np.random.randint(1, 100, len(existing_data))

# Convert dictionary to DataFrame
additional_data_df = pd.DataFrame(additional_data)

# Merge existing data with additional data
merged_data = pd.concat([existing_data, additional_data_df], axis=1)

# Create a new filename with a descriptive name (e.g., census2011_modified.csv)
new_filename = '/Users/arif/Downloads/archive-2/census2011_modified2.csv'

# Save merged DataFrame to the new CSV file
merged_data.to_csv(new_filename, index=False)

print(f"Merged data saved to a new file: {new_filename}")
