def select_sort(unsorted_list):
  
  for i in range(len(unsorted_list) - 1):
    min_index = i
    for j in range(i + 1, len(unsorted_list)):
      if unsorted_list[j] < unsorted_list[min_index]:
        min_index = j

    unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]

return unsorted_list
#USING unsorted_list = [14,27,8,42,11,35,-9,56,23] to implement the sort algorithm above
    unsorted_list = [14, 27, 8, 42, 11, 35, -9, 56, 23]
    sorted_list = select_sort(unsorted_list)

    print(sorted_list)

# THE COMPLEXITY CLASS =  O(n^2)


def insert_sort(unsorted_list):
  
  for i in range(1, len(unsorted_list)):
    current_element = unsorted_list[i]
    j = i - 1
    while j >= 0 and unsorted_list[j] > current_element:
      unsorted_list[j + 1] = unsorted_list[j]
      j -= 1

    unsorted_list[j + 1] = current_element

  return unsorted_list


# SORTING PROCESS FOR THE unsorted_list = [14,27,8,-42,11,35,-9,56,23] using the sort algorith above

unsorted_list = [14, 27, 8, 42, 11, 35, -9, 56, 23]
sorted_list = insert_sort(unsorted_list)

print(sorted_list)

#  THE COMPLEXITY CLASS = O(n^2)
