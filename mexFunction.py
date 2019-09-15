def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break

    else:
        found = upperBound

    return found

if __name__ == "__main__":
    s = [0, 4, 2, 3, 1, 7]
    upperBound = 3
    print(mexFunction(s, upperBound))
