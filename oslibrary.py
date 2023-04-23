import os
current_file_absolute_path = __file__
current_directory = os.getcwd()
target_folder_path = os.path.join(current_directory,'output')
if 'output' not in os.listdir(current_directory):
    os.mkdir(target_folder_path)


target_file_path = os.path.join(target_folder_path,'my_first_file_output.txt')

output_file = open(target_file_path,'w+')
for input_line in open('file_text.txt'):
    output_file.write('HPCSA '+input_line)
    
output_file.seek(0)
var = output_file.readlines()
print(var)
output_file.close()

