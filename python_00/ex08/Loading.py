def ft_tqdm(lst):
    """
    Decorate an iterable object, returning an iterator.
    And print a progess bar every time a value is requested.
    """
    maxi = len(lst)
    i = 0
    for item in lst:
        i += 1
        progress = i / maxi * 100
        bar = ''
        barsize = int(progress / 2)
        for x in range(barsize):
            bar += '='
        bar += '>'
        print("{:>3d}%|[{:<51}]| {:>3d}/{:>3d}".format(int(progress),
              bar, i, maxi), end='\r')
        yield item
