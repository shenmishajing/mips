import re


def dec2bin(x, length=5, base=10):
    if not isinstance(x, int):
        x = int(x, base)

    if x < 0:
        x += 2 ** length
    x = bin(x).replace('0b', '')

    if len(x) < length:
        x = '0' * (length - len(x)) + x
    return x


def dec2hex(x, length=5, base=10):
    if not isinstance(x, int):
        x = int(x, base)

    if x < 0:
        x += 16 ** length
    x = hex(x).replace('0x', '')

    if len(x) < length:
        x = '0' * (length - len(x)) + x
    return x


def bin2dec(x):
    d = int(x[1:], 2)
    if x[0] == '1':
        d = -d
    return d


op_list = dict()
fun_list = dict()

inv_op_list = dict()
inv_fun_list = dict()

fun_list['sll'] = dec2bin(0x00, length=6)
fun_list['srl'] = dec2bin(0x02, length=6)
fun_list['sra'] = dec2bin(0x03, length=6)
fun_list['jr'] = dec2bin(0x08, length=6)
fun_list['jalr'] = dec2bin(0x09, length=6)
fun_list['syscall'] = dec2bin(0x0C, length=6)
fun_list['break'] = dec2bin(0x0D, length=6)
fun_list['mfhi'] = dec2bin(0x10, length=6)
fun_list['mflo'] = dec2bin(0x11, length=6)
fun_list['mthi'] = dec2bin(0x12, length=6)
fun_list['mtlo'] = dec2bin(0x13, length=6)
fun_list['mult'] = dec2bin(0x18, length=6)
fun_list['multu'] = dec2bin(0x19, length=6)
fun_list['div'] = dec2bin(0x1A, length=6)
fun_list['divu'] = dec2bin(0x1B, length=6)
fun_list['add'] = dec2bin(0x20, length=6)
fun_list['addu'] = dec2bin(0x21, length=6)
fun_list['sub'] = dec2bin(0x22, length=6)
fun_list['subu'] = dec2bin(0x23, length=6)
fun_list['and'] = dec2bin(0x24, length=6)
fun_list['or'] = dec2bin(0x25, length=6)
fun_list['xor'] = dec2bin(0x26, length=6)
fun_list['nor'] = dec2bin(0x27, length=6)
fun_list['slt'] = dec2bin(0x2A, length=6)
fun_list['sltu'] = dec2bin(0x2B, length=6)

for op in fun_list.keys():
    op_list[op] = dec2bin(0x00, length=6)

op_list['j'] = dec2bin(0x02, length=6)
op_list['jal'] = dec2bin(0x03, length=6)
op_list['beq'] = dec2bin(0x04, length=6)
op_list['bne'] = dec2bin(0x05, length=6)
op_list['blez'] = dec2bin(0x06, length=6)
op_list['bgtz'] = dec2bin(0x07, length=6)
op_list['addi'] = dec2bin(0x08, length=6)
op_list['addiu'] = dec2bin(0x09, length=6)
op_list['slti'] = dec2bin(0x0A, length=6)
op_list['sltiu'] = dec2bin(0x0B, length=6)
op_list['andi'] = dec2bin(0x0C, length=6)
op_list['ori'] = dec2bin(0x0D, length=6)
op_list['xori'] = dec2bin(0x0E, length=6)
op_list['lui'] = dec2bin(0x0F, length=6)
op_list['eret'] = dec2bin(0x10, length=6)
op_list['mfco'] = dec2bin(0x10, length=6)
op_list['mtco'] = dec2bin(0x10, length=6)
op_list['lb'] = dec2bin(0x20, length=6)
op_list['lh'] = dec2bin(0x21, length=6)
op_list['lw'] = dec2bin(0x23, length=6)
op_list['lbu'] = dec2bin(0x24, length=6)
op_list['lhu'] = dec2bin(0x25, length=6)
op_list['sb'] = dec2bin(0x28, length=6)
op_list['sh'] = dec2bin(0x29, length=6)
op_list['sw'] = dec2bin(0x2B, length=6)

for key, value in op_list.items():
    inv_op_list[value] = key

for key, value in fun_list.items():
    inv_fun_list[value] = key

inv_op_list[dec2bin(0, length=6)] = 'r'


def find_register(reg):
    if isinstance(reg, int):
        return dec2bin(reg)
    if reg[1] != 'a' and reg[0] == 'r' or reg[0] == 'R':
        return dec2bin(reg[1:])
    else:
        if reg == 'zero':
            return dec2bin(0)
        elif reg == 'at':
            return dec2bin(1)
        elif reg[0] == 'v':
            return dec2bin(int(reg[1]) + 2)
        elif reg[0] == 'a':
            return dec2bin(int(reg[1]) + 4)
        elif reg[0] == 't' and reg[1] <= '7':
            return dec2bin(int(reg[1]) + 8)
        elif reg[0] == 's' and reg[1] != 'p':
            return dec2bin(int(reg[1]) + 16)
        elif reg[0] == 't' and reg[1] >= '8':
            return dec2bin(int(reg[1]) + 16)
        elif reg == 'gp':
            return dec2bin(28)
        elif reg == 'sp':
            return dec2bin(29)
        elif reg == 'fp':
            return dec2bin(30)
        elif reg == 'ra':
            return dec2bin(31)
        else:
            return dec2bin(reg)


def find_register_name(reg):
    if isinstance(reg, str):
        reg = int(reg, 2)
    if reg == 0:
        return '$zero'
    elif reg == 1:
        return '$at'
    elif reg == 2 or reg == 3:
        return '$v' + str(reg - 2)
    elif 4 <= reg <= 7:
        return '$a' + str(reg - 4)
    elif 8 <= reg <= 15:
        return '$t' + str(reg - 8)
    elif 16 <= reg <= 23:
        return '$s' + str(reg - 16)
    elif 24 <= reg <= 125:
        return '$t' + str(reg - 16)
    elif reg == 28:
        return '$gp'
    elif reg == 29:
        return '$sp'
    elif reg == 30:
        return '$fp'
    elif reg == 31:
        return '$ra'


class mips_re:
    def __init__(self):
        self.pdd = re.compile(r'\s*([0-9a-fA-FxX]*)\s*;?\s*(?:(?:\\\\|#).*)?')
        self.pl = re.compile(r'\s*\$\s*(.*)\s*,\s*(.*)\s*;?\s*(?:(?:\\\\|#).*)?')
        self.pm = re.compile(r'\s*\$\s*(.*)\s*,\s*\$(.*)\s*;?\s*(?:(?:\\\\|#).*)?')
        self.at = re.compile(r'\s*([0-9a-fA-F]*)\s*;?\s*(?:(?:\\\\|#).*)?')
        self.rt = re.compile(r'\s*\$\s*(.*)\s*,\s*\$(.*)\s*,\s*\$(.*)\s*;?\s*(?:(?:\\\\|#).*)?')
        self.it = re.compile(r'\s*\$\s*(.*)\s*,\s*\$(.*)\s*,\s*(.*)\s*;?\s*(?:(?:\\\\|#).*)?')
        self.lui = re.compile(r'\s*\$\s*(.*)\s*,\s*(.*)\s*;?\s*(?:(?:\\\\|#).*)?')
        self.jt = re.compile(r'\s*(.*)\s*;?\s*(?:(?:\\\\|#).*)?')
        self.jr = re.compile(r'\s*\$\s*(.*)\s*;?\s*(?:(?:\\\\|#).*)?')
        self.ls = re.compile(r'\s*\$\s*(.*)\s*,\s*(.*)\s*\(\s*\$\s*(.*)\s*\)\s*;?\s*(?:(?:\\\\|#).*)?')


mr = mips_re()


def assembler(code):
    binary = []
    labels = dict()
    cur_localtion = 0
    non_deal_label = []
    psudo_instruction = ['dd', 'move', 'la', 'li']

    for line in code:
        line = line.strip()
        if line == '':
            continue
        if ':' in line:
            label, line = line.split(':')
            label = label.strip()
            line = line.strip()
            if 'baseaddr' in label.lower() or 'dataaddr' in label.lower():
                m = mr.at.match(line)
                new_localtion = int(m.group(1), 16)
                for i in range(cur_localtion, new_localtion // 4):
                    binary.append(dec2bin(0, length=32))
                cur_localtion = new_localtion // 4
                continue
            else:
                labels[label] = dec2bin(cur_localtion, 26)
        line = line.split()
        line[0] = line[0].lower()
        for i in range(2, len(line)):
            line[1] += line[i]
        if line[0] in psudo_instruction:

            if line[0] == 'dd':
                m = mr.pdd.match(line[1])
                b = dec2bin(int(m.group(1), 16), length=32)
            elif line[0] == 'move':
                m = mr.pm.match(line[1])
                op = op_list['add']
                fun = fun_list['add']
                rs = find_register(m.group(2))
                rt = find_register(0)
                rd = find_register(m.group(1))
                shamt = dec2bin(0x00, length=5)
                b = op + rs + rt + rd + shamt + fun
            else:
                m = mr.pl.match(line[1])
                op = op_list['addi']
                rs = find_register(0)
                rt = find_register(m.group(1))
                if line[0] == 'la':
                    target = m.group(2)
                    if target in labels:
                        i = dec2bin(int(labels[target], 2), length=16)
                    else:
                        i = ''
                        non_deal_label.append((len(binary), target, 'la'))
                else:
                    i = dec2bin(m.group(2), 16)
                b = op + rs + rt + i
        else:
            op = op_list[line[0]]
            if op == dec2bin(0x00, length=6):
                fun = fun_list[line[0]]
                if line[0] == 'sll' or line[0] == 'srl' or line[0] == 'sra':
                    m = mr.it.match(line[1])
                    rs = find_register(0)
                    rt = find_register(m.group(2))
                    rd = find_register(m.group(1))
                    shamt = dec2bin(m.group(3), length=5)
                elif line[0] == 'jr':
                    m = mr.jr.match(line[1])
                    rs = find_register(m.group(1))
                    rt = find_register(0)
                    rd = find_register(0)
                    shamt = dec2bin(0x00, length=5)
                else:
                    m = mr.rt.match(line[1])
                    rs = find_register(m.group(2))
                    rt = find_register(m.group(3))
                    rd = find_register(m.group(1))
                    shamt = dec2bin(0x00, length=5)
                b = op + rs + rt + rd + shamt + fun
            elif line[0] == 'j' or line[0] == 'jal':
                m = mr.jt.match(line[1])
                target = m.group(1)
                if target in labels:
                    i = labels[target]
                else:
                    i = ''
                    non_deal_label.append((len(binary), target, 'j'))
                b = op + i
            else:
                if line[0] == 'lw' or line[0] == 'sw':
                    m = mr.ls.match(line[1])
                    rs = find_register(m.group(3))
                    rt = find_register(m.group(1))
                    i = dec2bin(m.group(2), 16)
                elif line[0] == 'lui':
                    m = mr.lui.match(line[1])
                    rs = find_register(0)
                    rt = find_register(m.group(1))
                    i = dec2bin(m.group(2), 16)
                else:
                    m = mr.it.match(line[1])
                    rs = find_register(m.group(2))
                    rt = find_register(m.group(1))
                    if line[0] == 'beq' or line[0] == 'bne':
                        rs, rt = rt, rs
                        target = m.group(3)
                        if target in labels:
                            i = dec2bin((int(labels[target], 2) - len(binary)), length=16)
                        else:
                            i = ''
                            non_deal_label.append((len(binary), target, 'branch'))
                    else:
                        i = dec2bin(m.group(3), 16)
                b = op + rs + rt + i

        binary.append(b)
        cur_localtion += 1

    for line, target, op in non_deal_label:
        if op == 'j':
            binary[line] = binary[line] + labels[target]
        elif op == 'la':
            binary[line] = binary[line] + labels[target][10:]
        else:
            binary[line] = binary[line] + dec2bin((int(labels[target], 2) - line), length=16)

    return binary


def inv_assembler(binary):
    code = []
    cur_label_number = 0
    labels = dict()
    non_deal_label = []

    for line in binary:
        line = line.strip()
        if line == '':
            continue
        op = inv_op_list[line[:6]]
        rs = find_register_name(line[6:11])
        rt = find_register_name(line[11:16])
        rd = find_register_name(line[16:21])
        shamt = str(int(line[21:26], 2))
        i = str(int(line[16:], 2))
        addr = int(line[6:], 2)
        if op == 'r':
            op = inv_fun_list[line[26:]]
            if op == 'jr':
                c = op + ' ' + rs
            elif op == 'sll' or op == 'srl' or op == 'sra':
                c = op + ' ' + rd + ', ' + rt + ', ' + shamt
            else:
                c = op + ' ' + rd + ', ' + rs + ', ' + rt

        elif op == 'j' or op == 'jal':
            if addr in labels:
                c = op + ' ' + labels[addr]
            else:
                if addr < len(code):
                    code[addr] = 'L' + str(cur_label_number) + ':' + code[addr]
                    labels[addr] = 'L' + str(cur_label_number)
                    c = op + ' ' + labels[addr]
                    cur_label_number += 1
                else:
                    non_deal_label.append((len(code), addr))
                    c = op + ' '
        else:
            if op == 'lui':
                c = op + ' ' + rt + ', ' + i
            elif op == 'lw' or op == 'sw':
                c = op + ' ' + rt + ', ' + i + '(' + rs + ')'
            elif op == 'beq' or op == 'bne':
                i = int(i)
                if i + len(code) in labels:
                    c = op + ' ' + rs + ', ' + rt + ', ' + labels[i + len(code)]
                else:
                    if i < 0:
                        code[i + len(code)] = 'L' + str(cur_label_number) + ':' + code[i + len(code)]
                        labels[i + len(code)] = 'L' + str(cur_label_number)
                        c = op + ' ' + rs + ', ' + rt + ', ' + labels[i + len(code)]
                        cur_label_number += 1
                    else:
                        non_deal_label.append((len(code), i + len(code)))
                        c = op + ' ' + rs + ', ' + rt + ', '
            else:
                c = op + ' ' + rs + ', ' + rt + ', ' + i

        code.append(c)

    for line, target in non_deal_label:
        code[target] = 'L' + str(cur_label_number) + ':' + code[target]
        labels[target] = 'L' + str(cur_label_number)
        code[line] += labels[target]
        cur_label_number += 1

    return code
