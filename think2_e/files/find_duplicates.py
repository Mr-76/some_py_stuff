import os
dic_dup = dict()
def find_files(cwd,suffix):
    global dic_dup
    files_list = []
    all_file_folder = os.listdir(cwd)
    for folder_or_file in all_file_folder:
        path = os.path.join(cwd,folder_or_file)
        if os.path.isfile(path):
            if (suffix in path):

                files_list.append(path)
            else:
                pass;
        else:
            find_files(path,suffix)
    for file in files_list:
        md5 = os.popen("md5sum "+file)
        string_md5 = md5.read().split(" ").pop(0)
        dic_dup.setdefault(string_md5,[]).append(file)
    
    print (dic_dup)
    print(10*"-")
    for key in dic_dup:
        if (len(dic_dup[key]) >= 2):
            print("DUPLICATE FILE FOUND")
            print( dic_dup[key])
def main():
    cwd = os.getcwd()
    find_files(cwd,".txt")

if __name__ == "__main__":
    main()
