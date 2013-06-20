#coding=UTF-8
import Y86API
import data
import assembler

word=[]
memory={}
val={}

list_val=[]
list_memory=[]

print("输入YO文件名".decode('UTF-8'))

fname=(str)(raw_input())

if(fname[-1]=="s"):
	assembler.ass(fname)
	fname=fname[:-1]+"o"

yo=file(fname)

while True:
	line=yo.readline()
	if	line=="":
		break
	word.append(line)

print("确认吗，n表示放弃".decode('UTF-8'))
s=(str)(raw_input())
if(s=="n") or (s=="N"):
	exit(0)

Y86API.initY86(word)
val,memory=Y86API.getY86()
data.show()

list_val.append(dict(val))
list_memory.append(dict(memory))
show=True
while val["end"]==False:
	val,memory=Y86API.executeY86(val,memory)
	if show:
		data.show()
	show=True
	if(len(list_val)==1):
		print("这是初始状态".decode('UTF-8'))
	print("Next?[x:退出][s:多步][b:退一次][m:内存查看][其他:继续]".decode('UTF-8'))
	s=(str)(raw_input())
	if(s=="x") or (s=="X"):
		exit(0)
	elif(s=="m") or	(s=="M"):
		for i in range(0,2048):
			s=str(i)
			if s in data.Memory:
				print("[%s]\t[%s]" %(str(hex(i)),data.Memory[s]))
		val=list_val[-1]
		memory=list_memory[-1]
		show=False
	elif(s=="b") or (s=="B"):
		if(len(list_val)<2):
			val=list_val[-1]
			memory=list_memory[-1]
		else:
			del list_val[len(list_val)-1]
			del list_memory[len(list_memory)-1]
			val=dict(list_val[len(list_val)-1])
			memory=dict(list_memory[len(list_memory)-1])
	elif(s=="s") or (s=="S"):
		print("用正负整数表示你想要前进后退的步数".decode('UTF-8'))
		k=(int)(raw_input())
		if(k>0):
			print(k)
			val=list_val[len(list_val)-1]
			memory=list_memory[len(list_memory)-1]
			while ((k>0) and (val["end"]==False)):
				val,memory=Y86API.executeY86(val,memory)
				list_val.append(dict(val))
				list_memory.append(dict(memory))
				k-=1		
		else:
			k=-k
			for i in range(0,k):
				if len(list_val)<2:
					continue
				else:
					del list_val[len(list_val)-1]
					del list_memory[len(list_memory)-1]

		val=dict(list_val[len(list_val)-1])
		memory=dict(list_memory[len(list_memory)-1])
	else:
		list_val.append(dict(val))
		list_memory.append(dict(memory))
		
		
	
		
