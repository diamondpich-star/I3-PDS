# ATM Cash Withdrawal System
money = {
    100: 50,
    50: 20,
    20: 300,
    10: 0,
    5: 200,
    1: 10
}
amount = int(input("Enter amount: $"))
if amount <= 0:
    print("Invalid amount!")
else:
    for bill in money:
        count = min(amount // bill, money[bill])
        if count > 0:
            print("$", bill, "x", count)
            amount = amount - (bill * count)
            money[bill] = money[bill] - count
    if amount == 0:
        print("Withdrawal successful!")
    else:
        print("Not enough money in ATM!")
        print("Remaining amount:", amount)

