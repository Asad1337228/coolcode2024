import os

def categorize_files_by_type(folder_path):
    file_dict = {}

    for dirpath,dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            ext = os.path.splitext(filename)[1] 
            if ext:
                file_path = os.path.join(dirpath, filename)
                if ext not in file_dict:
                    file_dict[ext] = []
                file_dict[ext].append(file_path)

    return file_dict
chek = input()
result = categorize_files_by_type(chek)
print(result)
