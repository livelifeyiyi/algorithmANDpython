char = raw_input()
lens = len(char)
arry = ''
arrb = ''
arrr = ''
for i in range(0,lens):
    if(char[i] == '<'):
        i = i+1
        if(char[i] == 'y'):
            i = i+7
            while(char[i] != '<'):
                arry += char[i]
                i +=1
        i += 1
        if(char[i] == 'b'):
            i += 5
            while(char[i] != '<'):
                arrb += char[i]
                i +=1
                
                