# Step 1: Read the "all_points.xyz" file
import glob
file_pattern = "*.xyz"
file_list = glob.glob(file_pattern)
input_file = file_list[0]
print(input_file)

# Initialize lists to store data
identities = [] # store id
coordinates = []  # To store X, Y, Z values
property_values = []  # To store the 5th column values

with open(input_file, "r") as file:
    lines = file.readlines()
    for line in lines:
        # Skip comment lines
        if line.startswith("#"):
            continue
        parts = line.strip().split()
        if len(parts) == 5:
            iden, x, y, z, prop = map(int, parts[0:5])
            identities.append(iden)
            coordinates.append((x, y, z))
            property_values.append(prop)

# Step 2: Write the data to "geo.txt"
output_file = "geo.txt"
output_file_1 = "node_set_1.txt"
output_file_2 = "node_set_2.txt"
output_file_3 = "node_set_3.txt"
output_file_4 = "node_set_4.txt"
output_file_5 = "node_set_5.txt"


with open(output_file, "w") as file, \
     open(output_file_1, "w") as file1, \
     open(output_file_2, "w") as file2, \
     open(output_file_3, "w") as file3, \
     open(output_file_4, "w") as file4, \
     open(output_file_5, "w") as file5:
    for i in range(len(coordinates)):
        iden = identities[i]
        x, y, z = coordinates[i]
        prop = property_values[i]
        # set block & node list
        if y==0 or y==2:
            file1.write(f"{iden}\n")
        if y==38 or y==40 :
            file2.write(f"{iden}\n")
        if x==0 or x==2 :
            file3.write(f"{iden}\n")
        if x==38 or x==40 :
            file4.write(f"{iden}\n")
        file5.write(f"{iden}\n")
    for j in range(len(coordinates)):
        iden = identities[j]
        x, y, z = coordinates[j]
        prop = property_values[j]
        # set block & node list
        if (y==0 and 2<x<38) or (y==2 and 2<x<38) :
            prop = prop+2
        elif (y==38 and 2<x<38) or (y==40 and 2<x<38) :
            prop = prop+4
        elif (x==0 and 2<y<38) or (x==2 and 2<y<38) :
            prop = prop+6
        elif (x==38 and 2<y<38) or (x==40 and 2<y<38) :
            prop = prop+8
        elif (x==0 and y==0) or (x==0 and y==2) or (x==2 and y==0) or (x==2 and y==2) :
            prop = prop+10
        elif (x==38 and y==0) or (x==38 and y==2) or (x==40 and y==0) or (x==40 and y==2) :
            prop = prop+12
        elif (x==38 and y==38) or (x==38 and y==40) or (x==40 and y==38) or (x==40 and y==40) :
            prop = prop+14
        elif (x==0 and y==38) or (x==0 and y==40) or (x==2 and y==38) or (x==2 and y==40) :
            prop = prop+16
        file.write(f"{x} {y} {z} {prop} 8\n")
