# Write your code here
def drop_nth(xs, n):
    result = xs[:n] + xs[n+1:]
    return result