# Open the data file for reading.
data_for_cleaning = open('C:\\[Insert Path]\\data_modified.csv', 'r');
written_data = open('C:\\[Insert Path]\\data_cleaned.csv', 'w');
# sz corresponds to the number of lines in the file.
sz = 0;
# col corresponds to the number of columns in the file.
cols = 0;
curr_line = data_for_cleaning.readline();

# position of Material, Organic names, Organic species, and Energy
e_col = 0;
mat_col = 0;
o_name_col = 0;
o_spec_col = 0;
# Determines the number of lines in the file.
while (len(curr_line) > 0):
    
    # Determine number of columns
    if (cols == 0):
        for i in range(len(curr_line)):
            if (curr_line[i] == ','):
                cols = cols + 1;
                
    # Determie position of Material, Energy, Organic names, and Organic species
    # columns.
    if (cols != 0 and e_col == 0):
        e_col = 1;
        split_line = curr_line.split(',', cols);
        for i in range(cols):
            if (split_line[i] == "Material"):
                mat_col = i;
            elif (split_line[i] == "Energy (eV)"):
                e_col = i;
            elif (split_line[i] == "Organic names"):
                o_name_col = i;
            elif (split_line[i] == "Organic species"):
                o_spec_col = i;
    sz = sz + 1;
    curr_line = data_for_cleaning.readline();
    
# Go back to the start of the file.
data_for_cleaning.seek(0);

# Can use the last written line as comparison because we already sorted by 
# Material and Organic names. We don't actually need energy since we pre-sorted
# it smallest to largest.

# Boolean for a write algorithm
data_write = 0;

for i in range(sz):

    data_write = 0;
    curr_line = data_for_cleaning.readline();
    split_line = curr_line.split(',', cols);
    
    # Ignore first case
    if (i == 0):
        data_write = 1;

    else:
        if (split_line[mat_col] != last_split[mat_col]):
            data_write = 1;
            
        else:
            if(split_line[o_name_col] != last_split[o_name_col] and
               split_line[o_spec_col] != last_split[o_spec_col]):
               data_write = 1;
            else:
                data_write = 0;
        
    # Write the data
    if (data_write == 1):
        written_data.write(curr_line);
        last_written_line = curr_line;
        last_split = last_written_line.split(',', cols);

data_for_cleaning.close();
written_data.close();