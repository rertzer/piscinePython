def ft_statistics(*args, **kwargs):
    """Calculate statistics on the args given as arguments."""
    if "mean" in kwargs.values():
        print(f"mean: {ft_mean(args)}")
    if "median" in kwargs.values():
        print(f"median: {ft_median(args)}")
    if "quartile" in kwargs.values():
        print(f"median: {ft_quartile(args)}")


def ft_mean(args):
    """Return the mean of the numbers given as arguments."""
    length = len(args)
    mean = 0
    if (length != 0):
        args_sum = 0
        for n in args:
            args_sum += n
        mean = args_sum / length
    return mean

def ft_median(args):
    """Return the mean of the numbers given as arguments."""
    middle = int((len(args) + 1) / 2) - 1
    args = list(args)
    args.sort()
    median = 0
    if (middle != 0):
        median = args[middle]
    return median


def ft_quartile(args):
    """Return first and third quartile of the numbers given as arguments."""
    
    first = int((len(args) + 3) / 4) - 1
    third = int((3 * len(args) + 1) / 4) - 1


def main():
    """Main test."""
    ft_statistics(toto="mean")
    print("--------------")
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tata="median", titi="quartile")
    print("--------------")
    print("--------------")


if __name__ == "__main__":
    main()
