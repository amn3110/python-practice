def triangle(a, b, c):
    if a ==b and b ==c and c ==a:
        return "equilateral"
    elif a ==b or b ==c or c == a:
        return "isosceles"
    else:
        return "scalene"
print(triangle(10,10,10))