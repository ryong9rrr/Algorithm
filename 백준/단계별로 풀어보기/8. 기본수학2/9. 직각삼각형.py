import sys
input = sys.stdin.readline

while(True) :
    nums = sorted(map(int, input().split()))

    if(max(nums) == 0) :
        break    

    print("right") if nums[0]**2 + nums[1]**2 == nums[2]**2 else print("wrong")