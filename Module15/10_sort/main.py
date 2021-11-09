# TODO здесь писать код

nums = [1, 4, -3, 0, 10]
print('Изначальный список:', nums)

for i in range(len(nums)):
    for x in range(i, len(nums)):
        if nums[x] < nums[i]:
            nums[x], nums[i] = nums[i], nums[x]

print('\nОтсортированный список:',nums)