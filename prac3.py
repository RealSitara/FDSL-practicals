#Write a Python program for department library which has N books, write functions for following: 
#a) Delete the duplicate entries 
#b) Display books in ascending order based on cost of books 
#c) Count number of books with cost more than 500. 
#d) Copy books in a new list which has cost less than 500.

total=int(input("Enter the number of total books : "))
book=[]
def delete(a):
    ans=[]

    for i in a :
        if i not in ans :
            ans.append(i)
    return ans 

costm=[]
def costmore(a) :
    for i in a : 
        if i[0] > 500 : 
            costm.append(i)
    return len(costm)

costl=[]
def costless(a) :
    for i in a : 
        if i[0] < 500 : 
            costl.append(i)
    return costl


for i in range(1,total+1) :

    name=input(f"Enter name of book {i} : ")
    cost=int(input(f"Enter cost of book {i} : "))
    book.append([cost,name])
#print(book)

choice=1
dup=delete(book)

while(choice!=0):
    choice=int(input("1.Delete duplicate Entries\n2.Display books in ascending order\n3.Books which cost more that 500\n4.Books which cost less than 500\n0.Exit\n Enter your choice :"))
    if choice==1 :
        #dup=delete(book)
        print(dup)
    elif choice==2 :
        print(sorted(dup))
    elif choice==3 : 
        print(f"Number of books cost more than 500 : {costmore(dup)}")
    elif choice==4 :
        print(f"Books which cost less than 500 : \n {costless(dup)}")
