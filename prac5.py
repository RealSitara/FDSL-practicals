#Write a Python program to compute following operations on String: 
#a) To display word with the longest length 
#b) To determines the frequency of occurrence of particular character in the string 
#c) To check whether given string is palindrome or not 
#d) To display index of first appearance of the substring 
#e) To count the occurrences of each word in a given string


ch=1
str=input("Enter the string : ")
l=str.split()
while(ch) :
    ch=int(input("\n\n1.Longest word\n2.Frequency of character\n3.Check palindrome\n4.First appearance of substring\n5.occurrence of each word\n0.Exit\nEnter your choice : "))
    if ch==1:
        largest=max(l,key=len)
        print(f"\nThe longest word in the given string is : {largest} \n It's length is : {len(largest)}")
    elif ch==2:
        freq={}
        fch=input("\nEnter the character : ")
        for i in str :
            if i in freq :
                freq[i]+=1
            else :
                freq[i]=1
        if fch in freq :
            print(f"\nFrequency of {fch} is : {freq[fch]}")
    elif ch==3:
        pal=input("\nEnter a string to be checked : ")
        if pal==pal[::-1] :
            print(f"\nThe given string {pal} is palindrome ")
        else : 
            print(f"\nThe given string {pal} is not palindrome ")
    elif ch==4:
        f=input("\nEnter a string to be find : ")
        if f in l :
            print(f"\nThe Sting foud at : {str.find(f)}")
        else : 
            print("\nGiven substring in not prsent in the string")
    elif ch==5:
        freq={}
        for i in l :
            if i in freq :
                freq[i]+=1
            else :
                freq[i]=1
        print(f"\nFrequency of each word :\n{freq}")
    elif ch==0:
        print("\n-----Good Bye------")

