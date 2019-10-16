import turtle
import numpy as np
import random as rd

M = 1000
p = 0.3
v0 = 0
N = 10
dt = 1
vmax = 50
tmax = 100
t = 0

tr = []  #list mobil
v = [] #list kecepatan masing masing mobil tiap detik
v = [v0]*N #inisiasi v0 tiap mobil = 0 
vCar = [] #kepadatan mobil pada selang x 80 & x90
tCar = [] #waktu dr tiap untuk kemabali posisi semula
tCar = [v0]*N
nPutaran = [] #banyak mobil melewati koordinat awal
nPutaran = [v0]*N
clr = ['red','green','blue','black','yellow','orange','magenta','purple','pink','aquamarine']
koordinat = [] #koordinat awal mobil

#membuat koordinat
for a in range(10):
    koordinat.append(rd.randint(-500,500))
koordinat.sort()

turtle.Screen().setup(1000,300,0,0)
turtle.Screen().delay(1)

#pengecekan jarak antar mobil
def jarakMobil() :
    if (k == N-1):
        if(tr[k].xcor() > tr[0].xcor()):
           d = abs(M - (tr[k].xcor() - tr[0].xcor()))
           
        else :
           d = abs(tr[0].xcor() - tr[k].xcor())
           
    else :
        if (tr[k].xcor() < tr[k+1].xcor()) :
            d = abs(tr[k+1].xcor() - tr[k].xcor())
           
        else:
            d = abs(M - (tr[k+1].xcor() - tr[k].xcor()))
            
    return d

#pertambahan kecepatan
def updateV():
    v[k] = min(v[k]+10, vmax)
    d = jarakMobil()
    v[k] = min(v[k], d-10)
    x = np.random.uniform(0,1)
    if (x >= p):
        v[k] = max(0,v[k]-10)
    return v[k]

#membuat mobil
for j in range(10) :
    tr.append(turtle.Turtle())

#set koordinat mobil
for i in range (10) :
    tr[i].color(clr[i])
    tr[i].penup()
    tr[i].goto(koordinat[i],0)
    
#running
while t <= tmax:
    x = 0
    for k in range(N):
            
        tr[k].forward(updateV())
        tr[k].speed(10)
        if (tr[k].xcor() >= 500):
            tr[k].ht()
            tr[k].goto(-500,0)
            tr[k].st()
            
        #menghitung waktu mobil melewati posisi semula
        if (koordinat[k] >= tr[k].xcor()):
            if (0 <= koordinat[k] - tr[k].xcor() <=50):
                tCar[k] += t
                nPutaran[k] += 1
        #menghitung pada selang x80 dan x 90
        if (((M/2) - 200) <= tr[k].xcor() <= ((M/2)-100)):
            x+=1
    t+=1
    vCar.append(x)
print("==============================")
print("Kepadatan setiap pada selang x80 dan x 90 : ")
print(vCar)
print(" ")
print("==============================")  
for x in range(10):
    print('Rata - rata waktu mobil ',x,' adalah ',tCar[i]/nPutaran[x])
