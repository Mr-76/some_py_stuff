import os
def main():
    cwd = os.getcwd()
    walking_dirs = os.walk(cwd)
    for (root,other_dir,files) in walking_dirs:
        print(root)
        print(other_dir)
        print(files)
        for name_file in files:
            print(os.path.join(root,name_file))

if __name__ == "__main__":
    main()
