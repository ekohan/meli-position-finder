import requests
import csv
from config import api_key, pairs, output_type  # Import the required variables from config.py
from pathlib import Path
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

country_code = 'MLA'  

def save_to_csv(item_id, reference_query, found, position, title, filename="output.csv"):
    file_exists = Path(filename).is_file()

    with open(filename, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['item_id', 'reference_query', 'found', 'position', 'title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            'item_id': item_id,
            'reference_query': reference_query,
            'found': found,
            'position': position,
            'title': title,
        })

def setup_session(retries=3, backoff_factor=0.3, timeout=5):
    session = requests.Session()
    
    retry = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"]
    )
    
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    session.timeout = timeout
    
    return session

def find_matching_items(api_key, pairs, output_type='screen'):
    session = setup_session()

    for index, pair in enumerate(pairs, start=1):
        item_id, reference_query = pair

        print(f"Processing pair {index} of {len(pairs)}: Item ID {item_id}, Reference Query '{reference_query}'")

        search_url = f"https://api.mercadolibre.com/sites/MLA/search?search_type=scan&q={reference_query}"
        headers = {"Authorization": f"Bearer {api_key}"}

        has_next_page = True
        found = False
        while has_next_page:
            response = session.get(search_url, headers=headers)
            results = response.json()

            items = results["results"]

            for position, item in enumerate(items):
                if item["id"] == item_id:
                    found = True
                    if output_type == "screen":
                        print(f"{position + 1}: {item['title']}")
                    elif output_type == "csv":
                        save_to_csv(item_id, reference_query, found, position + 1, item['title'])

            has_next_page = "next" in results["paging"]
            if has_next_page:
                search_url = results["paging"]["next"]

        if not found:
            if output_type == "screen":
                print(f"No match found for item_id '{item_id}'.")
            elif output_type == "csv":
                save_to_csv(item_id, reference_query, found, None, None)


find_matching_items(api_key, pairs, output_type)