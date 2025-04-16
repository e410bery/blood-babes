import constants as c
import accumulation as A

#change case in constants.
#this will find accumlation values and save them onto the output.txt file to be parsed and graphed.

with open("output.txt", "a") as file:
    file.write(str(c.case) + ":")
    file.write(','.join(str(a) for a in A.acc))
    file.write('\n')


