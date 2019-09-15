def baseConversion(n, x):
    return hex(int(n,x))[2:]

if __name__ == "__main__":
    n = "1302"
    x = 5
    print(baseConversion(n, x))
