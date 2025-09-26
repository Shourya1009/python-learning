import requests

# Function to get exchange rates
def get_exchange_rate(base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency.upper()}"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Error fetching exchange rates!")
        return None

    data = response.json()
    if "rates" not in data:
        print("❌ Invalid response from API!")
        return None

    rates = data["rates"]
    return rates.get(target_currency.upper())

# Main Program
def currency_converter():
    print("🌍 Currency Converter")
    print("======================")

    base = input("Enter base currency (e.g., USD, EUR, INR): ")
    target = input("Enter target currency (e.g., USD, EUR, INR): ")
    amount = float(input(f"Enter amount in {base.upper()}: "))

    rate = get_exchange_rate(base, target)
    if rate:
        converted = amount * rate
        print(f"\n✅ {amount:.2f} {base.upper()} = {converted:.2f} {target.upper()}")
    else:
        print("❌ Conversion failed. Try again!")

if __name__ == "__main__":
    currency_converter()
