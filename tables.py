opcodes = {
#   opcode  : instrxn   type
    '10000' : 'add',    # A
    '10001' : 'sub',    # A
    '10010' : 'mov',    # B
    '10011' : 'mov',    # C
    '10100' : 'ld',     # D
    '10101' : 'st',     # D
    '10110' : 'mul',    # A
    '10111' : 'div',    # C
    '11000' : 'rs',     # B
    '11001' : 'ls',     # B
    '11010' : 'xor',    # A
    '11011' : 'or',     # A
    '11100' : 'and',    # A
    '11101' : 'not',    # C
    '11110' : 'cmp',    # C
    '11111' : 'jmp',    # E
    '01100' : 'jlt',    # E
    '01101' : 'jgt',    # E
    '01111' : 'je',     # E
    '01010' : 'hlt'     # F
}

registers = {
#   addr  : name
    '000' : 'R0',
    '001' : 'R1',
    '010' : 'R2',
    '011' : 'R3',
    '100' : 'R4',
    '101' : 'R5',
    '110' : 'R6',
    '111' : 'FLAG'
}

errors = {
    '01' : 'Typo in instruction name or register.',
    '02' : 'Use of undefined variable.',
    '03' : 'Use of undefined label.',
    '04' : 'Illegal use of FLAG register.',
    '05' : 'Illegal immediate value (more than 8 bits).',
    '06' : 'Misuse of label as variable or vice versa.',
    '07' : 'Variables not declared at the beginning.',
    '08' : 'Missing hlt instruction.',
    '09' : 'Last instruction is not hlt.'
}
