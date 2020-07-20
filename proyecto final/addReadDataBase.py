loginsRegister=[]
pointsFile = "/home/bryan/Desktop/entrybon/dataBase.txt" #

def cleanDataBase():
    openFile= open(pointsFile, 'w')
    openFile.write("")

def getDataBase(array):
    openFile= open(pointsFile, 'r')
    n=0
    word=""
    for linea in openFile:
        i=0
        while linea[i]!= "\n":
            word=word+linea[i]
            i=i+1
        array.append(word)
        word=""
    openFile.close()

def addToDataBase(array, newName):
    openFile= open(pointsFile, 'a')
    openFile.write(newName+"\n")
    loginsRegister.append(newName)
    openFile.close()
