import registers

n = list(map(str, input().split()))

def Rtype(n):
    instr=n[0]
    
    funct7=""
    funct3=""
    rd=n[1]
    r1=n[2]
    r2=n[3]
    temp=""
    opcode="0110011"
    if instr=="add":
        funct7="0000000"
        funct3="000"
    
    elif instr=="sub":
        funct7="0100000"
        funct3="000"

    elif instr=="sll":
        funct7="0000000"
        funct3="001"

    elif instr=="slt":
        funct7="0000000"
        funct3="010"

    elif instr=="sltu":
        funct7="0000000"
        funct3="011"

    elif instr=="xor":
        funct7="0000000"
        funct3="100"
    
    elif instr=="srl":
        funct7="0000000"
        funct3="101"

    elif instr=="or":
        funct7="0000000"
        funct3="110"

    
    elif instr=="and":
        funct7="0000000"
        funct3="111"
    

    return opcode+rd+funct3+r1+r2+funct7
    
print(Rtype(n))