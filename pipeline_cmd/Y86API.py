import data
import Readin
import main
def setY86(register,memory):
    data.write("CF",register["CF"])
    data.write("OF",register["OF"])
    data.write("ZF",register["ZF"])
    data.write("SF",register["SF"])

    data.write("stall",register["stall"])
    data.write("end",register["end"])

    data.write("pc",register["pc"])
    data.write("F_icode",register["F_icode"])

    data.write("D_index",register["D_index"])
    data.write("D_icode",register["D_icode"])
    data.write("D_ifunc",register["D_ifunc"])
    data.write("rA",register["rA"])
    data.write("rB",register["rB"])
    data.write("D_valC",register["D_valC"])
    data.write("D_valP",register["D_valP"])

    data.write("E_index",register["E_index"])
    data.write("E_icode",register["E_icode"])
    data.write("E_ifunc",register["E_ifunc"])
    data.write("E_valC",register["E_valC"])
    data.write("E_valA",register["E_valA"])
    data.write("E_valB",register["E_valB"])
    data.write("E_dstE",register["E_dstE"])
    data.write("E_dstM",register["E_dstM"])
    data.write("srcA",register["srcA"])
    data.write("srcB",register["srcB"])

    data.write("M_index",register["M_index"])
    data.write("M_icode",register["M_icode"])
    data.write("bch",register["bch"])
    data.write("M_valE",register["M_valE"])
    data.write("M_valM",register["M_valM"])
    data.write("M_dstE",register["M_dstE"])
    data.write("M_dstM",register["M_dstM"])

    data.write("W_index",register["W_index"])
    data.write("W_icode",register["W_icode"])
    data.write("W_valE",register["W_valE"])
    data.write("W_valM",register["W_valM"])
    data.write("W_dstE",register["W_dstE"])
    data.write("W_dstM",register["W_dstM"])
    
    data.RegWrite("0",register["eax"])
    data.RegWrite("1",register["ecx"])
    data.RegWrite("2",register["edx"])
    data.RegWrite("3",register["ebx"])
    data.RegWrite("4",register["esp"])
    data.RegWrite("5",register["ebp"])
    data.RegWrite("6",register["esi"])
    data.RegWrite("7",register["edi"])

    data.intwrite("total_cycle",register["total_cycle"])
    data.intwrite("valid_cycle",register["valid_cycle"])    

    data.Memory=memory

def getY86():
    #global register
    register={}
    #global memory
    register={}
    register["CF"]=data.read("CF")
    register["OF"]=data.read("OF")
    register["ZF"]=data.read("ZF")
    register["SF"]=data.read("SF")
    
    register["stall"]=data.read("stall")
    register["end"]=data.read("end")
    
    register["pc"]=data.read("pc")
    register["F_icode"]=data.read("F_icode")
    
    register["D_index"]=data.read("D_index")
    register["D_icode"]=data.read("D_icode")
    register["D_ifunc"]=data.read("D_ifunc")
    register["rA"]=data.read("rA")
    register["rB"]=data.read("rB")
    register["D_valC"]=data.read("D_valC")
    register["D_valP"]=data.read("D_valP")

    register["E_index"]=data.read("E_index")
    register["E_icode"]=data.read("E_icode")
    register["E_ifunc"]=data.read("E_ifunc")
    register["E_valC"]=data.read("E_valC")
    register["E_valA"]=data.read("E_valA")
    register["E_valB"]=data.read("E_valB")
    register["E_dstE"]=data.read("E_dstE")
    register["E_dstM"]=data.read("E_dstM")
    register["srcA"]=data.read("srcA")
    register["srcB"]=data.read("srcB")

    register["M_index"]=data.read("M_index")
    register["M_icode"]=data.read("M_icode")
    register["bch"]=data.read("bch")
    register["M_valE"]=data.read("M_valE")
    register["M_valM"]=data.read("M_valM")
    register["M_dstE"]=data.read("M_dstE")
    register["M_dstM"]=data.read("M_dstM")

    register["W_index"]=data.read("W_index")
    register["W_icode"]=data.read("W_icode")
    register["W_valE"]=data.read("W_valE")
    register["W_valM"]=data.read("W_valM")
    register["W_dstE"]=data.read("W_dstE")
    register["W_dstM"]=data.read("W_dstM")

    register["eax"]=data.RegRead("0")
    register["ecx"]=data.RegRead("1")
    register["edx"]=data.RegRead("2")
    register["ebx"]=data.RegRead("3")
    register["esp"]=data.RegRead("4")
    register["ebp"]=data.RegRead("5")
    register["esi"]=data.RegRead("6")
    register["edi"]=data.RegRead("7")
    
    register["total_cycle"]=data.intread("total_cycle")
    register["valid_cycle"]=data.intread("valid_cycle")

    memory=data.Memory
    return register,memory    
    
def exeY86():
    main.execute()

def initY86(linelist):
    Readin.linelist=linelist[:]
    Readin.readin()

def executeY86(Reg,Mem,Wrd=[""]):
    if(Wrd[0]==""):
        try:
            setY86(Reg,Mem)
        except:
            raise Y86err("The Register or Memory you set is not fitable!")
        try:
            exeY86()
        except:
            raise Y86err("Logical Error!!!")
        try:
            _reg,_mem = getY86()
            return _reg,_mem
        except:
            raise Y86err("The Inner Information is Error!")
    else:
        try:
            initY86(Wrd)
        except:
            raise Y86err("The YO File Information You Post is not fitable!")
        try:
            exeY86()
        except:
            raise Y86err("Logical Error!!!")
        try:
            _reg,_mem = getY86()
            for i in range(0,len(data.RealNum)):
                _reg[data.LineNum[i]]=data.RealNum[i]
                print(data.LineNum[i])
            return _reg,_mem
        except:
            raise Y86err("The Inner Information is Error!")
    


