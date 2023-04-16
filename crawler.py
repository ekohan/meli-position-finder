import requests
import csv
from config import api_key, pairs, output_type  # Import the required variables from config.py

country_code = 'MLA'  

def find_matching_items(item_id, reference_query, max_pages=10, results_per_page=50):
    page = 0
    found = False
    total_results_iterated = 0

    while not found and page < max_pages:
        offset = page * results_per_page
        url = f'https://api.mercadolibre.com/sites/{country_code}/search?q={reference_query}&access_token={api_key}&limit={results_per_page}&offset={offset}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            results = data['results']
            total_results_iterated += len(results)

            print(f"Searching for {item_id} using query '{reference_query}'... Page {page + 1} of {max_pages} ({total_results_iterated} results iterated so far)")

            for index, result in enumerate(results):
                if result['id'] == item_id:
                    found = True
                    break

            page += 1
        else:
            print(f"Error: Unable to fetch data. Status code {response.status_code}")
            break

    if not found:
        print(f"No match found for item_id '{item_id}'. Iterated over {total_results_iterated} results.")
        
    return found, offset + index + 1 if found else None, result['title'] if found else None

results_list = []
for item_id, reference_query in pairs:
    found, position, title = find_matching_items(item_id, reference_query)
    results_list.append((item_id, reference_query, found, position, title))

if output_type == 'csv':
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Item ID', 'Reference Query', 'Found', 'Position', 'Title'])
        for result in results_list:
            csv_writer.writerow(result)
else:  # Output to screen
    for result in results_list:
        print(f"Item ID: {result[0]}")
        print(f"Reference Query: {result[1]}")
        if result[2]:
            print(f"Position: {result[3]}")
            print(f"Title: {result[4]}")
        else:
            print("Item not found")
        print('-' * 80)