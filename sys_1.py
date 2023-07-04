import sys


#sys.argv 

FirstNumber  = int(sys.argv[1])
SecondNumber = int(sys.argv[2])

if sys.argv[3] == "m" :
    multiple = FirstNumber * SecondNumber 
    print("multiple is {}".format(multiple))

elif sys.argv[3] == "p" :
     multiple = FirstNumber ** SecondNumber 
     print("power is {}".format(multiple))

#sys.exit()

#sys.maxsize
x1 = range(sys.maxsize)
x2 = range(sys.maxsize +1)
print(len(x1))
#print(len(x2))


#sys.float_info
print(sys.float_info)
print("Min" , sys.float_info.min)
print("Max", sys.float_info.max)