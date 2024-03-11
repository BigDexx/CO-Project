registers = { 'zero': '00000', 'ra': '00001', 'sp': '00010','gp': '00011', 'tp': '00100', 't0': '00101','t1': '00110','t2': '00111', 's0': '01000', 'fp': '01000', 's1': '01001', 'a0': '01010', 'a1': '01011', 'a2': '01100', 'a3': '01101', 'a4': '01110', 'a5': '01111', 'a6': '10000', 'a7': '10001', 's2': '10010', 's3': '10011', 's4': '10100', 's5': '10101', 's6': '10110', 's7': '10111', 's8': '11000', 's9': '11001', 's10': '11010', 's11': '11011', 't3': '11100', 't4': '11101', 't5': '11110', 't6': '11111' }
instructionsR = { "add": ["0000000", "000"], "sub": ["0100000", "000"], "sll": ["0000000", "001"], "slt": ["0000000", "010"], "sltu": ["0000000", "011"], "xor": ["0000000", "100"], "srl": ["0000000", "101"], "or": ["0000000", "110"], "and": ["0000000", "111"] }
instructionsI = { "lw": ["010", "0000011"], "addi": ["000", "0010011"], "sltiu": ["011", "0010011"], "jalr": ["000", "1100111"] }
instructionsS = ["sw"]
instructionsB = { "beq": "000", "bne": "001", "blt": "100", "bge": "101", "bltu": "110", "bgeu": "111" }
instructionsU = {"auipc":"0010111", "lui":"0110111"}
instructionsJ = ["jal"]
instructionsbonus=["mul", "rst", "halt" ,"rvrs"]
labeldict={}




def sextRISB(n):
   binary_string = bin(n & ((1 << 12) - 1))[2:].zfill(12)
   return binary_string

def sextJ(n):
    binary_string = bin(n & ((1 << 21) - 1))[2:].zfill(21)
    return binary_string

def sextU(n):
    binary_string = bin(n & ((1 << 20) - 1))[2:].zfill(20)
    return binary_string

def sextB(n):
    binary_string = bin(n & ((1 << 13) - 1))[2:].zfill(13)
    return binary_string

#------------------------------------------------------------------------------------------------
def rtype(instruct, register):
    opcode = "0110011"
    temp=instructionsR[instruct]
    funct7=temp[0]
    funct3=temp[1]
    return funct7 + registers[register[2]] + registers[register[1]] + funct3 + registers[register[0]] + opcode
    
def stype(instruct,register):
    register[1],temp=register[1].split('(')
    temp=temp[0:-1:1]
    register.append(temp)
    t=sextRISB(int(register[1]))
    return t[0:7]+registers[register[0]]+registers[register[2]]+"010"+t[7:12]+"0100011"

def utype(instruct,register):
    opcode=instructionsU[instruct]
    t=sextU(int(register[1]))
    return t+registers[register[0]]+opcode
    

def jtype(instruct,register):
    t=sextJ(int(register[1]))
    return t[0]+t[10:20]+t[9]+t[1:9]+registers[register[0]]+"1101111"
    
def itype(instruct,register):
    temp=instructionsI[instruct]
    funct3=temp[0]
    opcode=temp[1]
    
    if instruct == "lw":
        register[1],temp=register[1].split('(')
        temp=temp[0:-1:1]
        register.append(temp)
        t=sextRISB(int(register[1]))
        return t+registers[register[2]]+funct3+registers[register[0]]+opcode
    
    t=sextRISB(int(register[2]))    
    return t+registers[register[1]]+funct3+registers[register[0]]+opcode

def btype(instruct, register, counter):
    opcode = "1100011"
    if register[2] not in labeldict:
        t = sextB(int(register[2]))
        return t[0] + t[2:8] + registers[register[1]] + registers[register[0]] + instructionsB[instruct] + t[8:12] + t[1] + opcode
    else:
        t = sextB((counter - labeldict[register[2]])*4)
       
        return t[0] + t[2:8] + registers[register[1]] + registers[register[0]] + instructionsB[instruct] + t[8:12] + t[1] + opcode  
    

def bonustype(instruct, register):
    if instruct == "mul":
       return "000000"+registers[register[2]]+registers[register[1]]+"00"+registers[register[0]]+"000000"
    elif instruct == "rst":
        return "0"*32
    elif instruct == "halt":
        return "0"*32
    elif instruct == "rvrs":
        return "0"*11+registers[register[1]]+"00"+registers[register[0]]+"000000"

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#INPUT

file_path = 'example.txt'
with open("D:/Coding/example.txt", 'r') as file:
    lines = file.readlines()



counter=0
for n in lines:
    if ':' in str(n):
        n = n.strip()
        label,instruct, reg=n.split(" ")
        labeldict[label[:-1]]=counter
    else:
        counter += 1

counter = 0
for n in lines:
    if ':' in str(n):
        n = n.strip()
        label,instruct, reg=n.split(" ")
        register=list(map(str, reg.split(",")))
        labeldict[label[:-1]]=counter
    else:
        n = n.strip()
        instruct, reg=n.split(" ")
        register=list(map(str, reg.split(",")))   
       
    counter+=1

    if instruct in instructionsR:
        print(rtype(instruct, register))
    elif instruct in instructionsI:
        print(itype(instruct, register))
    elif instruct in instructionsS:
        print(stype(instruct, register))
    elif instruct in instructionsB:
        print(btype(instruct, register,counter))
    elif instruct in instructionsU:
        print(utype(instruct, register))
    elif instruct in instructionsJ:
        print(jtype(instruct, register))
    elif instruct in instructionsbonus:
        print(bonustype(instruct, register))  




