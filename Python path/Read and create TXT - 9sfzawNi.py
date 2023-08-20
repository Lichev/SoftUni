import os
import csv

folder_path = 
new_folder_path = 

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Iterate through the files in the folder
for file in files:
    # Check if the file is DETAIL file
    if file.endswith('.DETAIL'):
        # Open the file and read it
        file_path = os.path.join(folder_path, file)
        store_lines = []
        with open(file_path, 'r') as f:
            contents = csv.reader(f, delimiter='\t')
            # nested loop here
            for line in contents:
                if line[3] == '56094886':
                    line[3] = '70136911'
                if line[7] == '56094886':
                    line[7] = '70136911'
                store_lines.append(line)

        # if the new folder dont exist

        # if not os.path.exists(new_folder_path):
        #     os.makedirs(new_folder_path)

        # Create a file with the same name
        new_file_path = os.path.join(new_folder_path, file)
        with open(new_file_path, 'w', encoding='UTF8', newline='') as new_f:
            # Write the lines from store_lines list
            writer = csv.writer(new_f, delimiter='\t')
            for line in store_lines:
                writer.writerow(line)

print('all done')
