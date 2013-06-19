import data
import Readin
clocknum=0

def nothing():
    return 0

def arc(s):#大端法与小端法转换
    return s[6]+s[7]+s[4]+s[5]+s[2]+s[3]+s[0]+s[1]

def forwarding(src):#实现转发机制
    global e_icode
    global e_dstE
    global e_valE
    global e_valM
    global m_icode
    global m_dstE
    global m_valE
    global m_valM
    if(((e_icode=="2") or (e_icode=="3") or (e_icode=="6") or (e_icode=="8") or (e_icode=="9") or (e_icode=="a") or (e_icode=="c")) and (e_dstE==src)):
            return e_valE
    if((e_icode=="b") and (src=="4")):
            return e_valE
    if((e_icode=="d") and (src=="4")):
            return e_valE
    if((e_icode=="d") and (src=="5")):#对于leave的加载使用冒险判断
            return "X"
    if(((e_icode=="5") or (e_icode=="b")) and (e_dstE==src)):#对于mrmovl的加载使用冒险判断
            return "X"

    if(((m_icode=="2") or (m_icode=="3") or (m_icode=="6") or (m_icode=="8") or (m_icode=="9") or (m_icode=="a") or (m_icode=="c")) and (m_dstE==src)):#如果已经进入了memory阶段，就可以直接转发，不需要暂停一个周期
            return m_valE
    if((m_icode=="b") and (src=="4")):
            return m_valE
    if((m_icode=="d") and (src=="4")):
            return m_valE
    if((m_icode=="d") and (src=="5")):
            return m_valM
    if(((m_icode=="5") or (m_icode=="b")) and (m_dstE==src)):
            return m_valM

    return data.RegRead(src)

#-----------------------
def execute():#执行一个clock
    global ret_pc
    global jmp_pc
    global call_pc
    global pred_pc
    global w_icode
    global w_valE
    global w_valM
    global w_dstE
    global w_dstM
    global m_icode
    global m_valE
    global m_valM
    global m_dstE
    global m_dstM
    global e_icode
    global e_bch
    global e_valE
    global e_valM
    global e_dstE
    global e_dstM
    global d_icode
    global d_ifunc
    global d_valC
    global d_valA
    global d_valB
    global d_dstE
    global d_dstM
    global d_srcA
    global d_srcB
    global f_icode
    global f_ifunc
    global f_ra
    global f_rb
    global f_valC
    global f_valP
    global total_cycle
    global valid_cycle
    while(data.isend()==False):#如果程序的结束状态为假，继续执行
        #data.show()
        #global clocknum
        #clocknum+=1
        #print("CLOCK_NO:%d" %(clocknum))
        #PipeClock.PipeClock();
        ret_pc=""
        jmp_pc=""
        call_pc=""
        pred_pc=""
    
        valid_cycle=data.intread("valid_cycle")
        total_cycle=data.intread("total_cycle")
        total_cycle+=1
        #print("CLOCK-------------------------------")
#WriteBack---------------------------------
        #print("writeback:")
        w_icode=data.read("W_icode")#从外部寄存器读入信号
        w_valE=data.read("W_valE")
        w_valM=data.read("W_valM")
        w_dstE=data.read("W_dstE")
        w_dstM=data.read("W_dstM")
    
        if(w_icode=="0"):#nop
            nothing()
        elif(w_icode=="1"):#halt  如果halt阶段执行完writeback阶段，程序就结束了，并且强行清空之前的4个阶段
            data.write("M_index","X")
            data.write("M_icode","0")
            data.write("E_index","X")
            data.write("E_icode","0")
            data.write("D_index","X")
            data.write("D_icode","0")
            data.write("pc","X")
            data.write("F_icode","0")
            data.setend()
        elif(w_icode=="2"):#rrmovl
            data.RegWrite(w_dstE,w_valE)
        elif(w_icode=="3"):#irmovl
            data.RegWrite(w_dstE,w_valE)
        elif(w_icode=="4"):#rmmovl
            nothing()
        elif(w_icode=="5"):#mrmovl
            data.RegWrite(w_dstE,w_valM)
        elif(w_icode=="6"):#op
            data.RegWrite(w_dstE,w_valE)
        elif(w_icode=="7"):#jmp
            nothing()
        elif(w_icode=="8"):#call
            data.RegWrite("4",w_valE)
        elif(w_icode=="9"):#ret
            data.RegWrite("4",w_valE)
        elif(w_icode=="a"):#push
            data.RegWrite("4",w_valE)
        elif(w_icode=="b"):#popl
            data.RegWrite("4",w_valE)
            data.RegWrite(w_dstE,w_valM)
        elif(w_icode=="c"):#iaddl
            data.RegWrite(w_dstE,w_valE)
        elif(w_icode=="d"):#leave
            data.RegWrite("4",w_valE)
            data.RegWrite("5",w_valM)

        if(w_icode=="0"):
            nothing()
        else:
            valid_cycle+=1
#Memory--------------------------------------
        #print("Memory:")
    
        m_icode=""
        m_valE=""
        m_valM=""
        m_dstE=""
        m_dstM=""

        m_icode=data.read("M_icode")#从外部读入信号
        m_valE=data.read("M_valE")
        m_valM=data.read("M_valM")
        m_dstE=data.read("M_dstE")
        m_dstM=data.read("M_dstM")
    
        if(m_icode=="0"):#nop
            m_valE=""
            m_valM=""
            m_dstE=""
            m_dstM=""
        elif(m_icode=="1"):#halt 一旦halt出现就要强行结束之前的3个阶段
            data.write("E_index","X")
            data.write("E_icode","0")
            data.write("D_index","X")
            data.write("D_icode","0")
            data.write("pc","X")
            data.write("F_icode","0")
        elif(m_icode=="2"):#rrmovl
            nothing()
        elif(m_icode=="3"):#irmovl
            nothing()
        elif(m_icode=="4"):#rmmovl
            data.MemoryWrite(m_dstM,m_valM)
        elif(m_icode=="5"):#mrmovl
            m_valM=data.MemoryRead(m_dstM)
        elif(m_icode=="6"):#op
            nothing()
        elif(m_icode=="7"):#jmp
            nothing()
        elif(m_icode=="8"):#call
            data.MemoryWrite(m_valE,m_valM)
        elif(m_icode=="9"):#ret ret阶段也要清空之前的所有阶段，直到下一步的指令明确
            m_valM=data.MemoryRead(m_dstM)
            ret_pc=arc(m_valM)# 从内存中读取出来的pc，用于更新pred_pc
            data.write("E_index","X")
            data.write("E_icode","0")
            data.write("D_index","X")
            data.write("D_icode","0")
            data.write("pc","X")
            data.write("F_icode","0")
        elif(m_icode=="a"):#push
            data.MemoryWrite(m_valE,m_valM)
        elif(m_icode=="b"):#pop
            m_valM=data.MemoryRead(m_dstM)
        elif(m_icode=="c"):#iaddl
            nothing()
        elif(m_icode=="d"):#leave
            m_valM=data.MemoryRead(m_dstM)
    
        data.write("W_index",data.read("M_index"))
    
        data.write("W_icode",m_icode)#将信号写入下一阶段
        data.write("W_valE",m_valE)
        data.write("W_valM",m_valM)
        data.write("W_dstE",m_dstE)
        data.write("W_dstM",m_dstM)
#Execute----------------------------------------------
        #print("Execute:")

        e_icode=""
        e_bch=""
        e_valE=""
        e_valM=""
        e_dstE=""
        e_dstM=""

        e_icode=data.read("E_icode")#从外部读入信号
        e_ifunc=data.read("E_ifunc")
        e_valC=data.read("E_valC")
        e_valA=data.read("E_valA")
        e_valB=data.read("E_valB")
        e_dstE=data.read("E_dstE")
        e_dstM=data.read("E_dstM")
        srcA=data.read("srcA")
        srcB=data.read("srcB")

        if(e_icode=="0"):#nop
            nothing()
            e_bch=""
            e_valE=""
            e_valM=""
            e_dstE=""
            e_dstM=""
        elif(e_icode=="1"):#halt 清空之前所有阶段
            data.write("D_index","X")
            data.write("D_icode","0")
            data.write("pc","X")
            data.write("F_icode","0")
        elif(e_icode=="2"):#rrmovl
            e_valE=e_valA
        elif(e_icode=="3"):#irmovl
            e_valE=e_valC
        elif(e_icode=="4"):#rmmovl
            aluA=e_valB
            aluB=e_valC
            e_dstM=data.alu("0",aluA,aluB)
            e_valM=e_valA
        elif(e_icode=="5"):#mrmovl
            aluA=e_valB
            aluB=e_valC
            e_dstM=data.alu("0",aluA,aluB)
            e_dstE=srcA
        elif(e_icode=="6"):#op
            aluA=e_valA
            aluB=e_valB
            e_valE=data.alu(e_ifunc,aluA,aluB)
            e_dstE=srcB
        elif(e_icode=="7"):#jmp
            if(data.check(e_ifunc)):#根据CF，SF，OF，ZF判断是否跳转
                data.write("D_index","X")
                data.write("D_icode","0")
                data.write("pc","X")
                data.write("F_icode","0")
                jmp_pc=arc(e_valC)#如果要改变当前流程的话，记录对应的pc值
                e_bch=jmp_pc
        elif(e_icode=="8"):#call
            e_valM=e_valB#将返回地址存入栈中
            aluA=e_valA
            aluB="04000000"
            e_valE=data.alu("1",aluB,aluA)
            data.write("D_index","X")
            data.write("D_icode","0")
            data.write("pc","X")
            data.write("F_icode","0")
            call_pc=arc(e_valC)        
            e_bch=call_pc    
        elif(e_icode=="9"):#ret
            aluA=e_valA
            aluB="04000000"
            e_valE=data.alu("0",aluA,aluB)
            data.write("D_index","X")
            data.write("D_icode","0")
            data.write("pc","X")
            data.write("F_icode","0")
            e_dstM=e_valA
        elif(e_icode=="a"):#push
            aluA=e_valB
            aluB="04000000"
            e_valE=data.alu("1",aluB,aluA)
            e_valM=e_valA
        elif(e_icode=="b"):#popl
            aluA=e_valB
            aluB="04000000"
            e_valE=data.alu("0",aluA,aluB)
            e_dstM=e_valB
            e_dstE=srcA
        elif(e_icode=="c"):#iaddl
            aluA=e_valA
            aluB=e_valC
            e_valE=data.alu("0",aluA,aluB)
            e_dstE=srcA
        elif(e_icode=="d"):#leave
            aluA=e_valA
            aluB="04000000"
            e_valE=data.alu("0",aluB,aluA)
            e_dstM=e_valA
            e_dstE="4"
        data.write("M_index",data.read("E_index"))

        data.write("M_icode",e_icode)#把信号写入到下一阶段
        data.write("bch",e_bch)
        data.write("M_valE",e_valE)
        data.write("M_valM",e_valM)
        data.write("M_dstE",e_dstE)
        data.write("M_dstM",e_dstM)
#Decode----------------------------------
        #print("Decode:")

        d_icode=""
        d_ifunc=""
        d_valC=""
        d_valA=""
        d_valB=""
        d_dstE=""
        d_dstM=""
        d_srcA=""
        d_srcB=""
    
        d_icode=data.read("D_icode")#从外部读入信号
        d_ifunc=data.read("D_ifunc")
        ra=data.read("rA")
        rb=data.read("rB")
        d_valC=data.read("D_valC")
        d_valP=data.read("D_valP")

        if(d_icode=="0"):#nop
            nothing()
            d_ifunc=""
            d_valC=""
            d_valA=""
            d_valB=""
            d_dstE=""
            d_dstM=""
            d_srcA=""
            d_srcB=""
        elif(d_icode=="1"):#halt
            nothing()
        elif(d_icode=="2"):#rrmovl
            Temp=forwarding(ra)#判断是否存在加载使用冒险
            if(Temp=="X"):
                data.setstall()#存在就暂停
            else:
                d_valA=Temp#否则取得forwarding的值
            d_dstE=rb
            d_srcA=ra
            d_srcB=rb
        elif(d_icode=="3"):#irmovl
            d_valA=d_valC
            d_dstE=rb
        elif(d_icode=="4"):#rmmovl-------------------------------------------------------------
            Temp=forwarding(ra)#判断要读取的寄存器a是否存在冒险
            if(Temp=="X"):
                data.setstall()
            else:
                d_valA=Temp
            Temp=forwarding(rb)#判断要读取的寄存器b是否存在冒险
            if(Temp=="X"):
                data.setstall()
            else:
                d_valB=Temp
            d_srcA=ra
            d_srcB=rb
        elif(d_icode=="5"):#mrmovl-------------------------------------------------------
            Temp=forwarding(rb)#判断寄存器a是否存在冒险
            if(Temp=="X"):
                data.setstall()
            else:
                d_valB=Temp
            d_dstE=ra
            d_srcA=ra
            d_srcB=rb
        elif(d_icode=="6"):#op------------------------------------------------------------------------
            Temp=forwarding(ra)#判断寄存器a是否存在冒险
            if(Temp=="X"):
                data.setstall()
            else:
                d_valA=Temp
            Temp=forwarding(rb)#判断寄存器b是否存在冒险
            if(Temp=="X"):
                data.setstall()
            else:
                d_valB=Temp
            d_srcA=ra
            d_srcB=rb
            d_dstE=rb
        elif(d_icode=="7"):#jmp----------------------
            nothing()
        elif(d_icode=="8"):#call---------------------
            Temp=forwarding("4")#特别要注意的是call隐式调用了esp，需要判断是否冒险
            if(Temp=="X"):
                data.setstall()
            else:
                d_valA=Temp
            d_valB=d_valP
            d_srcA="4"
            d_dstE="4"
        elif(d_icode=="9"):#ret--------------------------------------
            Temp=forwarding("4")#ret 调用了esp，需要判断冒险
            if(Temp=="X"):
                data.setstall()
            else:
                d_valA=Temp
            d_dstE="4"
            d_srcA="4"
        elif(d_icode=="a"):#push-------------------------------------
            Temp=forwarding(ra)#push 同时调用了esp ebp需要同时判断冒险
            if(Temp=="X"):
                data.setstall()
            else:
                d_valA=Temp
            Temp=forwarding("4")
            if(Temp=="X"):
                data.setstall()
            else:
                d_valB=Temp
            d_srcA=ra
            d_srcB="4"
            d_dstE="4"
        elif(d_icode=="b"):#popl---------------------------------------------------------------
            Temp=forwarding("4")#pop 调用了esp，需要判断冒险
            if(Temp=="X"):
                data.setstall()
            else:
                d_valB=Temp
            d_dstE=ra
            d_srcA=ra
            d_srcB="4"
        elif(d_icode=="c"):#iaddl-------------------------------------------------------------
            Temp=forwarding(ra)#判断iaddl的寄存器冒险
            if(Temp=="X"):
                data.setstall()
            else:
                d_valA=Temp
            d_valB=d_valC
            d_dstE=ra
            d_srcA=ra
        elif(d_icode=="d"):#leave------------------------------------------------------------
            Temp=forwarding("5")#leave要读取ebp，需要判断冒险
            if(Temp=="X"):
                data.setstall()
            else:
                d_valA=Temp
            d_dstE="4"
            d_dstM="5"
            d_srcA="5"

        if(data.isstall()):#如果说cycle中的decode和fetch处于暂停状态的话，在下一个Execute阶段需要插入一个bubble
            data.write("E_icode","0")
            data.write("E_index","X")
        else:#其他情况下，正常复制信号到外部寄存器
            data.write("E_index",data.read("D_index"))
    
            data.write("E_icode",d_icode)
            data.write("E_ifunc",d_ifunc)
            data.write("E_valC",d_valC)
            data.write("E_valA",d_valA)
            data.write("E_valB",d_valB)
            data.write("E_dstE",d_dstE)
            data.write("E_dstM",d_dstM)
            data.write("srcA",d_srcA)
            data.write("srcB",d_srcB)
#Fetch---------------------------------------------
        #print("Fetch:")
    
        f_icode=""
        f_ifunc=""
        f_ra=""
        f_rb=""
        f_valC=""
        f_valP=""
    
        f_icode=data.read("F_icode")#从外部寄存器读入信号
        pc=data.read("pc")    
    
        if(pc=="X"):#如果Fetch阶段因为stall不能取指，那么Fetch阶段本次不执行，但是需要将stall的一回合锁定取消，以保证下次能取指
            data.write("D_index","X")
            data.write("D_icode","0")
            data.write("F_icode","1")
            f_ifunc=""
            f_ra=""
            f_rb=""
            f_valC=""
            f_valP=""
            data.write("D_ifunc",f_ifunc)
            data.write("rA",f_ra)
            data.write("rB",f_rb)
            data.write("D_valC",f_valC)
            data.write("D_valP",f_valP)
        elif(f_icode=="0"):#如果Fetch阶段是因为ret和jXX被清零，那么同样恢复合法状态，保证下次能取指
            data.write("D_index","X")
            data.write("D_icode","0")
            data.write("F_icode","1")
            f_ifunc=""
            f_ra=""
            f_rb=""
            f_valC=""
            f_valP=""
            data.write("D_ifunc",f_ifunc)
            data.write("rA",f_ra)
            data.write("rB",f_rb)
            data.write("D_valC",f_valC)
            data.write("D_valP",f_valP)
        else:#如果就是合法，那么就根据内容正常取指
            pred_pc=data.next(pc)
            s=data.MemoryGet(pc)
                    
            if(s[0]=="0"):#nop
                nothing()
            if(s[0]=="1"):#halt
                nothing()
            if(s[0]=="2"):#rrmovl
                f_ra=s[2]
                f_rb=s[3]
            if(s[0]=="3"):#irmovl
                f_rb=s[3]
                f_valC=s[4:12]
            if(s[0]=="4"):#rmmovl
                f_ra=s[2]
                f_rb=s[3]
                f_valC=s[4:12]
            if(s[0]=="5"):#mrmovl
                f_ra=s[2]
                f_rb=s[3]
                f_valC=s[4:12]
            if(s[0]=="6"):#op
                f_ra=s[2]
                f_rb=s[3]
            if(s[0]=="7"):#jmp
                f_valC=s[2:10]
            if(s[0]=="8"):#call
                f_valC=s[2:10]
                f_ra="4"
            if(s[0]=="9"):#ret
                f_ra="4"
                nothing()
            if(s[0]=="a"):#push
                f_ra=s[2] 
                f_rb="4"
            if(s[0]=="b"):#pop
                f_ra=s[2]
                f_rb="4"
            if(s[0]=="c"):#iaddl
                f_ra=s[3]
                f_valC=s[4:12]
            if(s[0]=="d"):#leave
                f_ra="5"

        
            f_icode=s[0]
            f_ifunc=s[1]
            
            if(data.isstall()):
                nothing()
            else:#不暂停的合法状态下，将信号写入下一个Decode阶段
                data.write("D_index",pc)
                data.write("D_icode",f_icode)
                data.write("D_ifunc",f_ifunc)
                data.write("rA",f_ra)
                data.write("rB",f_rb)
                data.write("D_valC",f_valC)
                if(pred_pc[0]!="X"):
                    data.write("D_valP",arc(pred_pc))
                else:
                    data.write("D_valP","X")
#PC------------------------------------
        data.intwrite("total_cycle",total_cycle)#将总周期数写入外部
        data.intwrite("valid_cycle",valid_cycle)#将实际执行的周期数写入外部
        #print("PC:")
        if(data.isstall()):
            data.start()
            return 0

        if(ret_pc!=""):#判断下一个pc应该取什么值
            data.write("pc",ret_pc)#有ret先取ret_pc
        elif(call_pc!=""):
            data.write("pc",call_pc)#有call，取call_pc
        elif(jmp_pc!=""):
            data.write("pc",jmp_pc)#有jXX,取jmp_pc
        elif(pred_pc!=""):
            data.write("pc",pred_pc)#都没有的情况下取得下一个pc
        return 0
        #print("-------------------------Final--------------------------")


        
        
        












    
