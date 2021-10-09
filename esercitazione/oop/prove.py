def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact
k=-5
while k<0:
    print("a")
    k+=k
