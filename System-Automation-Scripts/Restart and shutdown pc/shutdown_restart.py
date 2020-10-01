# Imprort OS library
import os

# User input
option = int(input("""
Enter input
[1] Shutdown
[2] Restart
[3] Quit
"""))

# Function for shutting down pc
def shutdown():
    os.system('shutdown -s')

# Function for restarting pc
def restart():
    os.system("shutdown /r /t 1") 

if(option == 1):
    shutdown()
elif(option == 2):
    restart() 

else:
    exit()