"""This code basically automates various system operations.
It is a very interactive and user-friendly program
The two modules used are os and pyttsx3."""

def system_operations():
    import pyttsx3 
    import os
    pyttsx3.speak("Feel free to type in any statement!")
    while(True):
        
        operation=input("Please type which operation you want to peform? :\n ")
        
        print()
        operation= operation.lower()
    
        if("chrome" in operation) or ("browser" in operation):
            pyttsx3.speak("Please wait opening chrome for you")
            os.system("chrome")
        
        elif("notepad" in operation) or ("text editor" in operation) or ("text document" in operation):
            pyttsx3.speak("Please wait opening notepad for you")
            os.system("notepad")

        elif("media player" in operation) or ("player" in operation) or ("windows media player" in operation):
            pyttsx3.speak("Please wait opening media player for you")
            os.system("wmplayer")

        elif("visual studio code" in operation) or ("vs code" in operation) or ("vs" in operation):
            pyttsx3.speak("Please wait opening vs code for you")
            os.system("code")

        elif("Git Hub" in operation) or ("github" in operation):
            pyttsx3.speak("Please wait opening github for you")
            os.system("GitHubDesktop")

        elif("microsoft edge" in operation) or ("edge" in operation) or ("microsoft browser" in operation):
            pyttsx3.speak("Please wait opening microsoft edge for you")
            os.system("msedge")

        elif("team viewer" in operation) or ("teamviewer" in operation):
            pyttsx3.speak("Please wait opening team viewer for you")
            os.system("TeamViewer")

        elif("microsoft paint" in operation) or ("ms paint" in operation) or ("paint" in operation):
            pyttsx3.speak("Please wait opening microsoft edge for you")
            os.system("msedge")

        elif("website" in operation) or ("link" in operation) or ("page" in operation) or ("chrome website" in operation) or ("chrome page" in operation):
            website=input("Enter the link for the website or page you want to open: \n")
            pyttsx3.speak("Please wait opening {} for you".format(website))
            os.system("chrome {}".format("website"))
        
        elif("microsoft word" in operation) or ("ms word" in operation) or ("word" in operation):
            pyttsx3.speak("Please wait opening microsoft word for you")
            os.system("winword")

        elif("exit" in operation) or ("return" in operation) or ("close" in operation) or ("end" in operation):
            pyttsx3.speak("Thank You! Hope to see you again")
            break

        else:
            print("Error: Try some other operation available from the list!")
            pyttsx3.speak("Please enter some other operation")
            print()

def main():

    import os
    import pyttsx3
    print()
    pyttsx3.speak("Welcome to the automation world")
    print("         This Is A Menu Drive Program !         ")
    print()
    print("Available Operations:")
    print("1) Open Chrome \n2) Open Notepad \n3) Open Media Player \n4) Open VS Code \n5) Open Git Hub \n6) Open any Website")
    print("7) Open Microsoft Edge \n8) Open Team Viewer(TeamViewer) \n9) Open MS Paint(mspaint) \n10) Open MS Word ")
    print()
    print("You can type a statement and interact!")
    print()
    
    system_operations()

if __name__ == "__main__":
    main()
