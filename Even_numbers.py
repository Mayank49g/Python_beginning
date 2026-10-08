#program that return even values from 1 to x.
# 1st way
n = int(input("Enter the number:"))
def even(x): 
    l = []
    for i in range(1,x+1):
        if i%2==0:
            l.append(i)
    
    return l, f"Total even no. {len(l)}"

n,c = even(n)
print(n)
print(c)
#2nd way
#program that return even values from 1 to x.
'''def even(x):
    for i in range(1,x+1):
        l = []
        if i%2==0:
            l.append(i)
    return l

a = even(10)
print(a)'''

#which is correct and why?
#2nd way Resets the list to empty ([]) on every single loop iteration.
#Hence 1st is correct.
