import math

def first_function(x):
    return ( x^2 - 1)**(x - 1)
def second_function(x):
    return 1 / (math.sin(x) + abs(math.cos(x)))
def third_functin(x):
    return math.log(math.exp**x + 4)

a = 7.5
b = 10
h = 0.2
x = a 
result = [ ]

while x <= b :
    if x <= 8 :
        result.append((x, first_function(x)))
    elif 8 < x <= 9 :
        result.append((x, second_function(x)))
    elif x > 9 :
        result.append((x, third_functin(x)))

    x += h
    x = round(x, 3)

for x, y in result:
    print(f"x = {x}; f(x) = {y};")