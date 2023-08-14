import heapq
from typing import List
from collections import defaultdict

def topKFrequent(words: List[str], k: int) -> List[str]:

    class PriorityWord(str):
        def __new__(cls, word: str, priority: int):
            instance = super().__new__(cls, word)
            instance.priority = priority
            return instance    

        def __lt__(self, other):
            return self.priority < other.priority or (self.priority == other.priority and self > other)

    priorityWords = defaultdict(int)
    for w in words:
        if w in priorityWords:
            priorityWords[w] = priorityWords[w] + 1
        else:
            priorityWords[w] = 1
    
    priorityWordsList = [PriorityWord(k, v) for k,v in priorityWords.items()]
    
    heapq._heapify_max(priorityWordsList)
    if k == 1:
        output = heapq.heappop(priorityWordsList)
    else:
        output = heapq.nlargest(k, priorityWordsList)


    return output

words = ["i","love","leetcode","i","love","coding"]
words = ["plpaboutit","jnoqzdute","sfvkdqf","mjc","nkpllqzjzp","foqqenbey","ssnanizsav","nkpllqzjzp","sfvkdqf","isnjmy","pnqsz","hhqpvvt","fvvdtpnzx","jkqonvenhx","cyxwlef","hhqpvvt","fvvdtpnzx","plpaboutit","sfvkdqf","mjc","fvvdtpnzx","bwumsj","foqqenbey","isnjmy","nkpllqzjzp","hhqpvvt","foqqenbey","fvvdtpnzx","bwumsj","hhqpvvt","fvvdtpnzx","jkqonvenhx","jnoqzdute","foqqenbey","jnoqzdute","foqqenbey","hhqpvvt","ssnanizsav","mjc","foqqenbey","bwumsj","ssnanizsav","fvvdtpnzx","nkpllqzjzp","jkqonvenhx","hhqpvvt","mjc","isnjmy","bwumsj","pnqsz","hhqpvvt","nkpllqzjzp","jnoqzdute","pnqsz","nkpllqzjzp","jnoqzdute","foqqenbey","nkpllqzjzp","hhqpvvt","fvvdtpnzx","plpaboutit","jnoqzdute","sfvkdqf","fvvdtpnzx","jkqonvenhx","jnoqzdute","nkpllqzjzp","jnoqzdute","fvvdtpnzx","jkqonvenhx","hhqpvvt","isnjmy","jkqonvenhx","ssnanizsav","jnoqzdute","jkqonvenhx","fvvdtpnzx","hhqpvvt","bwumsj","nkpllqzjzp","bwumsj","jkqonvenhx","jnoqzdute","pnqsz","foqqenbey","sfvkdqf","sfvkdqf"]

k = 1
output = topKFrequent(words, k)
print(output)