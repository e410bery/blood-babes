import constants as c
import accumulation as A

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
    file.write(','.join(str(a) for a in A.acc)) #<- change A.acc to whatever u need to graph.
    file.write('\n')


