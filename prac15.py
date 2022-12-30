#Write a Python program to store second year percentage of students in Array. 
#Write function for sorting Aay of floating point numbers in ascending order using 
#a) Insertion sort 
#b) Shell Sort and display top five scores


#--------------------------------------------------Insertion sort------------------------------------------------
def insertionsort(A):
    for i in range(1,len(A)):
        key=A[i]
        j=i-1
        while j>=0 and key<A[j]:
            A[j+1]=A[j]
            j=j-1

        A[j+1]=key

    print("Insertion sort :\n")
    for i in range(no):
        print(A[i],end="  ")

    A.reverse()
    print("\nTop 5 student : ")
    for i in range(5):
        print(A[i])

#--------------------------------------------------------Shell Sort---------------------------------------------------
def shellsort(A):
    gap=no//2
    while gap>0:
        j=gap
        while j<no:
            i=j-gap
            while i>=0 :
                if A[i+gap] > A[i] :
                    break
                else :
                    A[i],A[i+gap]=A[i+gap],A[i]
                i=i-gap
            j+=1
        gap=gap//2

    print("\nShell sort :\n")
    for i in range(no):
        print(A[i],end="  ")

    inv=A[::-1] 
    print("\nTop 5 scores are : ")
    for i in range(5) : 
        print(inv[i])

#-----------------------------------------------------------------------------------------------------------------------------
marks=[]
no=int(input("Enter the number of student you want to enter : "))
print("Enter the numbers : ")
for i in range(no):
    marks.append(float(input()))

ch=1
while(ch):
    ch=int(input("1.Insertion Sort\n2.Shell Sort\n0.Exit\nEnter your Choice : "))
    if ch==1 :
        insertionsort(marks)
    elif ch==2 :
        shellsort(marks)
    elif ch==0 :
        print("-----Good Bye------")