'''
Given two sorted lists of integers. 
Implement a function that merges them such that the resulting list is still sorted.
For example, 
considering a list A of [2, 5, 6, 9, 11] and a list B of [1, 1, 3, 5, 8], the resulting list should be [1, 1, 2, 3, 5, 5, 6, 8, 9, 11].

listA[i] is int
'''

class ListsHelper:
    def mergeLists(self, listA, listB):
        lenA = len(listA)
        lenB = len(listB)

        if lenA == 0:
            return listB
        if lenB == 0:
            return listA

        res = []
        aPointer, bPointer = 0, 0
        while aPointer < lenA and bPointer < lenB:
            if listA[aPointer] <= listB[bPointer]:
                res.append(listA[aPointer])
                aPointer += 1
            elif listA[aPointer] > listB[bPointer]:
                res.append(listB[bPointer])
                bPointer += 1

        if aPointer < lenA:
            [res.append(v) for v in listA[aPointer:]]
        
        if bPointer < lenB:
            [res.append(v) for v in listB[bPointer:]]
        
        return res

if __name__ == "__main__":
    listsHelper = ListsHelper()
    #output = listsHelper.mergeLists([2, 5, 6, 9, 11], [1, 1, 3, 5, 8])
    # passed
    #output = listsHelper.mergeLists([2, 5, "hello fresh", 9, 11], [1, 1, 3, 5, 8])
    # passed
    output = listsHelper.mergeLists([], [1, 1, 3, 5, 8])
    # passed
    
    #expectedResult = [1, 1, 2, 3, 5, 5, 6, 8, 9, 11]
    expectedResult = [1, 1, 3, 5, 8]


    if output == expectedResult:
        print(f"Merge was successful with the result being: {output}")
    else:
        print("Merge was unsuccessful")