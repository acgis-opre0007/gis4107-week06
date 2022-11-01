from ast import Break


txt = "075 45 03 W 45 23 05 N\n"

x = str(txt.splitlines()[0])
working_elements = x.split(' ')
long = 0

for i in range(0,len(working_elements)):
    if i == 2 or i == 7:
        directionBool = working_elements[i].isalpha()
        print(directionBool)

        if directionBool == False:
            break

for i in range(0,3):
    long = long + int(working_elements[i])/(60**i)

#print(f'{str(long)')