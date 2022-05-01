def twoSum(self, nums: list[int], target: int) -> list[int]:
    prev_map = {} # value : index
    for i,n in enumerate(nums): # index, value
        diff = target - n
        # Builidng hash map as we go along, if diff exists
        # for current n value, return indices of diff and n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return

