# Sending automated message through the python script  
import keyboard
i =0
while(i<11):
    i+=1
    keyboard.wait('enter')
    keyboard.write("Sending message {} times ".format(i))
    keyboard.send('enter')
