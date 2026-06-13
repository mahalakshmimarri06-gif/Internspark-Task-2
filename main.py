import requests

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 5, "page": 1}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def main():
    print("--- Live Crypto Price Tracker ---")
    data = get_crypto_prices()
    if data:
        search = input("Enter a coin name to search (or press Enter for top 5): ").lower()
        print(f"\n{'NAME':<20} | {'PRICE (USD)':<15}")
        print("-" * 35)
        found = False
        for coin in data:
            if search in coin['name'].lower() or search == "":
                print(f"{coin['name']:<20} | ${coin['current_price']:,.2f}")
                found = True
        if not found:
            print("Coin not found in top 5.")
    else:
        print("No data retrieved.")

if __name__ == "__main__":
    main()
