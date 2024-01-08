import os
def count_lines(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        lines = file.readlines()
    return len(lines)
def sort_files_by_lines(file_list,directory_path):

    file_counts = {}

    for file in file_list:
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            line_count = count_lines(file_path)
            file_counts[file] = line_count

    sorted_files = sorted(file_counts.items(), key=lambda x: x[1])
    return sorted_files




def combine_files(file_paths, output_file_path):
    with open(output_file_path, 'w',encoding='utf-8') as output_file:
        for file_path in file_paths:
            with open(file_path, 'r',encoding='utf-8') as file:
                output_file.write(file_path+'\n')
                output_file.write(str(count_lines(file_path))+'\n')
                output_file.write(file.read()+'\n')
combine_files(['1.txt', '2.txt', '3.txt'], 'new_file.txt')

