import requests
import sys

def fetch_beers(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.RequestException as err:
        print(f"Error fetching data: {err}")
        sys.exit(1)

def filter_and_sort_beers(beers, min_abv):
    filtered_beers = [beer for beer in beers if beer['abv'] > min_abv]
    sorted_beers = sorted(filtered_beers, key=lambda x: x['abv'])
    return sorted_beers

def print_beers(beers):
    for beer in beers:
        if beer['abv'] < 5:
            emoji = '😐'
        elif 5 <= beer['abv'] <= 8:
            emoji = '🙂'
        else:
            emoji = '🥴'
        print(f"{beer['name']},{beer['abv']} {emoji}")

def main():
    url = 'https://s3-eu-west-1.amazonaws.com/kg-it/devopsTest/api-punkapi-com-v2-beers.json'
    if len(sys.argv) > 1:
        try:
            min_abv = float(sys.argv[1])
        except ValueError:
            print("Invalid ABV value. Please provide a numeric value.")
            sys.exit(1)
    else:
        min_abv = 0

    beers = fetch_beers(url)
    filtered_and_sorted_beers = filter_and_sort_beers(beers, min_abv)
    print_beers(filtered_and_sorted_beers)

if __name__ == "__main__":
    main()

# Example usage:
#   python3 beers.py 6
#   This will list all beers with ABV greater than 6, sorted by ABV.
#
#   python3 beers.py
#   This will list all beers, sorted by ABV, with no filtering.
# 
#   please drink responsibly 🍺 