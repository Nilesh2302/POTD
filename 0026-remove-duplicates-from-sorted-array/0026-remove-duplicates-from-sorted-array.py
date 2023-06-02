class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        N = len(arr)
        i = 0
        for j in range(N):
            if arr[j] != arr[i]:
                i += 1
            arr[i] = arr[j]
        return i + 1

        