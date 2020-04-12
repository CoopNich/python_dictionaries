stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak"
}

purchases = [
    ( 'GM', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GM', 200, '1-jul-1998', 56 )
]


for purchase in purchases:
    for company in stockDict:
        if company == purchase[0]:
            print(f'I purchased {stockDict[company]} stock for ${purchase[1]*purchase[3]}.')



unique = set()

for purchase in purchases:
    unique.add(purchase[0])


for company in unique:
    stock_value = 0
    print(f'----{company}----')
    for purchase in purchases:
        if purchase[0] == company:
            stock_value += purchase[1]*purchase[3]
            print(f'{purchase[1]} shares at {purchase[3]} dollars each on {purchase[2]}')
    print("")
    print(f'Total value of stock ${stock_value}')

            