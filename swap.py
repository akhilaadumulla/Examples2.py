X=5
Y=4
X,Y=Y,X 
print("X= ",X)
print("Y= ",Y)


X=input("Enter value of X: ")
Y=input("Enter value of Y: ")
temp=X
X=Y
Y=temp
print("The value of X after swapping: {}".format(X))
print("The value of Y after swapping: {}".format(Y))