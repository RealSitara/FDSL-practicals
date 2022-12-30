#Write a Python program to compute following computation on matrix: 
#a) Addition of two matrices 
#b) Subtraction of two matrices 
#c) Multiplication of two matrices 
#d) Transpose of a matrix


a=list()
b=list()
res=list()
row=int(input("Enter no of rows of matrix : "))
col=int(input("Enter no of columns of matrix : "))

print("\nEnter values for 1st matrix : ")       #Matrix 1 input
for i in range(row) :
    x=list()
    for j in range(col):
        no=int(input())
        x.append(no)
    a.append(x)
    del x

print("\nEnter values for 2nd matrix : ")   #Matrix 2 input
for i in range(row) :
    x=list()
    for j in range(col):
        no=int(input())
        x.append(no)
    b.append(x)
    del x
#print(a)
#print(b)

#----------------------------------------------------Addition-----------------------------------------------------
print("\nAddition : \n")
for i in range(row):  
    x=list()
    for j in range(col):
        no=a[i][j]+b[i][j]
        x.append(no)
    res.append(x)
    del x

for i in res :
    print(i)

#--------------------------------------------------subtraction-------------------------------------------------------

print("\nSubtraction : \n")
for i in range(row):
    for j in range(col):
        res[i][j]=a[i][j]-b[i][j]

for i in res :
    print(i)

#--------------------------------------------------Multiplication------------------------------------------------------

print("\nMultiplication : \n")
for i in range(row):
    for j in range(col):
        res[i][j]=a[i][j]-b[j][i]

for i in res :
    print(i)

#---------------------------------------------------Transpose------------------------------------------------------------

print("\nTranspose of Matrix 1 : \n")  #Matrix 1 Transpose
for i in range(row):
    for j in range(col):
        res[i][j]=a[j][i]

for i in res :
    print(i)


print("\nTranspose of Matrix 2 : \n")  #Matrix 2 Transpose 
for i in range(row):
    for j in range(col):
        res[i][j]=b[j][i]

for i in res :
    print(i)