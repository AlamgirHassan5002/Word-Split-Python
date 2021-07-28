def WordSplit(strArr):
    size=len(strArr)
    word=strArr[0]
    pattern=strArr[1]
    words1=[]
    words2=[]

    patternlist=pattern.split(",")
    length=0
    for i in range(0,len(word)-1):
        for j in range(0,len(patternlist)):
            pattern1=patternlist[j]
            length=0
            if(word[i]==pattern1[0]):
                for k in range(0,len(pattern1)):
                    z=i+k
                    if(z<=len(word)):
                        if(word[z]==pattern1[k]):
                            length+=1
                        else:
                            break
                    else:
                        break
                if(length==len(pattern1)):
                    words1.append(pattern1)
    check=False
    for i in range(0,len(words1)-1):
        for j in range(i+1,len(words1)):
            x=words1[i]
            x+=words1[j]
            if(len(x)==len(word)):
                words2.append(words1[i])
                words2.append(words1[j])
                check=True
                break
    if(check==True):
        for i in range(0,len(words2)):
            for j in range(0,len(words2)):
                if((words2[i]+words2[j])==word):
                    return [words2[i],words2[j]]
    else:
        return []
print(WordSplit(["baseball","a,all,b,ball,bas,base,cat,code,d,e,quit,z"]))
print(WordSplit(["abcgefd","a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]))
print(WordSplit(["hamza","h,z,laiba,haz,ham,za,dog,e,efd,zzzz"]))
print(WordSplit(["molvihamza","a,ab,abc,mercedes,mol,molvi,ha,hamza,efd,zzzz"]))


x="Mercedes"
print(x[0:4])
print(x[4:len(x)])