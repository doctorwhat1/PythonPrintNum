# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def countHash(line, module=10):
    total = 0
    for i in line:
        #myord=(ord(i)-ord("a"))
        total = (26*total + (ord(i)-ord("a")) ) % module
    return total
def main(module,pattern,stream):

    matches=[]
    spurious=[]

    patternHash=countHash(pattern)

    #print(countHash('uv'))

    for i in range(0,1+len(stream)-len(pattern)):
        kusok=stream[i:i+len(pattern)]
        if (patternHash==countHash(kusok)):
            #Collision. Spurious?

            if (kusok==pattern):
                #real
                matches.append(i)
            else:
                #sus
                spurious.append(i)

   # print("Matches: ",end="")

    print(str(matches))
    return(str(matches))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
