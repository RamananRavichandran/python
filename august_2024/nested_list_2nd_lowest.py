#still one test case to solve

if __name__ == '__main__':
    nested_ls, names, numbers = [[]], [], []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp_ls = [name, score]
        nested_ls.append(temp_ls)

    nested_ls1 = nested_ls[1:]
    i = 0
    while i < len(nested_ls1):
        for index in range(len(nested_ls1) - 1):
            if nested_ls1[index][1] > nested_ls1[index + 1][1]:
                temp_ls = nested_ls1[index]
                nested_ls1[index] = nested_ls1[index + 1]
                nested_ls1[index + 1] = temp_ls
            numbers.append(nested_ls1[index][1])
        i += 1

    ns = list(set(numbers))
    ns.sort()
    sec_lar = ns[1]

    for ls in nested_ls1:
        if ls[1] == sec_lar:
            names.append(ls[0])
    names.sort()
    for i in names:
        print(i)
