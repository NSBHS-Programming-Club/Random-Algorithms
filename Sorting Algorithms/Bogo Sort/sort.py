# I know right? Bogo Sort. What a disgusting thing to consider
import random as bogo

class norris:
    first_name = "Jackie"
    unsorted_array = [2, 1, 5, 8, 7]

    #Don't even need a constructor but im hipster so here it is
    def __init__(self):
        first_name = "Chuck"

    def sort(self, array_to_sort=[]):
        if self.check_sorted(array_to_sort):
            return 0
        else:
            bogo.shuffle(array_to_sort)
            
            if self.check_sorted(array_to_sort):
                return 0
            else:
                for x in array_to_sort:
                    print(str(x)+"\n")
                self.sort(array_to_sort)
        
    def check_sorted(self, array_checked = []):
        for x in range(1, len(array_checked)):
            if array_checked[x-1] > array_checked[x]:
                return False
        return True

chuck = norris()
chuck.sort(chuck.unsorted_array)
for x in chuck.unsorted_array:
        print(str(x))
