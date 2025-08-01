import requests
url = "https://api.exchangerate-api.com/v4/latest/USD"
data = requests.get(url)
money = int(input("Enter the amount: "))
convert = money * data.json()['rates']['INR']
print(f"The converted amount is: {convert} INR")