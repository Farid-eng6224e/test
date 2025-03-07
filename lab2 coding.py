#lab2
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
x=8
for i in range(9):
    if x>=9 and x<=12:
        y=2*(a**2)+3*x
    elif x>12:
        y=4*(b**2)-7*x
    else:
        y="False"

    print(y)
    x+=1
    