class exampleprograms():
    def Subfields():
            print("Sub-fields in AI are:")
            print("Machine Learning")
            print("Neural Networks")
            print("Vision")
            print("Robotics")
            print("Speech Processing")
            print("Natural Language Processing")

    def oddeven(num):
        if num%2!=0:
                print("odd number")
                number="The given number is odd"        
        else:
            print("even number")
            number="The given number is even number"
                   
        return number
        
            
            
    def Eligible(Gender, age):
                print("Your Gender:", Gender)
                print("Your Age:", age)
                if Gender == "male" and age > 21:
                    print("Eligible for marriage:")
                    Marriage = "Eligible"
                elif Gender == "female" and age > 18:
                    print("Eligible for marriage:")
                    Marriage = "Eligible"
                else:
                    print("Not Eligible")
                    Marriage = "Not Eligible"
                return Marriage                        
        
    
    def marks_report(s1, s2, s3, s4, s5):
            total = s1 + s2 + s3 + s4 + s5
            percentage = (total / 500) * 100
            print("Subject1 =", s1)
            print("Subject2 =", s2)
            print("Subject3 =", s3)
            print("Subject4 =", s4)
            print("Subject5 =", s5)
            print("Total :", total)
            print("Percentage :", percentage)
    
    def Triangle(Height,Breadth):
            print("Height:",Height)
            print("Breadth:",Breadth)
            formula=(Height*Breadth)/2
            print("Area of Triangle:",formula)
            H1 =2
            H2 =4
            bd =4
            print("Height1:", H1)
            print("Height2:", H2)
            print("Breadth:", bd)
            Perimeter_formula = H1 + H2 + bd
            print("Perimeter formula: Height1+ Height2+Breadth")
            print("Perimeter of Triangle:", Perimeter_formula)
        
        
    
    
        
    
    
                
        
