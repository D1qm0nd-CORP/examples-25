def in_same_quarter(x1, y1, x2, y2):
    x_coords_same_sign = (x1 > 0 and x2 > 0) or (x1 < 0 and x2 < 0)
    y_coords_same_sign = (y1 > 0 and y2 > 0) or (y1 < 0 and y2 < 0)
    return x_coords_same_sign and y_coords_same_sign


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print("YES" if in_same_quarter(x1,y1,x2,y2)==True else "NO")