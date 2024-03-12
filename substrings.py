def sub(x):
    a = []
    for i in range(len(x)):
        for j in range(i + 1, len(x) + 1):
            a.append(x[i:j])
    print(a)


sub([1, 2, 3, 4])