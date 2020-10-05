
print('Zacatek')
print('\n')

with open('train-labels.idx1-ubyte', 'rb') as f:
    big_byte = f.read()
    print(big_byte)
    
    '''
    while True:
        for i in range(4):
            byte[i] = f.read(1)
            print(byte)
        if (byte[i] != ""):
            break
    '''
    
    f.close()
    
print('\n')
print('Konec')
