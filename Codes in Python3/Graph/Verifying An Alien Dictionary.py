
# Pseudocode:-
# 1)Create a hashmap of of the dictionary order with the letters and its index in the 
# order.
# 2)For each word in the words list check if the order is followed, if not followed return false,
# otherwise return true.


# Approach 1
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index={c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            w1,w2= words[i],words[i+1]

            for j in range(len(w1)):
                if j==len(w2):
                    return False
                    
                if w1[j]!=w2[j]:
                    if(order_index[w1[j]]>order_index[w2[j]]):
                        return False
                    break
        return True

