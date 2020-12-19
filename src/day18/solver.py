import re
from functools import reduce
from utils.file import read_file


def evaluate_inner_exp_a(exp):
    m = re.findall('(\\d+|\\*|\\+)', exp)
    answer = m[0]
    for i in range(1, len(m), 2):
        op, val = m[i:i+2]
        answer = eval(str(answer) + op + str(val))
    return str(answer)


def evaluate_inner_exp_b(exp):
    split = re.split('\\*', exp)
    return str(reduce(lambda a, v: a * int(eval(v)), split[1:], int(eval(split[0]))))


def evaluate_inner_parentheses(exp, evaluate_inner_exp, start, end):
    return exp[:start] + evaluate_inner_exp(exp[start + 1:end - 1]) + exp[end:]


def evaluate(exp, inner_exp_evaluator):
    while True:
        m = re.search('\\(([^\\)\\(]+)\\)', exp)
        if not m:
            break
        exp = evaluate_inner_parentheses(exp, inner_exp_evaluator, *m.span())
    return inner_exp_evaluator(exp)


def solve(inp, ev_fn):
    answer = 0
    for row in inp:
        row = re.sub(r'\s+', '', row)
        answer += int(evaluate(row, ev_fn))
    return answer


data = read_file('day18/1.in').splitlines()
print(solve(data, evaluate_inner_exp_a), solve(data, evaluate_inner_exp_b))

