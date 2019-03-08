soda = ['cola', 'fanta', 'sprite', 'juce', 'water', 'milk']
print("The first three items in the lisy are:" + str(soda[0:3]))
print("Three items from middle of the lisit are:" + str(soda[1:3]))
print("The last three items in the list are:" + str(soda[3:]))
friend_pizzas = ('Margaret', 'Pepperoni', 'Hawaiian')
print("My friends favorite pizzas are:")
for friend_pizza in friend_pizzas[0:2]:
    print(friend_pizza.title())