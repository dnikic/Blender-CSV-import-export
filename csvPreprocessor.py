def header_remover(filename):
    #filename = "test5.csv"
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    #print(len(lines))
    #print(type(lines))
    f = open(filename+"_fixed"+".csv", "w")
    #new_lines = []
    chars = set('abcdefghijklmn_+=[]()!$%^&*()')
    for i in range(0,len(lines)):
        # print(lines[i])
        #print(type(lines[i]))
        if any((c in chars) for c in lines[i]):
            f.write(lines[i])#FoundAnd writen header
            break
        else:
            continue
    for i in range(0,len(lines)):
        # print(lines[i])
        #print(type(lines[i]))
        if any((c in chars) for c in lines[i]):
            print('Removed line ',i)
        else:
            #new_lines.append(lines[i])
            f.write(lines[i])
    #print(new_lines)
    f.close()

header_remover("test5.csv")
