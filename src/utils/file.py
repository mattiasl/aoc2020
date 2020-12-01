import os


def read_file(name):
    f = open(os.path.join(os.path.dirname(__file__).replace("/utils", ""), name), "r")
    answer = f.read()
    f.close()
    return answer


