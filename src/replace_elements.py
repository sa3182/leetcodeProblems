class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        for i in range(len(arr)-1,-1,-1):
            current_element = arr[i]
            arr[i]=right_max
            if current_element> right_max:
                right_max = current_element
        return arr