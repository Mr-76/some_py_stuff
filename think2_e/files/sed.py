import os
def main():
    sed("true","false","text1.txt","text2.txt")






def sed(pattern_string,replacement_string,file_name1,file_name2):
    try:
        with open(file_name1,"r") as file:
            contends = file.readlines()
    except:
        print("error reading file")
        return False
    for line in range(len(contends)):
        if (pattern_string in contends[line]):
            contends[line] = contends[line].replace(pattern_string,replacement_string)#strigns are immutable 
   #checking now if file exists

    if(not(os.path.exists(file_name2))):
        print("file does not exist")
    try:
        with open(file_name2,"w")  as file:
            for line in contends:
                file.write(line)
    except:
        print("error writing file2")
        return False
        
if __name__ == "__main__":
    main()
