def mergesortedarray(nums1:list[int],nums2:list[int],m:int,n:int) -> None:
    i = 0
    j = 0
    nums = []
    while (i < m and j < n):
        if (nums1[i]<= nums2[j]):
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1
    while i < m:
        nums.append(nums1[i])
        i += 1

    while j < n:
        nums.append(nums2[j])
        j += 1
    nums1 = nums
    print(nums1)
mergesortedarray([],[2,4,5],0,3)




