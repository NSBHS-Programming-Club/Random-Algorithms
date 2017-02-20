class binarySearch:
    array_to_search = [5, 8, 2, 1, 6, 8, 3, 21, 67, 54]
    
    def search(self, array_to_search, value_to_search):
        array_to_search.sort()
        
        lower_bound = 1
        upper_bound = len(array_to_search) - 1
        x = value_to_search
        number_found = False

        while number_found == False:
            if upper_bound < lower_bound:
                return "Number Does Not Exists"
            midpoint = lower_bound + (upper_bound - lower_bound) / 2

            if array_to_search[midpoint] < value_to_search:
                lower_bound = midpoint + 1
            if array_to_search[midpoint] > x:
                upper_bound = midpoint - 1
            if array_to_search[midpoint] == x:
                number_found = True
                return "Number Found At Index "+str(midpoint)+" Of Sorted Array"



binary = binarySearch()
print(binary.search(binary.array_to_search, 8))
