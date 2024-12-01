name = "Haris"

def greet(name):
    print(f'Hello {name}')
    print("Have a nice day\n")

# greet("talha")

# names = ["Talha", "Abdullah", "Amna", "Rafeh"]

# for name in names:
#     greet(name)

# def SumNums(a, b):
#     print(a+b)

# SumNums(93, 28)

def SumNums(a, b):
    return a+b

num = SumNums(93, 28)

num2 = SumNums(num, num)

print(num2)