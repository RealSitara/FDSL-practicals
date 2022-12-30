#In second year computer engineering class, group A student’s play cricket, group B students play badminton and group C students play football. 
# Write a Python program using functions to compute following: - 
# a) List of students who play both cricket and badminton 
# b) List of students who play either cricket or badminton but not both 
# c) Number of students who play neither cricket nor badminton 
# d) Number of students who play cricket and football but not badminton. 
# (Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in functions)


name=" "
student=set()
cricket=set()
football=set()
batminton=set()

def add_stud():
    name=input("Enter the name of studnet : ")
    student.add(name)
    ifbat=input(f"Enter yes if {name} plays batminton : ")
    ifcri=input(f"Enter yes if {name} plays Cricket : ")
    iffoot=input(f"Enter yes if {name} plays football : ")

    if ifbat=="yes":
        batminton.add(name)
    if ifcri=="yes":
        cricket.add(name)
    if iffoot=="yes":
        football.add(name)

def display():
    x=1
    while(x!=0) :
        x=int(input("\n0.Back\n1.Student list\n2.Student cricket & batminton\n3.either cricket or batminton\n4.cricket & football not batminton\n5.No cricekt no football\nEnter your choice : "))
        if x==1 :
            print("-----STUDENT LIST-----")
            for i in student :
                print(i)
        elif x==2:
            print("------STUDENT IN CRICKET & BATMINTON-------")
            for i in cricket & batminton :
                print(i)
        elif x==3:
            print("--------STUDENTS IN CRICKET OR BATMINTON--------")
            for i in cricket|batminton :
                print(i)
        elif x==5:
            count=0
            for i in student :
                if i not in cricket|batminton :
                    count=count+1
            print(f"Number of students who play neither cricket nor batminton : {count}")
        elif x==4 :
            count=0
            for i in cricket&football :
                if i not in batminton :
                    count=count+1
            print(f"Number of students who play cricket and football but not badminto : {count}")
ch=1

while ch!=0 :
    ch=int(input("\n1.Add student\n2.Display\n0.Exit\nEnter your choice : "))
    if ch==1:
        add_stud()
    elif ch==2:
        display()
    elif ch==0 :
        print("\n-----Good Bye------")
    else :
        print("inavlid choice !")