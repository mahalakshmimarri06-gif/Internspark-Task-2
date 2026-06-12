import requests

# 1. Ensure the function receives 'country_name' as an argument
def get_universities(country_name): 
    # Now this 'country_name' matches the one in your function definition
    url = f"http://universities.hipolabs.com/search?country={country_name}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def main():
    country = input("Enter country name (e.g., India): ")
    # 2. Pass the 'country' variable into the function here
    uni_list = get_universities(country) 
    
    print(f"\nFound {len(uni_list)} universities:")
    for uni in uni_list[:10]:
        print(f"- {uni['name']}")

if __name__ == "__main__":
    main()