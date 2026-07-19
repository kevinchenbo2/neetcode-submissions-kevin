class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch():
            l, r = 0, cols - 1
            
            while l <= r:
                mid =  (r + l) // 2
                if matrix[center][mid] == target:
                    return True
                
                elif target < matrix[center][mid]:
                    r = mid - 1
                
                else:
                    l = mid + 1

            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        top, bottom = 0, rows - 1

        while top <= bottom:
            center = (top + bottom) // 2
            if matrix[center][0] == target or matrix[center][cols - 1] == target:
                return True
            
            elif target < matrix[center][0]:
                bottom = center - 1
            
            elif target > matrix[center][cols - 1]:
                top = center + 1
            else:
                return binarySearch()
        
        return False



        
            