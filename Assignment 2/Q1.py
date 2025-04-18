def terrain(val):
    return -1 * (val - 7) ** 2 + 49

def climb(limit):
    left, right = 0, limit
    while left < right:
        center = (left + right) // 2
        if terrain(center) < terrain(center + 1):
            left = center + 1
        else:
            right = center
    return right

boundary = 15
summit = climb(boundary)
print("Peak located at:", summit)
print("Height at peak:", terrain(summit))
