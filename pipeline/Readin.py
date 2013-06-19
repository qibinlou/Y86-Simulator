import data
linelist=[]
    
def readin():
    global linelist
    for i in range(0,len(linelist)):
        line=linelist[i]
        if    line=="":
            break
        p1=line.find(":")
        if(p1==-1):
            continue
        if(line[p1+2]==" "):
            continue
        s=line[p1+2:]
        p2=s.find(" ")
        s=s[:p2]
        data.LineNum.append("00000"+line[p1-3:p1])
        data.RealNum.append(i)
        data.Text.append(s)

    i=0
    while i<len(data.LineNum):
        #print (data.LineNum[i]+":"+data.Text[i])
        data.MemoryCopy(data.LineNum[i],data.Text[i])
        i+=1



