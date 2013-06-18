global Text
Text=[]
global LineNum
LineNum=[]
global halt
halt=False
global end
end=False
global ret
ret=False
global stall
stall=False

global total_cycle
total_cycle=0

global valid_cycle
valid_cycle=0

def setstall():
    global stall
    stall=True

def isstall():
    return stall

def start():
    global stall
    stall=False

def setend():
    global end
    end=True

def isend():
    return end

global F_icode
F_icode=""
global pc
pc="00000000"
global D_index
D_index="X"
global D_icode
D_icode="0"
global D_ifunc
D_ifunc=""
global rA
rA=""
global rB
rB=""
global D_valC
D_valC=""
global D_valP
D_valP=""
global E_index
E_index="X"
global E_icode
E_icode="0"
global E_ifunc
E_ifunc=""
global E_valC
E_valC=""
global E_valA
E_valA=""
global E_valB
E_valB=""
global E_dstE
E_dstE=""
global E_dstM
E_dstM=""
global M_index
M_index="X"
global M_icode
M_icode="0"
global bch
bch=""
global M_valE
M_valE=""
global M_valM
M_valM=""
global M_dstE
M_dstE=""
global M_dstM
M_dstM=""
global srcA
srcA=""
global srcB
srcB=""
global W_index
W_index="X"
global W_icode
W_icode="0"
global W_valE
W_valE=""
global W_valM
W_valM=""
global W_dstE
W_dstE=""
global W_dstM
W_dstM=""
global ZF
ZF=False
global SF
SF=False
global OF
OF=False
global CF
CF=False

def arc(s):
    return s[6]+s[7]+s[4]+s[5]+s[2]+s[3]+s[0]+s[1]

def get(s):
    if(s[0]=="a"):
        return 10
    elif(s[0]=="b"):
        return 11
    elif(s[0]=="c"):
        return 12
    elif(s[0]=="d"):
        return 13
    elif(s[0]=="e"):
        return 14
    elif(s[0]=="f"):
        return 15
    else:
        return ord(s[0])-ord("0")

def num(s):
    ans=0
    ss=s[0:2]
    temp=get(ss[0])
    temp=temp*16+get(ss[1])
    ans+=temp
    ss=s[2:4]
    temp=get(ss[0])
    temp=temp*16+get(ss[1])
    ans+=temp*256
    ss=s[4:6]
    temp=get(ss[0])
    temp=temp*16+get(ss[1])
    ans+=temp*256*256
    ss=s[6:8]
    temp=get(ss[0])
    temp=temp*16+get(ss[1])
    ans+=temp*256*256*256
    return ans

def intread(temp):
    if(temp=="total_cycle"):
        return total_cycle
    if(temp=="valid_cycle"):
        return valid_cycle

def intwrite(temp,val):
    if(temp=="total_cycle"):
        global total_cycle
        total_cycle=val
    elif(temp=="valid_cycle"):
        global valid_cycle
        valid_cycle=val

def read(temp):
    if(temp=="F_icode"):
        return F_icode
    elif(temp=="pc"):
        return pc
    elif(temp=="D_index"):
        return D_index
    elif(temp=="D_icode"):
        return D_icode
    elif(temp=="D_ifunc"):
        return D_ifunc
    elif(temp=="rA"):
        return rA
    elif(temp=="rB"):
        return rB
    elif(temp=="D_valC"):
        return D_valC
    elif(temp=="D_valP"):
        return D_valP
    elif(temp=="E_index"):
        return E_index
    elif(temp=="E_icode"):
        return E_icode
    elif(temp=="E_ifunc"):
        return E_ifunc
    elif(temp=="E_valC"):
        return E_valC
    elif(temp=="E_valA"):
        return E_valA
    elif(temp=="E_valB"):
        return E_valB
    elif(temp=="E_dstE"):
        return E_dstE
    elif(temp=="E_dstM"):
        return E_dstM
    elif(temp=="M_index"):
        return M_index
    elif(temp=="M_icode"):
        return M_icode
    elif(temp=="bch"):
        return bch
    elif(temp=="M_valE"):
        return M_valE
    elif(temp=="M_valM"):
        return M_valM
    elif(temp=="M_dstE"):
        return M_dstE
    elif(temp=="M_dstM"):
        return M_dstM
    elif(temp=="srcA"):
        return srcA
    elif(temp=="srcB"):
        return srcB
    elif(temp=="W_index"):
        return W_index
    elif(temp=="W_icode"):
        return W_icode
    elif(temp=="W_valE"):
        return W_valE
    elif(temp=="W_valM"):
        return W_valM
    elif(temp=="W_dstE"):
        return W_dstE
    elif(temp=="W_dstM"):
        return W_dstM
    elif(temp=="CF"):
        return CF
    elif(temp=="OF"):
        return OF
    elif(temp=="ZF"):
        return ZF
    elif(temp=="SF"):
        return SF
    elif(temp=="end"):
        return end
    elif(temp=="stall"):
        return stall
        

def write(temp,val):
    if(temp=="F_icode"):
        global F_icode
        F_icode=val
    elif(temp=="pc"):
        global pc
        pc=val
    elif(temp=="D_index"):
        global D_index
        D_index=val
    elif(temp=="D_icode"):
        global D_icode
        D_icode=val
    elif(temp=="D_ifunc"):
        global D_ifunc
        D_ifunc=val
    elif(temp=="rA"):
        global rA
        rA=val
    elif(temp=="rB"):
        global rB
        rB=val
    elif(temp=="D_valC"):
        global D_valC        
        D_valC=val
    elif(temp=="D_valP"):
        global D_valP
        D_valP=val
    elif(temp=="E_index"):
        global E_index
        E_index=val
    elif(temp=="E_icode"):
        global E_icode
        E_icode=val
    elif(temp=="E_ifunc"):
        global E_ifunc
        E_ifunc=val
    elif(temp=="E_valC"):
        global E_valC
        E_valC=val
    elif(temp=="E_valA"):
        global E_valA
        E_valA=val
    elif(temp=="E_valB"):
        global E_valB
        E_valB=val
    elif(temp=="E_dstE"):
        global E_dstE
        E_dstE=val
    elif(temp=="E_dstM"):
        global E_dstM
        E_dstM=val
    elif(temp=="M_index"):
        global M_index
        M_index=val
    elif(temp=="M_icode"):
        global M_icode
        M_icode=val
    elif(temp=="bch"):
        global bch
        bch=val
    elif(temp=="M_valE"):
        global M_valE
        M_valE=val
    elif(temp=="M_valM"):
        global M_valM
        M_valM=val
    elif(temp=="M_dstE"):
        global M_dstE
        M_dstE=val
    elif(temp=="M_dstM"):
        global M_dstM
        M_dstM=val
    elif(temp=="srcA"):
        global srcA
        srcA=val
    elif(temp=="srcB"):
        global srcB
        srcB=val
    elif(temp=="W_index"):
        global W_index
        W_index=val
    elif(temp=="W_icode"):
        global W_icode
        W_icode=val
    elif(temp=="W_valE"):
        global W_valE
        W_valE=val
    elif(temp=="W_valM"):
        global W_valM
        W_valM=val
    elif(temp=="W_dstE"):
        global W_dstE
        W_dstE=val
    elif(temp=="W_dstM"):
        global W_dstM
        W_dstM=val
    elif(temp=="CF"):
        global CF
        CF=val
    elif(temp=="OF"):
        global OF
        OF=val
    elif(temp=="ZF"):
        global ZF
        ZF=val
    elif(temp=="SF"):
        global SF
        SF=val
    elif(temp=="end"):
        global end
        end=val
    elif(temp=="stall"):
        global stall
        stall=val
#reg---------------------------------------------
global eax
eax="00000000"
global ecx
ecx="00000000"
global edx
edx="00000000"
global ebx
ebx="00000000"
global esp
esp="00000000"
global ebp
ebp="00000000"
global esi
esi="00000000"
global edi
edi="00000000"

def RegWrite(reg,val):
    if(reg=="0"):
        global eax
        eax=val
    if(reg=="1"):
        global ecx
        ecx=val
    if(reg=="2"):
        global edx
        edx=val
    if(reg=="3"):
        global ebx
        ebx=val
    if(reg=="4"):
        global esp
        esp=val
    if(reg=="5"):
        global ebp
        ebp=val
    if(reg=="6"):
        global esi
        esi=val
    if(reg=="7"):
        global edi
        edi=val

def RegRead(reg):
    if(reg=="0"):
        return eax
    if(reg=="1"):
        return ecx
    if(reg=="2"):
        return edx
    if(reg=="3"):
        return ebx
    if(reg=="4"):
        return esp
    if(reg=="5"):
        return ebp
    if(reg=="6"):
        return esi
    if(reg=="7"):
        return edi
#Memory------------------------------------------------
global Memory
Memory={}


def MemoryRead(temp):
    tmp=num(temp)
    return Memory[tmp]+Memory[tmp+1]+Memory[tmp+2]+Memory[tmp+3]

def MemoryWrite(temp,val):
    tmp=num(temp)
    global Memory
    Memory[tmp]=val[0:2]
    Memory[tmp+1]=val[2:4]
    Memory[tmp+2]=val[4:6]
    Memory[tmp+3]=val[6:8]

def MemoryCopy(temp,val):
    tmp=num(arc(temp))
    global Memory
    i=0
    while i<len(val):
        Memory[tmp+i/2]=val[i]+val[i+1]
        i+=2
def MemoryGet(temp,six=False):
    tmp=num(arc(temp))
    global Memory
    if not(tmp in Memory):
        return "00000000"
    if six:
        return Memory[tmp]+Memory[tmp+1]+Memory[tmp+2]+Memory[tmp+3]+Memory[tmp+4]+Memory[tmp+5]
    s=Memory[tmp]
    if (s[0]=="3") or (s[0]=="4") or (s[0]=="5") or (s[0]=="c"):
        return Memory[tmp]+Memory[tmp+1]+Memory[tmp+2]+Memory[tmp+3]+Memory[tmp+4]+Memory[tmp+5]
    elif (s[0]=="7") or (s[0]=="8"):
        return Memory[tmp]+Memory[tmp+1]+Memory[tmp+2]+Memory[tmp+3]+Memory[tmp+4]
    elif (s[0]=="2") or (s[0]=="6") or (s[0]=="a") or (s[0]=="b"):
        return Memory[tmp]+Memory[tmp+1]
    elif (s[0]=="0") or (s[0]=="1") or (s[0]=="9") or (s[0]=="d"):
        return Memory[tmp]
    else:
        return ""
#alu-------------------------------------------------------
def GetBin(k):
    global a
    a=[]
    s=k[0:2]
    i=get(s[0])*16+get(s[1])
    temp=i
    s=k[2:4]
    i=get(s[0])*16+get(s[1])
    temp+=i*256
    s=k[4:6]
    i=get(s[0])*16+get(s[1])
    temp+=i*256*256
    s=k[6:8]
    i=get(s[0])*16+get(s[1])
    temp+=i*256*256*256
    while(len(a)<32):
        a.append(temp%2)
        temp=temp/2
    return a

def change(arr):
    i=0
    ans=0
    while(i<31):
        ans=ans*2+arr[i]
        i+=1
    if(arr[i]==1):
         ans=-ans
    return ans

def change0x(k1,k2,k3,k4):
    k=k1*8+k2*4+k3*2+k4
    if(k==15):
        return "f"
    elif(k==14):
        return "e"
    elif(k==13):
        return "d"
    elif(k==12):
        return "c"
    elif(k==11):
        return "b"
    elif(k==10):
        return "a"
    elif(k==9):
        return "9"
    elif(k==8):
        return "8"
    elif(k==7):
        return "7"
    elif(k==6):
        return "6"
    elif(k==5):
        return "5"
    elif(k==4):
        return "4"
    elif(k==3):
        return "3"
    elif(k==2):
        return "2"
    elif(k==1):
        return "1"
    elif(k==0):
        return "0"

def alu(op,alua,alub,setCC=True):
    global CF
    global ZF
    global SF
    global OF
    if setCC:
        CF=False
        ZF=False
        SF=False
        OF=False
    temp=GetBin(alua)
    global bina
    bina=temp[:]
    temp=GetBin(alub)
    global binb
    binb=temp[:]
    temp=GetBin("00000000")
    global binc
    binc=temp[:]
    binc.append(0)    
    
    if(op=="1"):
        for i in range(0,32):
            bina[i]=bina[i] ^ 1
        bina[0]+=1
        for i in range(0,31):
            if(bina[i]>2):
                bina[i+1]+=bina[i]/2
                bina[i]=bina[i]%2
    
        if(bina[31]>2):
            bina[31]=bina[31]%2    

    i=0;
    while(i<32):
        binc[i]+=bina[i]+binb[i]
        if(binc[i]>=2):
            binc[i+1]+=binc[i]/2
            binc[i]=binc[i]%2
        i+=1

    if setCC and (binc[32]!=0):
        CF=True

    if(op=="2"):
        for i in range(0,32):
            binc[i]=bina[i] & binb[i]
        if setCC:
            CF=False
    
    if(op=="3"):
        for i in range(0,32):
            binc[i]=bina[i] ^ binb[i]
        if setCC:
            CF=False

    a=change(bina)
    b=change(binb)
    c=change(binc)    
    
    if setCC:
        if(c==0):
            ZF=True
        if(c<0):
            SF=True
        if(((a<0)==(b<0)) and ((c<0)!=(a<0))):
            OF=True
    
    s0=change0x(binc[7],binc[6],binc[5],binc[4])
    s1=change0x(binc[3],binc[2],binc[1],binc[0])
    s2=change0x(binc[15],binc[14],binc[13],binc[12])
    s3=change0x(binc[11],binc[10],binc[9],binc[8])
    s4=change0x(binc[23],binc[22],binc[21],binc[20])
    s5=change0x(binc[19],binc[18],binc[17],binc[16])
    s6=change0x(binc[31],binc[30],binc[29],binc[28])
    s7=change0x(binc[27],binc[26],binc[25],binc[24])
    
    s=s0+s1+s2+s3+s4+s5+s6+s7
    return s
    
def check(func):
    if(func=="0"):#jmp
        return True
    elif(func=="1"):#jle
        return (SF == (not OF)) or ZF
    elif(func=="2"):#jl
        return (SF == (not OF))
    elif(func=="3"):#je
        return ZF
    elif(func=="4"):#jne
        return not ZF
    elif(func=="5"):#jge
        return not(SF == (not OF))
    elif(func=="6"):#jg
        return (not (SF == (not OF))) and (not ZF)
    else:
        return False
#---------------------------------------------------------------------------------------------------------------------
def next(pc):
    if(pc=="X"):
        return "X"
    s=MemoryGet(pc)
    if(s[0]=="0"):
        return arc(alu("0",arc(pc),"01000000",False))
    elif(s[0]=="1"):
        return arc(alu("0",arc(pc),"01000000",False))
    elif(s[0]=="2"):
        return arc(alu("0",arc(pc),"02000000",False))
    elif(s[0]=="3"):
        return arc(alu("0",arc(pc),"06000000",False))
    elif(s[0]=="4"):
        return arc(alu("0",arc(pc),"06000000",False))
    elif(s[0]=="5"):
        return arc(alu("0",arc(pc),"06000000",False))
    elif(s[0]=="6"):
        return arc(alu("0",arc(pc),"02000000",False))
    elif(s[0]=="7"):
        return arc(alu("0",arc(pc),"05000000",False))
    elif(s[0]=="8"):
        return arc(alu("0",arc(pc),"05000000",False))
    elif(s[0]=="9"):
        return arc(alu("0",arc(pc),"01000000",False))
    elif(s[0]=="a"):
        return arc(alu("0",arc(pc),"02000000",False))
    elif(s[0]=="b"):
        return arc(alu("0",arc(pc),"02000000",False))
    elif(s[0]=="c"):
        return arc(alu("0",arc(pc),"06000000",False))
    elif(s[0]=="d"):
        return arc(alu("0",arc(pc),"01000000",False))
    else:
        return "X"

def show():
    print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX[State]XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#F---------------------------------------
    s=read("pc")
    if(s=="X"):
        print ("[Fetch____]\t[]")
    else:
        k=MemoryGet(s)        
        print ("[Fetch____]\t[%s:%s]" %(s,k))

    print ("pc=%s" %(read("pc")))
    print("------------------------ALL---------------------------")
    
#D---------------------------------------
    s=read("D_index")
    if(s=="X"):
        print ("[Decode]\t[]")
    else:
        k=MemoryGet(s)
        print ("[Decode]\t[%s:%s]" %(s,k))

    print ("D_icode=%s" %(read("D_icode")))
    print ("D_ifunc=%s" %(read("D_ifunc")))
    print ("ra=%s" %(read("rA")))
    print ("rb=%s" %(read("rB")))
    print ("D_valC=%s" %(read("D_valC")))
    print ("D_valP=%s" %(read("D_valP")))
    print("------------------------ALL---------------------------")
#E----------------------------------------
    s=read("E_index")
    if(s=="X"):
        print ("[Execute]\t[]")
    else:
        k=MemoryGet(s)
        print ("[Execute]\t[%s:%s]" %(s,k))

    print ("E_icode=%s" %(read("E_icode")))
    print ("E_ifunc=%s" %(read("E_ifunc")))
    print ("E_valC=%s" %(read("E_valC")))
    print ("E_valA=%s" %(read("E_valA")))
    print ("E_valB=%s" %(read("E_valB")))
    print ("E_dstE=%s" %(read("E_dstE")))
    print ("E_dstM=%s" %(read("E_dstM")))
    print ("srcA=%s" %(read("srcA")))
    print ("srcB=%s" %(read("srcB")))
    print("------------------------ALL---------------------------")
#M----------------------------------------
    s=read("M_index")
    if(s=="X"):
        print ("[Memory]\t[]")
    else:
        k=MemoryGet(s)
        print ("[Memory]\t[%s:%s]" %(s,k))

    print ("M_icode=%s" %(read("M_icode")))
    print ("bch=%s" %(read("bch")))
    print ("M_valE=%s" %(read("M_valE")))
    print ("M_valM=%s" %(read("M_valM")))
    print ("M_dstE=%s" %(read("M_dstE")))
    print ("M_dstM=%s" %(read("M_dstM")))
    print("------------------------ALL---------------------------")
#W----------------------------------------
    s=read("W_index")
    if(s=="X"):
        print ("[WriteBack]\t[]")
    else:
        k=MemoryGet(s)
        print ("[WriteBack]\t[%s:%s]" %(s,k))

    print ("W_icode=%s" %(read("W_icode")))
    print ("W_valE=%s" %(read("W_valE")))
    print ("W_valM=%s" %(read("W_valM")))
    print ("W_dstE=%s" %(read("W_dstE")))
    print ("W_dstM=%s" %(read("W_dstM")))
    print("------------------------ALL---------------------------")
    
    print("[total_cycle]=%d" %(intread("total_cycle")))
    print("[valid_cycle]=%d" %(intread("valid_cycle")))

    print ("[0]eax=%s" %(RegRead("0")))
    print ("[1]ecx=%s" %(RegRead("1")))
    print ("[2]edx=%s" %(RegRead("2")))
    print ("[3]ebx=%s" %(RegRead("3")))
    print ("[4]esp=%s" %(RegRead("4")))
    print ("[5]ebp=%s" %(RegRead("5")))
    print ("[6]esi=%s" %(RegRead("6")))
    print ("[7]edi=%s" %(RegRead("7")))








