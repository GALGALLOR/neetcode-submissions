class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_row = 0
        last_row = len(matrix)-1
        i = 0
        j = len(matrix[0])-1

        while last_row>=start_row and j>=i:
            curr_row = start_row+(last_row-start_row)//2
            mid = i+(j-i)//2
            if matrix[curr_row][0]>target:
                last_row = curr_row-1
            elif matrix[curr_row][-1]<target:
                start_row = curr_row+1
            else:
                if matrix[curr_row][mid]==target:
                    return True
                elif matrix[curr_row][mid]>target:
                    j = mid-1
                else:
                    i = mid+1
        return False