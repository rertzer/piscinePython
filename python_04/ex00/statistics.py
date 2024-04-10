def ft_statistics(*args, **kwargs):
    """Calculate statistics on the args given as arguments."""
    for v in kwargs.values():
        try:
            if v == "mean":
                print(f"mean: {ft_mean(args)}")
            elif v == "median":
                print(f"median: {ft_median(args)}")
            elif v == "quartile":
                print(f"quartile: {ft_quartile(args)}")
            elif v == "std":
                print(f"std: {ft_std(args)}")
            elif v == "var":
                print(f"var: {ft_var(args)}")
        except AssertionError:
            print("ERROR")


def ft_mean(args):
    """Return the mean of the numbers given as arguments."""
    length = len(args)
    if length == 0:
        raise AssertionError("ERROR")
    args_sum = 0
    for n in args:
        args_sum += n
    return args_sum / length


def ft_median(args):
    """Return the mean of the numbers given as arguments."""
    length = len(args)
    if length == 0:
        raise AssertionError("ERROR")
    middle = int((length + 1) / 2) - 1
    args = list(args)
    args.sort()
    median = args[middle]
    return median


def ft_quartile(args):
    """Return first and third quartile of the numbers given as arguments."""
    length = len(args)
    if length == 0:
        raise AssertionError("ERROR")
    first_pos = int((len(args) + 3) / 4) - 1
    third_pos = int((3 * len(args) + 1) / 4) - 1
    args = list(args)
    args.sort()
    first = float(args[first_pos])
    third = float(args[third_pos])
    return (first, third)


def ft_std(args):
    """Return the standard deviation of the numbers given as arguments."""
    length = len(args)
    if length == 0:
        raise AssertionError("ERROR")
    var = ft_var(args)
    return var**(0.5)


def ft_var(args):
    """Return the variance of the numbers given as arguments."""
    length = len(args)
    if length == 0:
        raise AssertionError("ERROR")
    args_squares = 0
    for n in args:
        args_squares += n**2
    var = args_squares / length
    mean = ft_mean(args)
    var -= mean**2
    return var


def main():
    """Main test."""
    ft_statistics(1, 42, 360, 11, 64, pim="mean", pam="median", pum="quartile")
    print("--------------")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("--------------")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
    print("--------------")


if __name__ == "__main__":
    main()
