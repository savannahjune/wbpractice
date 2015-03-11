class Fibber:
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        # edge case: negative index
        if n < 0:
            raise Exception("Index was negative. No such thing as a negative index in a series.")

        # base case: 0 or 1
        elif n in [0,1]:
            return n

        # see if we've already calculated this
        if self.memo.has_key(n):
            return self.memo[n]

        result = self.fib(n-1) + self.fib(n-2)

        # memoize
        self.memo[n] = result

        return result

# Fib iterative:

def fib_iterative(n):

    # edge cases:
    if n < 0:
        raise Exception("Index was negative. No such thing as a negative index in a series.")

    elif n in [0,1]:
        return n

    prev = 0
    prev_prev = 1

    for index in range(n):
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current

# Fib recursive

def fib_recursive(n):
    if n in [1,0]:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)