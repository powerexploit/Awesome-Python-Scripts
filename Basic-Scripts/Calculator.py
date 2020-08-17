print("You can type a sentence and interact.")

def calculator(num1,num2):
    #Executing the loop infinite times as we donot know how many times the user will want to run
    while(True):
        choice= input("Enter what you want to perform: ")
        print()

        #For Addition user can type any Sentence containing word related to it and will get the output but here we are checking only for the common words
        if ("addition" in choice) or ("add" in choice) or ("sum" in choice) or ("plus" in choice):
            sum = (num1) + (num2)
            print("Output....")
            print("Adding {} and {} results to {}".format(num1,num2,sum))
            print()
        
        #For Subtraction user can type any Sentence containing word related to it and will get the output but here we are checking only for the common words
        elif ("subtraction" in choice) or ("minus" in choice) or ("difference" in choice) or ("sbtract" in choice):
            if( num1 > num2 ):
                diff = (num1) - (num2)
                print("Output....")
                print("Subtracting {} from {} results to {}".format(num2,num1,diff))
                print()
            elif( num2 > num1 ):
                diff = (num2) - (num1)
                print("Output....")
                print("Subtracting {} from {} results to {}".format(num1,num2,diff)) 
                print()   
        
        #For Multiplication user can type any Sentence cpntaining word related to it and will get the output but here we are checking only for the common words
        elif ("multiplication" in choice) or ("product" in choice) or ("multiply" in choice):
            if(num1==0 or num2==0):
                print("Output....")
                print("Multiplying {} and {} results to 0".format(num1,num2))
                print()
            elif(num1==1):
                print("Output....")
                print("Multiplying {} and {} results to {}".format(num1,num2,num2))
                print()
            elif(num2==1):
                print("Output....")
                print("Multiplying {} and {} results to {}".format(num1,num2,num1))
                print()
            else:
                mul = (num1) * (num2)
                print("Output....")
                print("Multiplying {} and {} results to {}".format(num1,num2,mul))
                print()

        #For Division user can type any Sentence cpntaining word related to it and will get the output but here we are checking only for the common words
        elif("division" in choice) or ("divide" in choice) or ("quotient" in choice):
            if( num1 > num2 ):
                if(num2==0):
                    print("Output....")
                    print("Error: Please try with some other values!")
                
                elif(num1==0):
                    print("Output....")
                    print("Dividing {} from {} results to 0".format(num1,num2))
                    print()
                else:
                    div = (num1) / (num2)
                    print("Output....")
                    print("Dividing {} from {} results to {}".format(num1,num2,div))
                    print()
            elif(num1==0 and num2==0):
                print("Infinity!")
                print()
            elif( num2 > num1 ):
                if(num1==0):
                    print("Output....")
                    print("Error: Please try with some other values!")
                    print()
                
                elif(num2==0):
                    print("Output....")
                    print("Dividing {} from {} results to 0".format(num1,num2))
                    print()
                else:
                    div = (num2) / (num1)
                    print("Output....")
                    print("Dividing {} from {} results to {}".format(num2,num1,div))
                    print()
        
        #For exiting the loop user can type any Sentence containing word related to it and it will exit from the loop but here we are checking for the common words
        elif ("exit" in choice) or ("stop" in choice) or ("return" in choice):
            break 
        
        else:
            print()
            print("Operation not found: Please try again!")
            print()



def main():

    print()
    print("         THIS IS A BASIC USER FRIENDLY CALCULATOR!          ")
    print()
    print("You can type a sentence and interact.")
    print()
    #inputting two numbers at a time using the split function
    num1,num2 = input("Enter two numbers: ").split()
    num1=float(num1)
    num2=float(num2)


    #printing both the numbers
    print("Number 1 is: ",num1)
    print("Number 2 is: ",num2)
    print()

    calculator(num1,num2)
if __name__ == "__main__":
    main()
