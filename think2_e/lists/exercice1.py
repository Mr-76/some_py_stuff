def nested_sum(lists_of_lists):
    final_sum = 0;
    for element in lists_of_lists:
        final_sum += sum(element);
    return final_sum
def main():
    list1 = [[1,2],[3],[4,5,6]];
    print(nested_sum(list1))
if __name__ == '__main__':
    main();
