def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")


happy_new_year()

happy_new_year(False)

value = None
if value is None:
    print("Sorry, you don't carry any value")

print(strange_function(2))
print(strange_function(1))


def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s


print(list_sum([5, 4, 3]))

