

str="12 45 63 26 87 345 09 75 14 35 87 11 32 00 43 87"
test=str.split(" ")
test
['12', '45', '63', '26', '87', '345', '09', '75', '14', '35', '87', '11', '32', '00', '43', '87']
test.sort()
test
['00', '09', '11', '12', '14', '26', '32', '345', '35', '43', '45', '63', '75', '87', '87', '87']
int_test = [int(x) for x in test]
int_test
[0, 9, 11, 12, 14, 26, 32, 345, 35, 43, 45, 63, 75, 87, 87, 87]
int_test.sort()
int_test
[0, 9, 11, 12, 14, 26, 32, 35, 43, 45, 63, 75, 87, 87, 87, 345]
int_test.sort(reverse=True)
int_test
[345, 87, 87, 87, 75, 63, 45, 43, 35, 32, 26, 14, 12, 11, 9, 0]
int_test.sort()
int_test
[0, 9, 11, 12, 14, 26, 32, 35, 43, 45, 63, 75, 87, 87, 87, 345]
number=int(input("insert number "))

def binary_search_3(original_list, element, left, right):
    if left>right:
        return False
    middle=(left+right)//2
    if middle>=right:
        return False
    if original_list[middle]<element and original_list[middle+1]>=element:
        return middle
    elif element<original_list[middle]:
        return binary_search_3(original_list, element, left, middle-1)
    else:
        return binary_search_3(original_list, element, middle+1, right)

print(binary_search_3(int_test, number, 0, len(int_test)-1))
