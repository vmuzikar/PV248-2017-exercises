class CallInspector:
    def __init__(self):
        self.called_times = 0
        self.args_counts = {}
        self.most_used_args = (None, 0)

    def inspect(self, func):
        "this is decorator"
        def decorate(*args, **kwargs):
            self.called_times += 1

            try:
                self.args_counts[args] += 1
            except KeyError:
                self.args_counts[args] = 1
            if self.args_counts[args] >= self.most_used_args[1]:
                self.most_used_args = (args, self.args_counts[args])

            return func(*args, **kwargs)
        return decorate

    def show_call_stats(self):
        "show some call statistics"
        print("Function was called {} times".format(self.called_times))
        print("Most frequently called parameter combinations was: {}, called {} times".format(self.most_used_args[0], self.most_used_args[1]))


inspector = CallInspector()


@inspector.inspect
def fib(n):
    "Return n-th Fibonacci number"
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


# invoke function and show call statistics
print(fib(6))
inspector.show_call_stats()