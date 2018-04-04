def findCategory(frame, x):
    newFrame = frame
    items = []
    for a in x:
        items.append(a)
        
    for i in range(len(items)):
        newFrame = newFrame[newFrame['categories'].str.contains(items[i])]
        
    return newFrame