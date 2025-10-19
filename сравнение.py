import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


def bubble_sort(nums):
    k = 0
    logging.info('bubble_sort_svetlana')
    swapped = True
    while swapped:
        k += 1
        swapped = False
        for i in range(len(nums) - 1):
            k += 1
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    logging.info(f'iteration = {k}')
    logging.info('k/bubble/svetlana')


import random

alex = [random.randint(0, 1000) for i in range(5000)]
bubble_sort(alex)
print(alex)


def selection_sort(nums):
    k = 0
    logging.info('sasa')
    for i in range(len(nums)):
        k += 1
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            k += 1
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    logging.info(f'iteration2 = {k}')
    logging.info('sasa')


alex1 = [random.randint(0, 1000) for i in range(5000)]
selection_sort(alex1)

print(alex1)#3 cек.24200000


def insertion_sort(nums):
    k = 0
    logging.info('milasa')
    for i in range(1, len(nums)):
        k += 1
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            k += 1
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
    logging.info(f'iteration3 = {k}')
    logging.info('milasa')


alex2 = [random.randint(0, 1000) for i in range(5000)]
insertion_sort(alex2)
print(alex2)#2 сек.12502500


def heapify(nums, heap_size, root_index):
    logging.info('heapify')
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)
    logging.info('heapify')


def heap_sort(nums):
    logging.info('dasa1')
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    logging.info('dasa1')


alex3 = [random.randint(0, 1000) for i in range(5000)]
heap_sort(alex3)
print(alex3)#4 cек.6274955



def merge(left_list, right_list):
    k=0
    logging.info('boba.alex')
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        k+=1
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    logging.info('boba.alex')

    return sorted_list


def merge_sort(nums):
    k=0
    logging.info('alex')
    if len(nums) <= 1:
        k+=1
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    logging.info('alex')
    return merge(left_list, right_list)


alex4 = [random.randint(0, 1000) for i in range(5000)]
alex4 = merge_sort(alex4)
print(alex4) #1сек



def partition(nums, low, high):
    k=0
    logging.info('aleks')
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        k+=1
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j
        logging.info('aleks')

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    logging.info('quick sort')
    def _quick_sort(items, low, high):
        logging.info('an info')
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    logging.info('quick sort')
    logging.info('an info')

    _quick_sort(nums, 0, len(nums) - 1)

alex5 = [random.randint(0, 1000) for i in range(5000)]
quick_sort(alex5)
print(alex5) #2 сек.очень много интераций
