def isEven(page):
    if page % 2 == 0:
        return True

def main():
    page = int(input("no of page: "))
    if isEven(page) == True:
        print(page)
    else:
        print("%60s%d" % (" ", page))


main()