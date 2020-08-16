def dayofweek(d, m, y): 
    t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ] 
    y -= m < 3
    k=( y + int(y / 4) - int(y / 100) + int(y / 400) + t[m - 1] + d) % 7
    if k==1:
        d='Monday'
    elif k==2:
        d='Tuesday'
    elif k==3:
        d='Wednesday'
    elif k==4:
        d='Thursday'
    elif k==5:
        d='Friday'
    elif k==6:
        d='Saturday'
    else:
        d='Sunday'
    return d

  

#day = dayofweek(24, 4, 2020) 
#print(day)
