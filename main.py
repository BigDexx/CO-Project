from dictionaries import instructionsR,instructionsI,instructionsS,instructionsB,instructionsU,instructionsJ,instructionsbonus
import type_funtions as isa
file_path = 'example.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    instruct, reg=line.split(" ")
    register=list(map(str, reg.split(",")))
    if instruct in instructionsR:
        print(isa.rtype(instruct, register))
    elif instruct in instructionsI:
        print(isa.itype(instruct, register))
    elif instruct in instructionsS:
        print(isa.stype(instruct, register))
    elif instruct in instructionsB:
        print(isa.btype(instruct, register))
    elif instruct in instructionsU:
        print(isa.utype(instruct, register))
    elif instruct in instructionsJ:
        print(isa.jtype(instruct, register))
    elif instruct in instructionsbonus:
        print(isa.bonustype(instruct, register))  
