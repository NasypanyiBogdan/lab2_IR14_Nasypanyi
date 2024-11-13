import math

def calculate_series(x, m, d):
    sum_value = 1
    term = 1
    n = 1
    
    while abs(term) >= d:
        term = (math.prod([m + k for k in range(n)]) / math.factorial(n)) * (x ** n)
        sum_value += term
        n += 1
        
    return sum_value

def tabulate_function(a, b, h, m, d):
    x = a
    results = []
    
    while x <= b:
        y = calculate_series(x, m, d)
        results.append((x, y))
        x += h
    
    return results

a = 0.1
b = 0.5
h = 0.05
d = 0.001
m = 3

table = tabulate_function(a, b, h, m, d)

for x, y in table:
    print(f"x = {x:.2f}, y = {y:.6f}")
