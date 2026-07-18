from covid import  Covid #importing coid python module
import matplotlib.pyplot as plt #for displaying graph of cases



covid = Covid()
nme=input("enter country name: ")
data=covid.get_status_by_country_name(nme)

# print(data)
'''<----Creating graph for main details---->'''
remove=['id', 'country', 'latitude', 'longitude', 'last_update']
for i in remove:
    data.pop(i)
all=data.pop('confirmed')

id=list(data.keys())
value=[str(i) for i in data.values()]
plt.pie(value,labels=id,colors=['r','y','g','b'],autopct="%1.1f%%")

plt.title("COUNTRY: "+nme.upper()+"\n TOTAL CASES : "+str(all))
plt.legend()
plt.show()