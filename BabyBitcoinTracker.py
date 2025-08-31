# Baby Bitcoin Tracker

balance_usd = 0.0
btc_owned = 0.0
btc_price = 20000.0  # fixed price for simplicity

def show_balance():
    print("\n==== Portfolio ====")
    print(f"Cash Balance: ${balance_usd:.2f}")
    print(f"BTC Owned: {btc_owned:.6f} BTC")
    print(f"Value of BTC: ${btc_owned * btc_price:.2f}")
    print("===================")

def buy_btc():
    global balance_usd, btc_owned
    amount = float(input("Enter USD amount to buy BTC: "))
    btc = amount / btc_price
    btc_owned += btc
    balance_usd -= amount
    print(f"You bought {btc:.6f} BTC.")

def sell_btc():
    global balance_usd, btc_owned
    amount = float(input("Enter BTC amount to sell: "))
    if amount > btc_owned:
        print("Not enough BTC.")
    else:
        btc_owned -= amount
        balance_usd += amount * btc_price
        print(f"You sold {amount:.6f} BTC.")

while True:
    print("\n==== Bitcoin Tracker Menu ====")
    print("1. Show Balance")
    print("2. Buy Bitcoin")
    print("3. Sell Bitcoin")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        buy_btc()
    elif choice == "3":
        sell_btc()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid option.")
