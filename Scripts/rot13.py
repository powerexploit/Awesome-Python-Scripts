def modulusX(x):
    return (((x % 26)+26)%26)

def rotateChr(huruf, rotx):
    rotx = modulusX(rotx)
    hasil = huruf
    
    if (65 <= huruf and huruf <= 90):
        hasil = huruf + rotx
        if (hasil > 90):
            hasil = 64 + (rotx - (90-huruf))
            
    elif (97 <= huruf and huruf <= 122):
        hasil = huruf + rotx
        if (hasil > 122):
            hasil = 96 + (rotx - (122 - huruf))
    
    return hasil

kata = input("Masukan kata yang akan di rotasi : ")
rotx = int(input("Masukan banyak rotasi : "))

idx = 0
chrKata = []
for i in kata:
    chrKata.append(ord(i))
    idx += 1
    
index=0
result = []
while index < len(chrKata):
    result.append(rotateChr(chrKata[index],rotx))
    print(chr(result[index]), end="")
    index += 1
