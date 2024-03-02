def remove_element(lst, element):
    count = 0
    while element in lst:
        lst.remove(element)
        count += 1
    return count

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element_to_remove = 5

removed_count = remove_element(my_list, element_to_remove)
print(f"تعداد {element_to_remove} حذف شده: {removed_count}")
print("لیست پس از حذف:")
print(my_list)

#FATEMEH REZAEI
