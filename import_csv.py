#_____________________________________________Read markers and draw as cubes from csv
import csv   
import bpy  
def string_toFloat(myString):
    myString = str(myString)
    myString = myString.replace('[', '')
    myString = myString.replace(']', '')
    myString = myString.replace('(', '')
    myString = myString.replace(')', '')
    myString = myString.replace(' ', '')
    myString = float(myString)
    return (myString)  



def read_markers_csv(filename):
    import csv   
    import bpy 
    # csv file name 
    #filename = "test4.csv"  
    # initializing the titles and rows list 
    fields = [] 
    rows = []   
    # reading csv file 
    with open(filename, 'r') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.reader(csvfile)       
        # extracting field names through first row 
        fields = next(csvreader)
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row)   
        # get total number of rows 
        print("Total no. of rows: %d"%(csvreader.line_num))   
    # printing the field names 
    print('Field names are:' + ', '.join(field for field in fields))   
    #  printing first all rows 
    verts = []#a list
    print('\nFirst ' + str(csvreader.line_num) + ' rows are:\n') 
    for i in range(0,csvreader.line_num-1):
    #    print(rows[i])
        e=0
        while e < len(rows[i]):
            one_vertex = [float(rows[i][e]),float(rows[i][e+1]),float(rows[i][e+2])]#A tuple
            print(one_vertex)
            if i==0:
                bpy.ops.mesh.primitive_cube_add(radius=0.1, view_align=False, enter_editmode=False, location=one_vertex, layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
                bpy.context.object.name = "marker_"+ str(e//3)
                bpy.data.objects['marker_'+str(e//3)].keyframe_insert(data_path="location", frame=i)
            else:
                bpy.data.objects['marker_'+str(e//3)].location = one_vertex
                bpy.data.objects['marker_'+str(e//3)].keyframe_insert(data_path="location", frame=i)
            e=e+3 
    return
       
read_markers_csv('test4.csv')

