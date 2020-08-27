#imports math so math functions work
from math import *
#two implemented math functions so far and function selection
print("Programmed: quadratic, pythagorean")
selectedFunction=int(input("Select program (number)"))
#checks if the function exists or not and runs the program accordingly
if(selectedFunction==1):
    valuea=int(input("Input value A"))
    valueb=int(input("Input value B"))
    valuec=int(input("Input value C"))
    #tries out calculating positive/negative side of quadratic formula because sometimes there is a domain error because... quadratic formula
    try:outputValue1=(-valueb+sqrt(pow(valueb,2)-(4*valuea*valuec)))/(2*valuea)
    except: pass
    try:outputValue2=(-valueb-sqrt(pow(valueb,2)-(4*valuea*valuec)))/(2*valuea)
    except: pass
    #attempts to print out positive/negative quadratic result
    try:print("Returned value (add)=",outputValue1)
    except: pass
    try:print("Returned value (minus)=",outputValue2)
    except: pass
#checks if selectedFunction is 2 or not and executes pythagorean theorem accordingly
elif(selectedFunction==2):
    value1=int(input("Input side value 1 (Raw value not squared)"))
    value2=int(input("Input side value 2 (Raw value not squared)"))
    outputValue= (sqrt(pow(value1,2)+pow(value2,2)))
    print(outputValue)
#if selectedFunction does not exist on list then prints out that it dosent exist
else:
    print("Selected function does not exist")