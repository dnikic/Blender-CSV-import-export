# Blender-CSV-import-export
```
Use Blender to read, analzie, filter and export as mocap data as a csv table.
In Blender run import_csv.py to import data, edit as keyframe data and export the edited data using export_csv.py.
The file test4.csv has been provided as an example structure of mocap marker locations.
Markers will be represented as small 3d cubes with keyframe animated locations.
```

# Example of usecase
```
0  Importing csv data
 Run scvPreprocessor to remove multiple headers.
 Make backup of output.csv
 Remove pupil data from csv files and vicon timestamp. 
 Use blender import script.
 Set playback start and end in blender
 If    you cant see the cubes:
 You can change  radius=0.1 to radius=10 if cubes are too small.
 In the viewport you can change the clipping plane distance to a much bigger value.

1  Removing lost values who are by default set to 0
 In 3D viewport select all cubes with A.
 In graph editor deselect all wiht A, find keyframes where y=0 and delete them.
 The deleted values will be replaced with spline interpolations.

2  Remove subject mismatching
In the graph editor search "y".
Select keyframes for subject one if y>0 (for subject two if y<0).
In dope sheet select x and z values for the selected y keyframe values.
Delete them or transfer them to the other subject.

3  Save fixed files
Export fixed files with export script.
Paste in timestamps, pupil data and first row with headers from backup.
```
