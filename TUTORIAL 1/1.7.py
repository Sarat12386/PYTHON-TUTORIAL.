def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    elif x > 0 and y < 0:
        return "Quadrant IV"
    elif x == 0 and y != 0:
        return "Point lies on the Y-axis"
    elif y == 0 and x != 0:
        return "Point lies on the X-axis"
    else:
        return "Point lies at the origin"

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

result = find_quadrant(x, y)
print(result)
