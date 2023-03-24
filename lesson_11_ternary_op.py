# унарный оператор
print(+7)
print(-7)


# бинарный оператор
print(1 + 2)


# тернарный оператор
score = int(input('Enter your score: '))
message = 'Ты лучший!' if score >= 80 else 'Учись играть, нубик!'
print(message)

x = 0
y = 1 + 1 if x == 1 else 2 + 2
print(y)