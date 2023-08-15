

def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    # Struggled with this problem for a long while.
    # Idea: Two pointers: moving end forward to find a valid window,
    #                     moving start forward to find a smaller window
    #                     counter and hash_map to determine if the window is valid or not

    # Count the frequencies for chars in t
    hash_map = dict()
    for c in t:
        if c in hash_map:
            hash_map[c] += 1
        else:
            hash_map[c] = 1

    start, end = 0, 0

    # If the minimal length doesn't change, it means there's no valid window
    min_window_length = len(s) + 1

    # Start point of the minimal window
    min_window_start = 0

    # Works as a counter of how many chars still need to be included in a window
    num_of_chars_to_be_included = len(t)

    while end < len(s):
        # If the current char is desired
        if s[end] in hash_map:
            # Then we decreased the counter, if this char is a "must-have" now, in a sense of critical value
            if hash_map[s[end]] > 0:
                num_of_chars_to_be_included -= 1
            # And we decrease the hash_map value
            hash_map[s[end]] -= 1

        # If the current window has all the desired chars
        while num_of_chars_to_be_included == 0:
            # See if this window is smaller
            if end - start + 1 < min_window_length:
                min_window_length = end - start + 1
                min_window_start = start

            # if s[start] is desired, we need to update the hash_map value and the counter
            if s[start] in hash_map:
                hash_map[s[start]] += 1
                # Still, update the counter only if the current char is "critical"
                if hash_map[s[start]] > 0:
                    num_of_chars_to_be_included += 1

            # Move start forward to find a smaller window
            start += 1

        # Move end forward to find another valid window
        end += 1

    if min_window_length == len(s) + 1:
        return ""
    else:
        return s[min_window_start:min_window_start + min_window_length]
    

print(minWindow(s = "ADOBECODEBANC", t = "ABC"))



# the following is also easy to understand
from collections import Counter
def minWindow2(s: str, t: str) -> str:
    # Count number of occurrences of each character from target string.
    t=Counter(t)   
    
    #This will store number of unique characters in target string e.g "aba": 2, "abc": 3
    count=len(t)    
    
    # Sliding window initialization
    i, j=0, 0  
    
    # Minimum size of the window where all characters from target string are found
    mini_window=float('inf')  
    
    # Return answer
    mini_word=""
    
    while j < len(s):
    
        # The following loop will run till we get all occourences of target characters in the window
        # size of s[i: j], this is indicated if the count hits 0.
        while j < len(s) and count != 0:  
            if s[j] in t:
                t[s[j]] -= 1
                if t[s[j]] == 0:
                    count -= 1
            j += 1
        
        # Now since we have a window from s[i: j] containing all characters from target string.
        # We will try to reduce the string until one character goes missing
        # And concurrently store the minimum string containing all characters from traget string.
        while i <= j and count==0:
            if mini_window > j-i:
                mini_word=s[i: j]
                mini_window = j-i # j-i is minimum window size.

            if s[i] in t:
                t[s[i]] += 1
                
                if t[s[i]] >=1:
                    count += 1    
            i += 1
    
    # Finally return the answer we received
    return mini_word

print(minWindow2(s = "ADOBECODEBANC", t = "ABC"))
