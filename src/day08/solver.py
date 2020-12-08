from utils.file import read_file


def compile_source(source):
    return list(map(lambda split: {'op': split[0], 'arg': int(split[1])}, [i.split() for i in source]))


def run(program, ops):
    pointer, acc, visited = 0, 0, set()
    while pointer not in visited and pointer < len(program):
        visited.add(pointer)
        op, arg = program[pointer].values()
        acc, jump = ops[op](arg, acc)
        pointer += jump

    return pointer == len(program), acc


def star_a(program):
    return run(program, operations)[1]


def star_b(program, corrupt_instructions={'nop': 'jmp', 'jmp': 'nop'}):
    for instruction in filter(lambda i: program[i]['op'] in corrupt_instructions.keys(), range(len(program))):
        patched_program = program.copy()
        patched_program[instruction] = program[instruction].copy()
        patched_program[instruction]['op'] = corrupt_instructions[program[instruction]['op']]
        success, result = run(patched_program, operations)
        if success:
            return result


code = read_file('day08/1.in').splitlines()
operations = {
    'nop': lambda arg, acc: (acc, 1),
    'jmp': lambda arg, acc: (acc, arg),
    'acc': lambda arg, acc: (acc + arg, 1)
}
print(star_a(compile_source(code)), star_b(compile_source(code)))

