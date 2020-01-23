def madlibs():
    one = input("adjustive: ")
    two = input("adjustive: ")
    three = input("adjustive: ")
    if one.isalpha() and two.isalpha() and three.isalpha():
        print(f"A {one} program, a {two} design, together they make a {three} project.")
    else:
        print("no")

madlibs()