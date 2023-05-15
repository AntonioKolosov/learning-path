"""

"""


def make_a_list(l):
    """"""
    while True:
        for i in l:
            if i.startswith("m"):
                l.remove(i)
                return [i for i in l if not i.startswith("m")]


def main():
    words = input("Input your words: ").strip()
    list = words.split()
    result = make_a_list(list)
    print(result)


if __name__ == "__main__":
    main()