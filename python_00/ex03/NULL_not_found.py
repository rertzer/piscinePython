def NULL_not_found(object: any) -> int:

    found = 0

    if object is None:
        print(object, (type(object)))
    elif object != object:
        print("Cheese:", object, (type(object)))
    elif isinstance(object, bool) and object is False:
        print("Fake:", object, (type(object)))
    elif isinstance(object, int) and object == 0:
        print("Zero:", object, (type(object)))
    elif isinstance(object, str) and object == '':
        print("Empty:", object, (type(object)))
    else:
        found = 1
        print("Type not Found")
    return found
