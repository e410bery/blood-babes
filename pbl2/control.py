import constants as c
import BrainA as A
import BrainB as B
import accumulation as Acc

#change case in constants.
#this will find accumlation values and save them onto the output.txt file to be parsed and graphed.

'''
STEPS TO MAKE NEW GRAPH WITH MULTIPLE CASES:
1. clear contents of output.txt (literally j delete everything)
2. Change the code below to what list/array you need to graph (import any necesary files)
3. Repeat following for each desired case:
    -Change case in constants, save
    -run control.py
    -optional check to make sure the output is saved in output.txt
4. After running control for all cases, open graph.py, change the name of file at the bottom then run it!

'''
with open("output.txt", "a") as file:
    file.write(str(c.case) + ":")
    file.write(','.join(str(a) for a in Acc.acc)) #<- change last thing to whatever u need to graph.
    file.write('\n')

print("case", c.case, "completed")
'''
with open("output.txt", "a") as file:
    # Save Ser
    file.write(f"{c.case}:")
    file.write(','.join(str(a) for a in B.Ser))
    file.write('\n')
    
    # Save DegSer
    file.write(f"{c.case}_DegSer:")
    file.write(','.join(str(a) for a in B.Deg_Ser))
    file.write('\n')

'''