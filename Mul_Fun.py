class multiple_function():
    def subfields():
        print("sub-fields in AI are: ")
        disreslut=['Machine Learning','Neural Networks','vision','robotics','speech processing','natural language processing']
        for i in disreslut:
            print(i)    
    def oddeven():
        evenfind=int(input("Enter a number: "))
        if (evenfind%2) ==0:
            print(evenfind, "is even number")
        else:
            print(evenfind, "is not even number")  
    def elegible():
        find_gender=input("Your Gender:")
        find_gender_Age =int(input("Your Age:"))
        if (find_gender=="male"):
            if find_gender_Age <18:
                print("Not Eligible")
            else:
                print("Eligible")
        elif(find_gender=="female"):
            if find_gender_Age <18:
                print("Not Eligible")
            else:
                print("Eligible")
    def percentage():
        mark1=int(input("Subject1= "))
        mark2=int(input("Subject2= "))
        mark3=int(input("Subject3= "))
        mark4=int(input("Subject4= "))
        mark5=int(input("Subject5= "))
        tot=mark1+mark2+mark3+mark4+mark5
        print("Total : ",tot)
        print("Percentage : ",((tot / 500) * 100))
        
    def triangle():
        intheight=int(input("Height: "))
        intBreadth=int(input("Breadth: "))
        print("Area formula:  (intheight*intBreadth)/2")
        print("Area of Triangle:: ", (intheight*intBreadth)/2)
        Height1=int(input("Height1: "))
        Height2=int(input("Height2: "))
        Breadth=int(input("Breadth: "))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle :", Height1+Height2+Breadth)