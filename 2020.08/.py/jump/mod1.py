from random import randint
numTosses = 100


fileOut = open("data.dat",'w') 

for index in range(numTosses): 
 fileOut.write(str(index) + ","
       + str(randint(0,1))
       + '\n') 

fileOut.close() 


fileIn = open("data.dat",'r') 

heads = list() 
tails = list() 

for line in fileIn.readlines(): 

 fields = line.split(',') 

 if fields[1].strip() == '1': 
  heads.append(1) 
 else: 
  tails.append(1)  

print("Number of heads is: " + str(len(heads))) 
print("Number of tails is: " + str(len(tails))) 

fileIn.close()  