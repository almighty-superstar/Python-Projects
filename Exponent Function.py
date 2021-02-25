number=input("Input a whole number:")
power=input("Enter the exponent, which is also a whole number:")

def raise_to_power(number,power):
    base=0
    # line above to define base
    base=number
    for power in range(power-1):
        number=number*base
    print(number)

raise_to_power(int(number),int(power))