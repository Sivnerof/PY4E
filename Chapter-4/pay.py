def computepay(hour, rate):
    if hour < 40:
        return hour * rate
    
    else:
        return ((hour - 40) * 1.5 * rate) + 40 * rate

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate: "))

pay = computepay(hrs, rate)
print("Pay", pay)