def countOdds(low, high):
    if low%2 == 0 and high%2== 0: 
        print((high-low)//2)
        
    else:
        print((high-low)//2 + 1)


countOdds(3, 7)