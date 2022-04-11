namespaces = {
    'global': {'parent': None, 'vars': set()},
}

def create(namesp, arg):
    if namesp == 'global':
        tmp = namespaces['global']
        s = tmp['vars']
        s.append(arg)
    pass

def add(namesp, arg):
    pass

def get(namesp, arg):
    pass

num = int(input())
cmd, namesp, arg = input().split()

print(f'{cmd}, {namesp}, {arg}')
for i in range(num):
    if cmd == 'create':
        create(namesp, arg)

    elif cmd == 'add':
        add(namesp, arg)

    elif cmd == 'get':
        get(namesp, arg)