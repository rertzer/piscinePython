import time as time

elapsed = time.time()
date = time.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {elapsed:,.4f}", end=' ')
print(f"or {elapsed:.2e} in scientific notation")
print(date)
