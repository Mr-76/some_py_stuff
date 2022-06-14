def in_bisec(list1,target):
    middle = len(list1)//2
    for index in range(0,middle):
        if (list1[index] == target):
            print("found in first half")
            return True
    for index in range(middle,len(list1)):
        if (list1[index] == target):
            print("found in second half")
            return True
    print("not found")
    return False
def main():
    test_list1 = [1,3,3,1,2,1,5,1,23,1,3,2,1,6,7,8,8,3,4,5,7,8]
    test_list2 = [1,3,3,1,2,3,5,1,23,1,3,2,1,6,7,8,8,3,3,5,7,8]
    test_list3 = [1,3,4,1,2,0,5,1,23,1,3,2,1,6,7,8,8,3,3,5,7,8]
    target = 4
    in_bisec(test_list1,target)
    in_bisec(test_list2,target)
    in_bisec(test_list3,target)
if __name__ == "__main__":
    main()
