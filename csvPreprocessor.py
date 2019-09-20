def header_remover(filename):
    #filename = "test5.csv"
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    #print(len(lines))
    #print(type(lines))
    f = open(filename+"_fixed"+".csv", "w")
    for i in range(0,len(lines)):
        # print(lines[i])
        #print(type(lines[i]))
        #Find header line
        if "vicon_timestamp" in lines[i]:
            f.write(lines[i])#FoundAnd writen header
            break
        else:
            continue
    #Find value line
    for i in range(0,len(lines)):
        # print(lines[i])
        #print(type(lines[i]))
        if "vicon_timestamp" in lines[i]:
            print('Removed line ',i)
        else:
            f.write(lines[i])
    f.close()

header_remover("output.csv")
