from tkinter import *
# function for removing common characters with their corresponding occurrences
def removeCommon(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            #drop the common charcter and return concatinated list with true flag
            if list1[i] == list2[j]:
                common = list1[i]
                list1.remove(common)
                list2.remove(common)
                # concatenation of two list elements with *
                # * is act as border mark here
                list3 = list1 + ["*"] + list2
                # return the concatenated list with True flag
                return [list3, True]
    #when no common characters are found
    list3 = list1 + ["*"] + list2
    return [list3, False]
#convert the players name string to list
def stringToListConvert(str):
    # converted all letters into lower case
    str=str.lower()
    # replace any space with empty string
    str.replace("","")
    # convert into list
    strList=list(str)
    return strList

# function for telling the relationship status
def resultStatus():
    # take a 1st player name from Player1Field entry box
    p1 = Player1Field.get()
    # convert the players name string to list
    p1_list = stringToListConvert(p1)
    # take a 2nd player name from Player2Field entry box
    p2 = Player2Field.get()
    # convert the players name string to list
    p2_list = stringToListConvert(p2)
    # taking a flag as True initially
    flag = True
    # call removeCommon function untill common characters is found
    while flag:
        # function calling and store return value
        ret_list = removeCommon(p1_list, p2_list)
        # take out concatenated list from return list
        con_list = ret_list[0]
        # take out flag value from return list
        flag = ret_list[1]
        # find the index of "*" / border mark
        star_index = con_list.index("*")
        # all characters before * store in p1_list
        p1_list = con_list[: star_index]
        # all characters after * store in p2_list
        p2_list = con_list[star_index + 1:]
        # count total remaining characters
    count = len(p1_list) + len(p2_list)

    # full form of FLAMES
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    # keep looping untill only one item is not remaining in the result list
    while len(result) > 1:
        split_index = (count % len(result) - 1)
        # anticlock-wise circular counting.
        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[: split_index]
            result = right + left

        else:
            result = result[: len(result) - 1]

            # insert value
    Status_field.insert(10, result[0])


# Function for clearing the contents of all text entry boxes
def clear_all():
    Player1Field.delete(0, END)
    Player2Field.delete(0, END)
    Status_field.delete(0, END)

    # set focus on the Player1Field entry box
    Player1Field.focus_set()


# Driver code
if __name__ == "__main__":
    master = Tk()
    # Set the background colour of GUI window
    master.configure(background='light blue')

    # Set the configuration of GUI window
    master.geometry("350x125")

    # set the name of tkinter GUI window
    master.title("Flames Game")

    # Create a Player 1 Name: label
    label1 = Label(master, text="Player 1 Name: ",
                   fg='black', bg='blue')

    # Create a Player 2 Name: label
    label2 = Label(master, text="Player 2 Name: ",
                   fg='black', bg='blue')

    # Create a Relation Status: label
    label3 = Label(master, text="You both are: ",
                   fg='black', bg='blue')

    #  placing the widgets at respective positions
    label1.grid(row=1, column=0, sticky="E")
    label2.grid(row=2, column=0, sticky="E")
    label3.grid(row=4, column=0, sticky="E")

    # for filling or typing the information.
    Player1Field = Entry(master)
    Player2Field = Entry(master)
    Status_field = Entry(master)

    #  placing the widgets at respective positions
    Player1Field.grid(row=1, column=1, ipadx="50")
    Player2Field.grid(row=2, column=1, ipadx="50")
    Status_field.grid(row=4, column=1, ipadx="50")


    # Submit Button and attached to tell_status function
    button1 = Button(master, text="Submit", bg="red",
                     fg="black", command=resultStatus)


    #  Clear Button and attached to clear_all function
    button2 = Button(master, text="Clear", bg="red",
                     fg="black", command=clear_all)

    #  placing the widgets at respective positions
    button1.grid(row=3, column=1)
    button2.grid(row=5, column=1)

    # Start the GUI
    master.mainloop()