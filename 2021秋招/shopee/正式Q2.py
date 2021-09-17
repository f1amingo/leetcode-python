def solute(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] <= nums[i + 1]:
        i -= 1
    if i < 0:
        return '0'
    j = len(nums) - 1
    while j > i and nums[i] <= nums[j]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    lt, rt = i + 1, len(nums) - 1
    while lt < rt:
        nums[lt], nums[rt] = nums[rt], nums[lt]
        lt += 1
        rt -= 1
    if len(nums) > 0 and nums[0] == '0':
        return '0'
    return ''.join(nums)


print(solute([ch for ch in '100']))
assert solute([ch for ch in '22222']) == '0'
assert solute([ch for ch in '1332']) == '1323'
assert solute([ch for ch in '33321']) == '33312'
# print(solute([ch for ch in input()]))
