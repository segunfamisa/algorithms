def  StairCase(n):
    space = " "
    fill = "#"
    for step in range(1, n+1):
        print (space * (n - step)) + (fill * step)


StairCase(6)
