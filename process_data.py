
def write_file(filename, text):
    text = f'{text}\n'
    with open(filename, 'a') as file:
        file.write(text)

def read_file(filename):
    input = open(filename, 'r').read() #open(sys.argv[1], 'r').read()
    literals = [i for i in list(set(input)) if i.isalpha()]
    cnf = input.splitlines()
    return cnf, literals