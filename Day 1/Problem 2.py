#Set up some arrays and overall tags
inp = []
numbers = []
outputs = []
total = 0

def calcFuel(mass):
    temp = mass//3
    temp = temp-2
    if temp <= 0:
        return 0
    else:
        return temp + calcFuel(temp)

#Get first input and append it to the list
temp = input("")
inp.append(temp)

#While we have input, get more input and append it to the list.
while temp != "":
    temp = input("")

    #If the input is not nothing append it to the inputs list
    if temp != "":
        inp.append(temp)

#Cycle all inputs and safely convert them to ints
for i in inp:
    try:
        temp = int(i)
        numbers.append(temp)
    except:
        print("Non number " + i)

#On all numbers, run the calculation, and append it to the outputs
for i in numbers:
    temp = calcFuel(i)
    outputs.append(temp)

#Add all of the numbers up
for i in outputs:
    total =  total+i

#Print the total output
print(total)
