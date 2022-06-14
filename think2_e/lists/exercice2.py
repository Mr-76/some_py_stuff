def cumsum(list1):
    total = 0
    cumsum_list = []
    for item in list1:
        total+= item
        cumsum_list.append(total) 
    print(cumsum_list)




def main():
    test_list = [1,2,3]
    cumsum(test_list)

if __name__ == "__main__":
    main()

