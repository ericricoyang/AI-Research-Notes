import random
import array as arr
while 1:
    x = random.randint(1234,9876)
    x1= (x//1000)
    x2= (x//100) - 10*x1
    x3= (x//10)  - 10*x2 -100*x1
    x4= (x//1)   - 10*x3 -100*x2 - 1000*x1
    xarray = (x1, x2, x3, x4)
    
    times=0   
    if x1 != x2:
        if x1 != x3:
            if x1 != x4:
                if x2 != x3:
                    if x2 != x4:
                        if x3 != x4:
                            break
                        else:                       
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        continue
    
    
while 1:
   x1= (x//1000)
   x2= (x//100) - 10*x1
   x3= (x//10)  - 10*x2 -100*x1
   x4= (x//1)   - 10*x3 -100*x2 - 1000*x1
   xarray = (x1, x2, x3, x4)
   
   y = int(input("Please guess a number between 0-9999: "))
   y1= (y//1000)
   y2= (y//100) - 10*y1
   y3= (y//10)  - 10*y2 - 100*y1
   y4= (y//1)   - 10*y3 - 100*y2 - 1000*y1
   yarray =(y1,y2,y3,y4)
   print("yarray=",yarray)

   if (xarray[0] == yarray[0]) & (xarray[1] == yarray[1]) & (xarray[2] == yarray[2]) & (xarray[3] == yarray[3]):
        print("You're correct!")
        times = times + 1 
        print("times=", times)
        break
      
   else:
        numA=0
        numB=0
        times = times + 1
        for i in range(4):
            if xarray[i] == yarray[i]:
                numA=numA+1
        for i in range(4):
            for j in range(4):
                if i == j:
                    pass
                else:
                    if xarray[i] == yarray[j]:
                        numB = numB + 1
              
        print(numA,"A",numB,"B","You have guessed",times,"次")
      
   continue

print("Game over")
