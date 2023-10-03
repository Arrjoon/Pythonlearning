def play(*args, **kwargs):
    for key, arg in kwargs:
        print(arg)


a = play(abc=12)
