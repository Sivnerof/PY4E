hrs = float(input("Enter Hours:"))
rate = float(input("Rate: "))

if hrs < 40:
    print(hrs * rate)
    
else:
    print(((hrs - 40) * 1.5 * rate) + 40 * rate)