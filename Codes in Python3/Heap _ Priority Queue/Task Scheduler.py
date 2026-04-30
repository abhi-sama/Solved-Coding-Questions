class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for c in tasks:
            freq[ord(c) - ord("A")] += 1

        freq.sort()

        maxi = freq[25]
        holes = maxi - 1
        idle_spots = n * holes

        for i in range(24, -1, -1):
            idle_spots -= min(holes, freq[i])

        if idle_spots > 0:
            return len(tasks) + idle_spots


        return len(tasks)


# TC=O(m). m is the no of tasks
# SC=O(1)
