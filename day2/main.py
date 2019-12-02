import sys

def add(opOne, opTwo):
    return opOne + opTwo

def mul(opOne, opTwo):
    return opOne * opTwo

def execute_program(noun, verb):
    tmp_memory = memory[:]
    tmp_memory[1] = noun
    tmp_memory[2] = verb
    opcode = tmp_memory[0]
    instruction_pointer = 0

    while opcode != 99:
        opOne = tmp_memory[tmp_memory[instruction_pointer + 1]]
        opTwo = tmp_memory[tmp_memory[instruction_pointer + 2]]
        tmp_memory[tmp_memory[instruction_pointer + 3]] = add(opOne, opTwo) if opcode == 1 else mul(opOne, opTwo)
        instruction_pointer += 4
        opcode = tmp_memory[instruction_pointer]

    return tmp_memory

def part_one():
    tmp_memory = execute_program(12, 2)
    return tmp_memory[0]

def part_two():
    for noun in range(100):
        for verb in range(100):
            tmp_memory = execute_program(noun, verb)
            if (tmp_memory[0] == 19690720):
                return 100 * noun + verb

if __name__ == '__main__':
    memory = [int(i) for i in sys.stdin.readlines()[0].strip().split(",")]
    print("p1: " + str(part_one()))
    print("p2: " + str(part_two()))
