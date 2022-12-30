#Write a Python program to store first year percentage of students in array. 
#Write function for sorting array of floating point numbers in ascending order using 
#a) Selection Sort 
#b) Bubble sort and display top five scores.


#----------------------------------------------------Selection Sort------------------------------------------------------
def selectionsort(A):
    for i in range(no):
        min=i
        for j in range(i+1,no):
            if A[min]>A[j]:
                min=j
        A[min],A[i]=A[i],A[min]

    print("\nSelection Sort array : ")
    for i in range(no):
        print(A[i],end="   ")
    
    print("\nTop five studnets of class : ")
    B=A[::-1]
    for i in range(5):
        print(B[i],end="  ")
#-------------------------------------------------------Bubble Sort--------------------------------------------------------
def Bubblesort(A):
    for i in range(no):
        for j in range(no-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    
    print("\nBubble Sort array : ")
    for i in range(no):
        print(A[i],end="  ")

    print("\nTop five students of class : ")
    B=A[::-1]
    for i in range(5):
        print(B[i],end="  ")

#----------------------------------------------------------------------------------------------------------------------
Mark=[]
no=int(input("\nEnter the no of student in your class : "))
print("\nEnter Marks : ")
for i in range(no):
    Mark.append(float(input()))
ch=1
while(ch!=0):
    ch=int(input("\n1.Selection sort\n2.Bubble sort\n0.Exit\nEnter your choice : "))
    if ch==1 :
        selectionsort(Mark)
    elif ch==2 :
        Bubblesort(Mark)
    elif ch==0 :
        print("\n----Good Bye----")
	