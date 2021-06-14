def cd(newPath, oldPath):
    newP=newPath.split("/")
    oldP=oldPath.split("/")

    lenCount=0;
    for i in newP:
        if i=="..":
            lenCount+=1
    oldLen=len(oldP)
    strout=""
    for i in range(oldLen-lenCount):
        strout=strout+oldP[i]+"/"
    newLen=len(newP)
    for i in range(newLen):
        if newP[i]!="..":
            strout=strout+newP[i]+"/"
    res = strout[0:len(strout)-1]
    return res
oldPath = "/a/b/c/d"
newPath = "../xs"
print(cd(newPath, oldPath))
