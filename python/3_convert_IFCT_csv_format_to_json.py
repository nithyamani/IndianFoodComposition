import csv
import json

# This script processes the input csv file IndianFoodCompositionTable_In_CSV_Format.csv 
# that was generated manually by consolidating the .csv file available 
# at https://github.com/ifct2017/compositions/tree/master/assets and convertes it into JSON format
# INPUT: IndianFoodCompositionTable_In_CSV_Format.csv
# OUTPUT: IndianFoodCompositionTable_In_JSON_Format.json

csv_file = open('IndianFoodCompositionTable_In_CSV_Format.csv', 'r')
json_data = []

# Create a CSV reader
reader = csv.DictReader(csv_file, delimiter=',')

food_groups = {
    'A': 'Cereals and Millets',
    'B': 'Grain Legumes',
    'C': 'Green Leafy Vegetables',
    'D': 'Other Vegetables',
    'E': 'Fruits',
    'F': 'Roots and Tubers',
    'G': 'Condiments and Spices',
    'H': 'Nuts and Oil Seeds',
    'I': 'Sugars',
    'J': 'Mushrooms',
    'K': 'Miscellaneous Foods',
    'L': 'Milk and Milk Products',
    'M': 'Egg and Egg Products',
    'N': 'Poultry',
    'O': 'Animal Meat',
    'P': 'Marine Fish',
    'Q': 'Marine Shellfish',
    'R': 'Marine Mollusks',
    'S': 'Fresh Water Fish and Shellfish',
    'T': 'Edible Oils and Fats'
}

# Iterate over each row in the CSV file
for row in reader:
    # Create a dictionary to store the data for each row
    row_data = {
        '_id': row['_id'],
        'code': row['code'],
        'name': row['name'],
        'no. of regions': int(row['regn']),
        'group': food_groups.get(row['code'][0], 'Unknown'),
        'nutrients': []
    }

    # Iterate over the columns in the row and add them to the collection list
    for col_name, col_val in row.items():
        if col_name not in ['_id','code', 'name', 'regn'] and col_val != 'x':
            v1, v2, v3 = col_name.split('|')
            category = v3.strip()
            composition = {
                'name': v1,
                'code': v2,
                'value': col_val
            }
            # Check if 'comp' already exists in the list for the same category
            category_exists = False
            for c in row_data['nutrients']:
                if c.get('category') == category:
                    if 'composition' in c and len(c['composition']) > 0:
                        c['composition'].append(composition)
                    else:
                        c['composition'] = [composition]
                    category_exists = True
                    break
            # If 'comp' doesn't exist for the category, add it to the list
            if not category_exists:
                row_data['nutrients'].append({
                    'category': category,
                    'composition': [composition]
                })

    # Remove duplicate categories
    categories = []
    for c in row_data['nutrients']:
        if c['category'] not in categories:
            categories.append(c['category'])
        else:
            row_data['nutrients'].remove(c)

    # Append the row data to the list of JSON data if it has at least one non-empty 'comp'
    if any(len(c['composition']) > 0 for c in row_data['nutrients']):
        json_data.append(row_data)

result = json.dumps(json_data, indent=4)
# save the JSON data to a file
with open('IndianFoodCompositionTable_In_JSON_Format.json', 'w') as output_file:
    output_file.write(result)