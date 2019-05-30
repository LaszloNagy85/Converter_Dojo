# 2 / 10 converter

num = (input("Add number and the type of it(separated by space): ")).split()
n, v = int(num[0]), int(num[1])
bin = []
if v == 10:
    while n >= 1:
        bin.insert(0, n % 2)
        n = n // 2
    for i in range(len(bin)):
        bin[i] = str(bin[i])
    result = "".join(bin)
    print(f"The result is: {result} 2")

result = 0

if v == 2:
    n = str(n)
    n = n[::-1]
    for i in range(len(n)):
        if n[i] == "1":
            result = result + 2**i
    print(f"The result is: {result} 10")
