from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def findPathValues(start, dest) -> int:
            for i, e in enumerate(equations):
                if (e[0], e[1]) in visited:
                    continue 
                if start in e:
                    if start == dest:
                        return 1   
                    visited.add((e[0], e[1]))
                    if start == e[0]:
                        value = values[i]
                        secondElement = e[1]
                    else:
                        value = 1/values[i]
                        secondElement = e[0]
                    if dest in e:         
                        return value        
                    subvalue = findPathValues(secondElement, dest)
                    if subvalue != -1:
                        return value * subvalue
            return -1

        output = []
        for q in queries:
            visited = set()
            start = q[0]
            dest = q[1]
            output.append(findPathValues(start, dest))
        return output
                                                                    

# previous code, not working 100%
# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

#         def findPathValues(start, dest, visited):
#             if (start, dest) in visited:
#                 return                 
                            
#             for i, e in enumerate(equations):
#                 if (e[0],e[1]) in visited:
#                     continue 
#                 if start in e:
#                     visited.add((e[0],e[1]))
#                     if start == dest:
#                         targetValues.append(1)
#                         found.append(True)
#                         return
#                     secondElement = None          
#                     if start == e[0]:
#                         targetValues.append(values[i])
#                         secondElement = e[1]
#                     else:
#                         targetValues.append(1/values[i])
#                         secondElement = e[0]                      
#                     if dest in e:
#                         found.append(True)
#                         return
#                     findPathValues(secondElement, dest, visited)

#         found = []
#         targetValues = []
#         output = []
#         for q in queries:
#             found = []
#             targetValues = []
#             visited = set()

#             start = q[0]
#             dest = q[1]
#             findPathValues(start, dest, visited)
#             print(targetValues)
#             print(found)
#             if len(found) > 0 and len(targetValues) > 0:
#                 product = 1.0
#                 for pv in targetValues:
#                     product *= pv
#                 output.append(product)
#             else:
#                 output.append(-1.0)
#         return output
        
                                    
                
                    


