def foobar_test():
    for i in range(1,1000):
        if i%10 == 0:
            pass
        elif i%3 == 0 and i%5 == 0:
            print("foo-bar")
        elif i%3 == 0:
            print("foo")
        elif i%5 == 0:
            print("bar")
        else:
            print(i)

def main():
    foobar_test()

if __name__ == "__main__":
    main()