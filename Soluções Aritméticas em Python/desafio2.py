x = int(input())
n = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(n)):
    n[i] = x
    x = x * 2
    print('N[{}] = {}'.format(i, n[i]))

