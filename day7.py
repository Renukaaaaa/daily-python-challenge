def trap(height):
    total_water = 0
    n = len(height)
    
    for i in range(n):
        left_max = max(height[:i+1])
        right_max = max(height[i:])
        total_water += min(left_max, right_max) - height[i]
    
    return total_water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  
