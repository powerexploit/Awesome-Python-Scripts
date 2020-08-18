import pyshorteners
link = input("Enter the link: ")
shortener = pyshorteners.Shortener
x=shortener.tinyurl.short(link)
print(x)