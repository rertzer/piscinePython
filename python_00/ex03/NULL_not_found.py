def NULL_not_found(object: any) -> int:
    
    found = 1

    if object == None:
        print(object, (type(object)))
        found = 0
    elif object != object:
        found = 0
        print("Cheese:", object, (type(object)))
    elif isinstance(object, bool) and object == object:
        found = 0
        print("Fake:", object, (type(object)))
    elif isinstance(object, int) and object == 0:
        found = 0
        print("Zero:", object, (type(object)))
    elif isinstance(object, str) and object == '':
        found = 0
        print("Empty:", object, (type(object)))
    else:
        found = 1
        print("Type not Found")
    return found

