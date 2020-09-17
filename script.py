values = [2.0, 3.0]
equations = [["a", "b"], ["b", "c"]]

for (a, b), v in zip(equations, values):
    print(a, b, v)
