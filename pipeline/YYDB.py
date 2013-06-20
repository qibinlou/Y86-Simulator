import Y86API
import data

word=[]
memory={}
val={}

list_val=[]
list_memory=[]

print("Which File do you want to import? Enter the Name:")

yo=file((str)(raw_input()))

while True:
	line=yo.readline()
	if	line=="":
		break
	word.append(line)

print("Confirm it?[\"n\" for not]")
s=(str)(raw_input())
if(s=="n") or (s=="N"):
	exit(0)

Y86API.initY86(word)
val,memory=Y86API.getY86()
data.show()

list_val.append(dict(val))
list_memory.append(dict(memory))

print("Next?[\"n\" for exit]")
s=(str)(raw_input())
if(s=="n") or (s=="N"):
	exit(0)

while val["end"]==False:
	val,memory=Y86API.executeY86(val,memory)
	data.show()
	print("Next?[\"n\" for exit;\"b\" for back]")
	s=(str)(raw_input())
	if(s=="n") or (s=="N"):
		exit(0)
	if(s=="b") or (s=="B"):
		if(len(list_val)<2):
			print("---------------------Sorry!!! This is the first phase")
			list_val.append(dict(val))
			list_memory.append(dict(memory))
		else:
			del list_val[len(list_val)-1]
			del list_memory[len(list_memory)-1]
			val=dict(list_val[len(list_val)-1])
			memory=dict(list_memory[len(list_memory)-1])
	else:
		list_val.append(dict(val))
		list_memory.append(dict(memory))
		
		
	
		
