import requests
import json

def fetch_all_laureates():
    """
    Fetches all laureate data from the Nobel Prize API using pagination.
    """
    all_laureates = []
    limit = 25
    offset = 0
    total_laureates = 0

    while True:
        url = f"https://api.nobelprize.org/2.1/laureates?limit={limit}&offset={offset}"
        print(f"Fetching data from: {url}")
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()
            
            # The API returns a 'laureates' key with a list of laureates
            laureates = data.get('laureates', [])

            if not laureates:
                # If the 'laureates' list is empty, we have fetched all data
                print("No more laureates to fetch. Reached the end.")
                break
            
            # Add the fetched laureates to our main list
            all_laureates.extend(laureates)

            # Check for the total count to track progress
            if 'meta' in data and 'count' in data['meta']:
                total_laureates = data['meta']['count']

            # Increment the offset for the next request
            offset += limit

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break
    
    print(f"\nSuccessfully fetched {len(all_laureates)} of {total_laureates} total laureates.")
    
    # Optionally, you can save the data to a JSON file
    with open("all_laureates.json", "w", encoding="utf-8") as f:
        json.dump(all_laureates, f, indent=4)
        
    print("Data saved to all_laureates.json")

    return all_laureates

if __name__ == "__main__":
    laureates_data = fetch_all_laureates()
    # You can now work with the `laureates_data` list
    # For example, print the name of the first laureate:
    if laureates_data:
        print(f"First laureate in the dataset: {laureates_data[0].get('fullName', {}).get('en')}")