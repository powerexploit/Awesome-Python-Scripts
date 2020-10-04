import numpy as np
def generatetable(text,k=4):
  T={}
  for i in range(len(text)-k):
    X=text[i:i+k]
    Y=text[i+k]
    #print(X,Y)
    if T.get(X) is None:
      T[X]={}
      T[X][Y]=1
    else:
      if T[X].get(Y) is None:
        T[X][Y]=1
      else:
        T[X][Y] +=1
  return T

def convertFreqIntoProb(T):     
    for kx in T.keys():
        s = float(sum(T[kx].values()))
        for k in T[kx].keys():
            T[kx][k] = T[kx][k]/s
                
    return T


def load_text(filename):
    with open(filename,encoding='utf8') as f:
        return f.read().lower()
    

def train(text,k=4):
  T = generatetable(text,k)
  T = convertFreqIntoProb(T)
    
  return T


def sample_next(ctx,T,k):
    ctx = ctx[-k:]
    if T.get(ctx) is None:
        return " "
    possible_Chars = list(T[ctx].keys())
    possible_values = list(T[ctx].values())
    
    return np.random.choice(possible_Chars,p=possible_values)


def generateText(starting_sent,k=4,maxLen=1000):
    
    sentence = starting_sent
    ctx = starting_sent[-k:]
    
    for ix in range(maxLen):
        next_prediction = sample_next(ctx,model,k)
        sentence += next_prediction
        ctx = sentence[-k:]
    return sentence


files="all-of-me.txt"
data= load_text(files)
model=train(data)
x = input("Enter the beginning word: ")
text = generateText(x,k=4,maxLen=2000)
print(text)
