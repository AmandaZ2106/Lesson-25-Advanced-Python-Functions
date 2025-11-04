Numbers1=[1,2,3]
Numbers2=[4,5,6]
result=map(lambda x,y:x+y,Numbers1,Numbers2)
print("Addition of lists:")
print(list(result))

num=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,num))
print("The square of the numbers in the list:")
print(square)