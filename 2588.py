a =int(input())
b =int(input())

일의자리 = b % 10
십의자리 = b  // 10 % 10
백의자리 = b // 100


print(a*일의자리)
print(a*십의자리)
print(a*백의자리)

print(a*b)