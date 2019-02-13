for value in range(1, 5):
    print(value)
number = list(range(1, 6))
print(number)
numbers = list(range(2, 11, 2))
print(numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
#Можно записать тот же код более компактным способом(опустить переменную square)
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

squares = [value**2 for value in range(1, 11)]
print(squares)