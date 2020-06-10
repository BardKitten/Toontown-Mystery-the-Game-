categories = ['foul-language', 'greening', 'rude-behavior', 'bad-name', 'hacking']

def isValidCategory(value):
    return value < len(categories)

def isValidCategoryName(value):
    return value in categories

def getCategory(value):
    return categories[value]
