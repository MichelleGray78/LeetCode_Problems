def maxProfit(prices):
    highest_sale_price = prices[-1]
    highest_profit = 0
    for number in reversed(prices):
        if number > highest_sale_price:
            highest_sale_price = number
        elif highest_profit < highest_sale_price - number:
            highest_profit = highest_sale_price - number
    print(highest_profit)

maxProfit([7,1,5,3,6,4])