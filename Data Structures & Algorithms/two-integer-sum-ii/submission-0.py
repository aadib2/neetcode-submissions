class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # can use two pointers technique where front = 0 and back = len - 1
        # check each pair and control pointers

        front = 0
        back = len(numbers) - 1

        while front < back:
            curr_sum = numbers[front] + numbers[back]

            if curr_sum == target:
                return [front + 1, back + 1]
            
            # take advantage of the array being sorted by checking if calc sum is > or <
            if curr_sum < target:
                # if the sum is less than target, increment front so it can be larger
                front+=1
            else: # if sum is then > target, then decrement back
                back-=1