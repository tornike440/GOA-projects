def no_space(x):
    for i in range(len(x)):
        if x[i] == " ":
            x.pop(i)
    return x