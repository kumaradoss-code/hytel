N=str(input('enter the string='))
length=len(N)
i=0
j=length
for row in range(length):
    for col in range(length):
        if row==i or col==j:
            print(N[row],end='  ')
            i+=1
            j-=1
        elif row==col:
            print(N[col],end='  ')
        else:
            print(end='  ')
    print()

