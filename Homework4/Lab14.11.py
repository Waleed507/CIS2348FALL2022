# Waleed Yusuf
# 2104654

def selection_sort_descend_trace(list1):
    for i in range(len(list1) - 1):
        maxint = i
        for j in range(i + 1, len(list1)):
            if list1[j] > list1[maxint]:
                maxint = j
        list1[i], list1[maxint] = list1[maxint], list1[i]
        print(' '.join([str(x) for x in list1]), '')
    return list


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)
