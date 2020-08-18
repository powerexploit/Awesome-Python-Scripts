##Connecting Wifi Automatically
-We can make Wifi Connect automatically by python
-We can make it by running commands on command line.

-**netsh wlan show profiles** 

-This command shows the saved networks in our pc

-**netsh wlan show networks**

-This command shows the available networks in our pc

-But how can we run this using python ???

-Yess..! we can run  commands using python by using os module

####os.popen()

-This will run commands using python

####os.popen().read()

-This will return the output after excuting the line

-For example 
```
 response=os.popen("netsh wlan disconnect").read()

 ```
 -This will connect the present network and return the response after Disconnection

 ```

resp = os.popen('netsh wlan connect name=' + '"' + preferred_ssid + '"').read()

```

-This line will connect to our prefered network