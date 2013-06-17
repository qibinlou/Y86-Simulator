import Y86API

word=[]
memory={}
val={}

yo=file("asumr.yo")

while True:
    line=yo.readline()
    if    line=="":
        break
    word.append(line)

val,memory=Y86API.executeY86(0,0,word)

while val["end"]==False:
    val,memory=Y86API.executeY86(val,memory)

