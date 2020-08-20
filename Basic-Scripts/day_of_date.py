#Function to calculate day of the week
def dayofweek(
        d, m, y):
    
    t = [
        0, 3, 2,
        5, 0, 3,
        5, 1, 4,
        6, 2, 4
        ]
    
    y = y - (m < 3)
    k=(
        y
        + int(y / 4)
        - int(y / 100)
        + int(y / 400)
        + t[m - 1]
        + d
       ) % 7
    
    switcher={
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday',
        7:'Sunday'
        }
    
    return switcher.get(k,'Invalid')

  
#Driver Program
if __name__=='__main__':
    day=dayofweek(20,8,2020)
    print(day)
