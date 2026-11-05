# ===== Problem 9. Electricity Bill with Progressive Tiers =====

# (a) Calculate electricity bill
def electricity_bill(kwh):
    if kwh < 0:
        return None

    # Calculate kWh in each tier
    tier1 = min(kwh, 50)
    tier2 = min(max(kwh - 50, 0), 150)
    tier3 = max(kwh - 200, 0)

    # Calculate electricity cost
    cost = (tier1 * 480) + (tier2 * 610) + (tier3 * 730)

    # Add service fee and VAT
    total = (cost + 2000) * 1.10

    return round(total)


# (b) Print electricity bill table
print("Electricity Bill Table")

for kwh in [0, 35, 50, 120, 200, 350]:
    bill = electricity_bill(kwh)
    usd = bill / 4100

    print(f"{kwh} kWh -> {bill:,} riel (≈ {usd:.2f} USD)")


# (c) Ask user for monthly consumption
print()
kwh = float(input("Enter your monthly consumption (kWh): "))

bill = electricity_bill(kwh)

if bill is None:
    print("Invalid consumption!")
else:
    usd = bill / 4100
    print(f"Your electricity bill: {bill:,} riel (≈ {usd:.2f} USD)")