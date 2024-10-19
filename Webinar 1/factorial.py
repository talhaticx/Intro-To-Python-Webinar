def fact(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    print(f"The factorial of {x} is {fact}")

for i in range(1, 11):
    fact(i)
