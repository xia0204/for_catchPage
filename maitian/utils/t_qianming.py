
i = 3
def t():
    i = 5
    def test():

        # for i in range(20):
        #     # nolocal i
        nonlocal i
        print(i)
    return test()
t()