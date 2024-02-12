import time as time

elapsed = time.time()
date = time.strftime("%b %d %Y")

print("Seconds since January 1, 1970: {:,.4f} or {:.2e}  in scientific notation".format(elapsed, elapsed))
print(date)
