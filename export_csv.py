#_____________________________________________Once you have used the importer to read and edit csv data, you can export it via this script
import csv   
import bpy 
def write_markers_csv(filename):
    marker_nbr=0
    i=0
    while(1):
        try:
            print(bpy.data.objects['marker_'+str(i)])
            i=i+1
        except:
            marker_nbr = i
            break

    f = open(filename, "w")
    bpy.context.scene.frame_start = 0
    bpy.context.scene.frame_set(0)

    header =''
    row = ''
    for i in range(0,marker_nbr-1):
        header = header+'marker_'+str(i)+','
        header = header+'marker_'+str(i)+','   
        header = header+'marker_'+str(i)+','   
    header = header+'marker_'+str(i+1)+','
    header = header+'marker_'+str(i+1)+','   
    header = header+'marker_'+str(i+1) #We dont want "," at the end of a line

    for e in range (0,bpy.context.scene.frame_end):
        bpy.context.scene.frame_set(e)
        row = ''
        for i in range(0,marker_nbr-1):
            row = row + str()+ str(bpy.data.objects['marker_'+str(i)].location[0]) + ','  
            row = row + str()+ str(bpy.data.objects['marker_'+str(i)].location[1]) + ','  
            row = row + str()+ str(bpy.data.objects['marker_'+str(i)].location[2]) + ','  
        row = row + str()+ str(bpy.data.objects['marker_'+str(i+1)].location[0]) + ','  
        row = row + str()+ str(bpy.data.objects['marker_'+str(i+1)].location[1]) + ','  
        row = row + str()+ str(bpy.data.objects['marker_'+str(i+1)].location[2])   
        header = header + '\n' + row
        
        e = e+1
        
    #print(header)    
    f.write(header)
    f.close()

write_markers_csv('test4.csv')












