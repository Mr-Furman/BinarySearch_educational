class BinarySearch:
    def __init__(self, array) -> None:
        self.array = array
    
    def search(self, target) -> int:
        min:int  = 0
        max:int =  len(self.array ) - 1 
        while min <= max:
            middle = (min + max) // 2
            if self.array[middle] == target:
                return middle
            elif self.array[middle]< target:
                min = middle + 1
            else:
                max = middle -1 
        return -1


list_with_data: list  = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
test_1 = BinarySearch(list_with_data)
print(test_1.search(4))
