i = int(input("数える数を指定してください："))
for num in range(1,i+1):
    if num % (3 * 5) == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)