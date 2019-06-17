def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    answer = []
    index_mid = 0
    mid = target/2
    for item in nums:
        if mid < item:
            index_mid = nums.index(item)

    left_index = index_mid
    right_index = index_mid

    def left_(nums, left_index):
        return nums[left_index]

    def right_(nums, right_index):
        return nums[right_index]

    while True:
        left = left_(nums, left_index)
        right = right_(nums, right_index)

        if left + right > target:
            left_index -= 1
        elif left + right < target:
            right_index += 1
        else:
            answer.append(left_index)
            answer.append(right_index)
    return answer
    
