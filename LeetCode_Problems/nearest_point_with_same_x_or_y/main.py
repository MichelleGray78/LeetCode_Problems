def nearestValidPoint(x, y, points):
    # if x matches left side of any of the points its valid
    # if y matches right side of any of the points its valid
    # Manhatten distance is abs(x)
    smallest_seen = float('inf')
    index = -1
    for i, (a, b) in enumerate(points):
        print(i, a, b)
        print(points)
        if x == a or y == b:
            if abs(x - a) + abs(y - b) < smallest_seen:
                smallest_seen = abs(x - a) + abs(y - b)
                index = i
    return index
                  
            


nearestValidPoint(3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]])