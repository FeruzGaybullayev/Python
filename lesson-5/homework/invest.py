def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount *= (1 + rate)
        print(f"year {year}: ${amount:.2f}")

# User input for investment
principal = float(input("Enter the initial amount: "))
annual_rate = float(input("Enter the annual percentage rate (as a decimal): "))
num_years = int(input("Enter the number of years: "))

invest(principal, annual_rate, num_years)