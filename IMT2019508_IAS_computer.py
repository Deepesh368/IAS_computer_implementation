"""Information about program 1 and program 2 is written in IMT2019508_readme.txt """


expression_1 = "{0:{fill}39b}"
expression_2 = "{0:{fill}40b}"


def jump_plus_lhs():
    global PC
    global MAR
    global memory
    global AC
    global IBR
    if(AC[0] == "0"):
        PC = MAR
        IBR = "00000000000000000000"
    return 0


def jump_lhs():
    global PC
    global MAR
    global memory
    global AC
    global IBR
    PC = MAR
    IBR = "00000000000000000000"
    return 0


def jump_plus_rhs():
    global PC
    global MAR
    global memory
    global AC
    global IBR
    if(AC[0] == "0"):
        PC = MAR
        m_index = int(MAR, 2)
        m_string = ""
        for i in range(20, 40):
            m_string += str(memory[m_index][i])
        IBR = m_string
    return 0


def jump_rhs():
    global PC
    global MAR
    global memory
    global AC
    global IBR
    PC = MAR
    m_index = int(MAR, 2)
    m_string = ""
    for i in range(20, 40):
        m_string += str(memory[m_index][i])
    IBR = m_string
    return 0


def load_mq():
    global AC
    global MQ
    AC = MQ
    return 0


def mul():
    global AC
    global MQ
    global memory
    global MAR
    d_index = int(MAR, 2)
    d_string = ""
    for i in range(0, 40):
        d_string += str(memory[d_index][i])
    val1 = int(MQ[1:40], 2)
    if(MQ[0] == "1"):
        val1 = val1 * -1
    val2 = int(d_string[1:40], 2)
    if(d_string[0] == "1"):
        val2 = val2 * -1
    val1 = val1 * val2
    most_significant = ""
    if(val1 < 0):
        most_significant += "1"
        val1 = val1 * -1
    string = "{0:{fill}80b}".format(val1, fill='0')
    most_significant += string[1:40]
    AC = most_significant
    MQ = string[40:80]
    return 0


def load_mq_mx():
    global MAR
    global memory
    global MQ
    d_index = int(MAR, 2)
    d_string = ""
    for i in range(0, 40):
        d_string += str(memory[d_index][i])
    MQ = d_string
    return 0


def load_mx():
    global AC
    global MAR
    global memory
    d_index = int(MAR, 2)
    d_string = ""
    for i in range(0, 40):
        d_string += str(memory[d_index][i])
    AC = d_string
    return 0


def load_negative_mx():
    global AC
    global MAR
    global memory
    d_index = int(MAR, 2)
    d_string = ""
    if(memory[d_index][0] == 0):
        d_string += "1"
    else:
        d_string += "0"
    for i in range(1, 40):
        d_string += str(memory[d_index][i])
    AC = d_string
    return 0


def load_absolute_mx():
    global AC
    global MAR
    global memory
    d_index = int(MAR, 2)
    d_string = ""
    d_string += "0"
    for i in range(1, 40):
        d_string += str(memory[d_index][i])
    AC = d_string
    return 0


def store_mx():
    global AC
    global MAR
    global memory
    d_index = int(MAR, 2)
    for i in range(0, 40):
        memory[d_index][i] = int(AC[i])
    return 0


def add_mx():
    global expression_1
    global expression_2
    global AC
    global MAR
    global memory
    d_index = int(MAR, 2)
    d_string = ""
    for i in range(0, 40):
        d_string += str(memory[d_index][i])
    val1 = int(AC[1:40], 2)
    if(AC[0] == "1"):
        val1 = val1 * -1
    val2 = int(d_string[1:40], 2)
    if(d_string[0] == "1"):
        val2 = val2 * -1
    val1 = val1 + val2
    if(val1 < 0):
        val1 = val1 * -1
        AC = "1" + expression_1.format(val1, fill='0')
    else:
        AC = expression_2.format(val1, fill='0')
    return 0


def halt():
    return -1


def sub_mx():
    global expression_1
    global expression_2
    global AC
    global MAR
    global memory
    d_index = int(MAR, 2)
    d_string = ""
    for i in range(0, 40):
        d_string += str(memory[d_index][i])
    val1 = int(AC[1:40], 2)
    if(AC[0] == "1"):
        val1 = val1 * -1
    val2 = int(d_string[1:40], 2)
    if(d_string[0] == "1"):
        val2 = val2 * -1
    val1 = val1 - val2
    if(val1 < 0):
        val1 = val1 * -1
        AC = "1" + expression_1.format(val1, fill='0')
    else:
        AC = expression_2.format(val1, fill='0')
    return 0


def div():
    global expression_1
    global expression_2
    global PC
    global MAR
    global memory
    global AC
    global MQ
    d_index = int(MAR, 2)
    d_string = ""
    for i in range(0, 40):
        d_string += str(memory[d_index][i])
    val1 = int(AC[1:40], 2)
    if(AC[0] == "1"):
        val1 = val1 * -1
    val2 = int(d_string[1:40], 2)
    if(d_string[0] == "1"):
        val2 = val2 * -1
    quotient = int(val1 / val2)
    remainder = int(val1 % val2)
    if(remainder < 0):
        remainder = remainder * -1
        AC = "1" + expression_1.format(remainder, fill='0')
    else:
        AC = expression_2.format(remainder, fill='0')
    if(quotient < 0):
        quotient = quotient * -1
        MQ = "1" + expression_1.format(quotient, fill='0')
    else:
        MQ = expression_2.format(quotient, fill='0')
    return 0


def execute():
    global IR
    if(IR == "00000001"):                   # LOAD M(X)
        return load_mx()
    elif(IR == "00000010"):                 # LOAD -M(X)
        return load_negative_mx()
    elif(IR == "00000011"):                 # LOAD |M(X)|
        return load_absolute_mx()
    elif(IR == "00100001"):                 # STOR M(X)
        return store_mx()
    elif(IR == "00000101"):                 # ADD M(X)
        return add_mx()
    elif(IR == "00000110"):                 # SUB M(X)
        return sub_mx()
    elif(IR == "00001010"):                 # LOAD MQ
        return load_mq()
    elif(IR == "00001101"):                 # JUMP M(X,0:19)
        return jump_lhs()
    elif(IR == "00001111"):                 # JUMP+ M(X,0:19)
        return jump_plus_lhs()
    elif(IR == "00001110"):                 # JUMP M(X,20:39)
        return jump_rhs()
    elif(IR == "00010000"):                 # JUMP+ M(X,20:39)
        return jump_plus_rhs()
    elif(IR == "00001100"):                 # DIV M(X)
        return div()
    elif(IR == "00001011"):
        return mul()
    elif(IR == "11111111"):                 # HALT
        return halt()


empty_forty = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
PC = "000000000000"
AC = "0000000000000000000000000000000000000000"
MBR = "0000000000000000000000000000000000000000"
MQ = "0000000000000000000000000000000000000000"
IBR = "00000000000000000000"
IR = "00000000"
MAR = "000000000000"
memory = []
for i in range(0, 1000):
    memory.append(empty_forty)

# Program 1 hardcoded into memory
"""memory[0] = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
             0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]

memory[1] = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]

memory[2] = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
             1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

memory[3] = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
             1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

memory[12] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]

memory[13] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]"""

# Program 2 hardcoded into memory
memory[0] = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
             0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]

memory[1] = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]

memory[2] = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
             0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]

memory[3] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

memory[4] = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
             0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]

memory[5] = [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]

memory[6] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

memory[12] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

memory[13] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

print("a = ", memory[12])
print("b = ", memory[13])
print("Initially c = ", memory[14])

check = 0
while(check != -1):                          # Fetch Cycle
    if(IBR == "00000000000000000000"):  # If IBR is empty
        MAR = PC
        m_index = int(MAR, 2)
        m_string = ""
        for i in range(0, 40):
            m_string += str(memory[m_index][i])
        MBR = m_string
        if(MBR[0: 20] != "00000000000000000000"):  # Memory has no left instruction
            IBR = MBR[20: 40]
            IR = MBR[0: 8]
            MAR = MBR[8: 20]
            check = execute()
        else:
            IR = MBR[20: 28]
            MAR = MBR[28: 40]
            val = int(PC, 2)
            val += 1                       # PC = PC + 1
            val_string = "{0:{fill}12b}".format(val, fill='0')
            PC = val_string
            check = execute()
    else:
        IR = IBR[0: 8]
        MAR = IBR[8: 20]
        IBR = "00000000000000000000"
        val = int(PC, 2)
        val += 1
        val_string = "{0:{fill}12b}".format(val, fill='0')
        PC = val_string
        check = execute()

print("Finally c = ", memory[14])
