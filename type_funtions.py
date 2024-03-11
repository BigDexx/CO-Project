from dictionaries import instructionsR,instructionsI,instructionsS,instructionsB,instructionsU,instructionsJ,registers
def sextRISB(n):
   binary_string = bin(n & ((1 << 12) - 1))[2:].zfill(12)
   return binary_string
def sextUJ(n):
    binary_string = bin(n & ((1 << 20) - 1))[2:].zfill(20)
    return binary_string
def sextB(n):
    binary_string = bin(n & ((1 << 13) - 1))[2:].zfill(13)
    return binary_string


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
    t=sextUJ(int(register[1]))
    return t+registers[register[0]]+opcode
    

def jtype(instruct,register):
    t=sextUJ(int(register[1]))
    return t[0]+t[9:20]+t[9]+t[1:8]+registers[register[0]]+"0010111"
    
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

def btype(instruct, register):
  opcode = "1100011"
  t = sextB(int(register[2]))
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
