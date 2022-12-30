#Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N students in the class. 
#Write functions to compute following: 
#a) The average score of class 
#b) Highest score and lowest score of class 
#c) Count of students who were absent for the test 
#d) Display mark with highest frequency

marks=list()
total=0
def add_marks():
    m=eval(input("*Enter 'A' if student is absent*\nEnter Marks : "))
    marks.append(m)
    global total
    total=total+1

def aveg():
    avg=0
    for i in marks :
        if type(i)==float:
            avg=avg+i
        else :
            global total
            total=total-1

    avg=avg/total
    print(f"Average Score of class : {avg}")

def highlow():
    temp=list()
    for i in marks :
        if type(i)==float :
            temp.append(i)
    print(f"Highest Score of class : {max(temp)}")
    print(f"Lowest Score of class : {min(temp)}")

def absent():
    count=0
    for i in marks :
        if i=='A':
            count=count+1
    print(f"No of student absent : {count}")

def frequency():
    freq={}
    for i in marks :
        if i in freq :
            freq[i]+=1
        else :
            freq[i]=1
    print(f"Frequency of class : {max(freq,key=freq.get)}")


ch=1
while(ch) :
    ch=int(input("\n1.Add Student marks\n2.Average score of class\n3.Highest & Lowest Score\n4.No. of Absent Students\n5.Frequency\n0.Exit\nEnter Your choice : "))

    if ch==1:
        add_marks()
    elif ch==2:
        aveg()
    elif ch==3:
        highlow()
    elif ch==4:
        absent()
    elif ch==5:
        frequency()
    elif ch==0:
        print("------Good Bye--------")
