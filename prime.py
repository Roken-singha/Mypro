num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("The number is not a prime.")
            break
    else:
        print("The number is a prime.")
else:
    print("The number is not a prime.")
