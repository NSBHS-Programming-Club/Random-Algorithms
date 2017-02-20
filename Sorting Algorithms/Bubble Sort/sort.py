# I don't know why it is in a class either

class buble:
    unsorted_arary = [7, 321, 1321, 3, 92, 100, 61]
    is_sorted = True

    def __init__(self):
       isSorted = False 

    def check_sorted(self, array_checked = []):
        for x in range(1, len(array_checked)):
            if array_checked[x-1] > array_checked[x]:
                return False
        return True

    def sort(self, array_to_sort = []):
        for x in range(1, len(array_to_sort)):
            if array_to_sort[x-1] > array_to_sort[x]:
                array_to_sort[x-1], array_to_sort[x] = array_to_sort[x], array_to_sort[x-1]
                print (str(array_to_sort[x-1])+" Swapped With "+str(array_to_sort[x]))
        if self.check_sorted(array_to_sort) :
            return 0
        else:
            self.sort(array_to_sort)

michael = buble()
michael.sort(michael.unsorted_arary)
for x in michael.unsorted_arary:
    print(x)

