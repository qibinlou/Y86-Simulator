import Y86API

word=[]
memory={}
val={}

print("Which File do you want to import? Enter the Name:")

yo=file((str)(raw_input()))

while True:
    line=yo.readline()
    if    line=="":
        break
    word.append(line)

print("Confirm it?[\"n\" for not]")
s=(str)(raw_input())
if(s=="n") or (s=="N"):
    exit(0)

val,memory=Y86API.executeY86(0,0,word)

print("Next?[\"n\" for not]")
s=(str)(raw_input())
if(s=="n") or (s=="N"):
    exit(0)

while val["end"]==False:
    val,memory=Y86API.executeY86(val,memory)
    print("Next?[\"n\" for not]")
    s=(str)(raw_input())
    if(s=="n") or (s=="N"):
        exit(0)
