# Python program to count positive and negative numbers in a List given by user 
def count_pos_neg(list1):
    ''' we have to to count total number of positive elements and total number of negative number so we iterate the list1 and then we check every element wheather
    it is greater than 0 or not. if element is grater than or equal to 0 then we count it as positive element and if it is small then 0  then we count it as negative'''
    pos_count, neg_count = 0, 0
    for num in list1:                           # iterating each number in list 
        if num>=0:                            # checking condition 
            pos_count += 1
        else: 
            neg_count += 1      
    print("Positive numbers in the list: ", pos_count) 
    print("Negative numbers in the list: ", neg_count) 

#main program
if __name__ == "__main__":
    num = int(input("Enter number of elements: "))
    #list of numbers
    lst = []
    for index in range(0,num):
        #print() 
        ele=int(input("Enter "+str(index)+"th element: "))
        lst.append(ele)        
    count_pos_neg(lst)
