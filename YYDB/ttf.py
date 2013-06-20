# coding=UTF-8
import Y86API
import data

word=[]
memory={}
val={}

list_val=[]
list_memory=[]

def arc(s):
	if(s=="X"):
		return ""
	if(len(s)!=8):
		return s
	return s[6]+s[7]+s[4]+s[5]+s[2]+s[3]+s[0]+s[1]

def TF(s):
	if(len(s)==8):
		return "true"
	else:
		return "false"

def which(s):
	if(len(s)==8):
		return s
	else:
		return ""

def output(txt):
	txt.write("Cycle_%d\n" %(data.total_cycle-1))
	txt.write("--------------------\n")
	txt.write("FETCH:\n")
	txt.write("\tF_predPC 	= 0x%s\n\n" %which(data.pc))

	txt.write("DECODE:\n")
	txt.write("\tD_icode  	= 0x%s\n" %data.D_icode)
	txt.write("\tD_ifun   	= 0x%s\n" %data.D_ifunc)
	txt.write("\tD_rA	 	= 0x%s\n" %data.rA)
	txt.write("\tD_rB	 	= 0x%s\n" %data.rB)
	txt.write("\tD_valC   	= 0x%s\n" %arc(data.D_valC))
	txt.write("\tD_valP   	= 0x%s\n\n" %arc(data.D_valP))

	txt.write("EXECUTE:\n")
	txt.write("\tE_icode  	= 0x%s\n" %data.E_icode)
	txt.write("\tE_ifun   	= 0x%s\n" %data.E_ifunc)
	txt.write("\tE_valC   	= 0x%s\n" %arc(data.E_valC))
	txt.write("\tE_valA   	= 0x%s\n" %arc(data.E_valA))
	txt.write("\tE_valB   	= 0x%s\n" %arc(data.E_valB))
	txt.write("\tE_dstE   	= 0x%s\n" %arc(data.E_dstE))
	txt.write("\tE_dstM   	= 0x%s\n" %arc(data.E_dstM))
	txt.write("\tE_srcA   	= 0x%s\n" %data.srcA)
	txt.write("\tE_srcB   	= 0x%s\n\n" %data.srcB)

	txt.write("MEMORY:\n")
	txt.write("\tM_icode  	= 0x%s\n" %data.M_icode)
	txt.write("\tM_Bch      \t= %s\n" %TF(data.bch))
	txt.write("\tM_valE   	= 0x%s\n" %arc(data.M_valE))
	txt.write("\tM_valA   	= 0x%s\n" %arc(data.M_valM))
	txt.write("\tM_dstE   	= 0x%s\n" %arc(data.M_dstE))
	txt.write("\tM_dstM   	= 0x%s\n\n" %arc(data.M_dstM))

	txt.write("WRITE BACK:\n")
	txt.write("\tW_icode  	= 0x%s\n" %data.W_icode)
	txt.write("\tW_valE   	= 0x%s\n" %arc(data.W_valE))
	txt.write("\tW_valM   	= 0x%s\n" %arc(data.W_valM))
	txt.write("\tW_dstE   	= 0x%s\n" %arc(data.W_dstE))
	txt.write("\tW_dstM   	= 0x%s\n\n" %arc(data.W_dstM))

print("Which File do you want to import? Enter the Name:")

yo=file((str)(raw_input()))

while True:
	line=yo.readline()
	if	line=="":
		break
	word.append(line)

Y86API.initY86(word)
val,memory=Y86API.getY86()

out=file("output.txt","w+")
data.show()
output(out)

list_val.append(dict(val))
list_memory.append(dict(memory))

while val["end"]==False:
	val,memory=Y86API.executeY86(val,memory)
	data.show()
	output(out)
	print("Next?[\"n\" for exit;\"b\" for back]")
	list_val.append(dict(val))
	list_memory.append(dict(memory))
		
yo.close()
out.close()
	
		
