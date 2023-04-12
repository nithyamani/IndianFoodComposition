import csv

# This script processes the input file regionalNames.csv that was generated by the script 
# 1_food_index_from_IFCT_as_csv.py and groups the regional food names by the food code 
# INPUT: regionalNames.csv
# OUTPUT: regionalFoodNamesOrderedByCode.csv

input_file = 'regionalNames.csv'
output_file = 'regionalFoodNamesOrderedByCode.csv'

# Create a dictionary to store the data
data = {}

# Open the CSV file and read the data
with open(input_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['name']

        for col_name, code in row.items():
            if col_name not in ['name'] and code is not None and code !='':
                # Add the name to the dictionary for code1
                code = code.strip()
                if code in data:
                    data[code].append(name)
                else:
                    data[code] = [name]

# Open the output CSV file and write the data
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['code', 'names'])

    # Write the data rows
    for code, names in data.items():
        if code is not None and code != '':
            writer.writerow([code, '|'.join(names)])