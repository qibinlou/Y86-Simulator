import Y86API

word=[]
memory={}
val={}

yo=file("input.yo")

while True:
    line=yo.readline()
    if    line=="":
        break
    word.append(line)

Y86API.initY86(word)

Y86API.exeY86()

val,memory = Y86API.getY86()

while val["end"]==False:
    Y86API.setY86(val,memory)
    Y86API.exeY86()
    val,memory=Y86API.getY86()
    # print "fuck",len(val),len(memory)
    print("@@@@@@@@@@@@@@@@@@@@@@@@")
