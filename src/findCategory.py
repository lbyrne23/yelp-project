def findCategory(*x):
    import pandas as pd
    df = pd.read_csv("../data/raw/yelp_business.csv")
    newFrame = df
    items = []
    for a in x:
        items.append(a)
        
    for i in range(len(items)):
        newFrame = newFrame[newFrame['categories'].str.contains(items[i])]
        
    return newFrame  