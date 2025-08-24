def is_armstrong(num):
    n = len(str(num))  
    total = sum(int(digit) ** n for digit in str(num))
    return total == num


num = int(input("Enter a number: "))
if is_armstrong(num):
    print("Armstrong number")
else:
    print("not an Armstrong number")
