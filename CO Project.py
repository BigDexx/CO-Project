registers = { 'zero': '00000', 'ra': '00001', 'sp': '00010','gp': '00011', 'tp': '00100', 't0': '00101','t1': '00110','t2': '00111', 's0': '01000', 'fp': '01000', 's1': '01001', 'a0': '01010', 'a1': '01011', 'a2': '01100', 'a3': '01101', 'a4': '01110', 'a5': '01111', 'a6': '10000', 'a7': '10001', 's2': '10010', 's3': '10011', 's4': '10100', 's5': '10101', 's6': '10110', 's7': '10111', 's8': '11000', 's9': '11001', 's10': '11010', 's11': '11011', 't3': '11100', 't4': '11101', 't5': '11110', 't6': '11111' }
instructionsR = { "add": ["0000000", "000"], "sub": ["0100000", "000"], "sll": ["0000000", "001"], "slt": ["0000000", "010"], "sltu": ["0000000", "011"], "xor": ["0000000", "100"], "srl": ["0000000", "101"], "or": ["0000000", "110"], "and": ["0000000", "111"] }
def Rtype(n):
    instr = n[0]
    funct7 = ""
    funct3 = ""
    temp = ""
    opcode = "0110011"
    
    if instr == "add":
        funct7 = "0000000"
        funct3 = "000"
    elif instr == "sub":
        funct7 = "0100000"
        funct3 = "000"
    elif instr == "sll":
        funct7 = "0000000"
        funct3 = "001"
    elif instr == "slt":
        funct7 = "0000000"
        funct3 = "010"
    elif instr == "sltu":
        funct7 = "0000000"
        funct3 = "011"
    elif instr == "xor":
        funct7 = "0000000"
        funct3 = "100"
    elif instr == "srl":
        funct7 = "0000000"
        funct3 = "101"
    elif instr == "or":
        funct7 = "0000000"
        funct3 = "110"
    elif instr == "and":
        funct7 = "0000000"
        funct3 = "111"

    return opcode + registers[n[3]] + funct3 + registers[n[1]] + "00000" + funct7

def Rtype(n):
    instr = n[0]
    funct7 = ""
    funct3 = ""
    temp = ""
    opcode = "0110011"
    
    if instr == "add":
        funct7 = "0000000"
        funct3 = "000"
    elif instr == "sub":
        funct7 = "0100000"
        funct3 = "000"
    elif instr == "sll":
        funct7 = "0000000"
        funct3 = "001"
    elif instr == "slt":
        funct7 = "0000000"
        funct3 = "010"
    elif instr == "sltu":
        funct7 = "0000000"
        funct3 = "011"
    elif instr == "xor":
        funct7 = "0000000"
        funct3 = "100"
    elif instr == "srl":
        funct7 = "0000000"
        funct3 = "101"
    elif instr == "or":
        funct7 = "0000000"
        funct3 = "110"
    elif instr == "and":
        funct7 = "0000000"
        funct3 = "111"

    return opcode + registers[n[3]] + funct3 + registers[n[1]] + "00000" + funct7

instruction = input("Enter R-type instruction").split()
print(Rtype(instruction))
