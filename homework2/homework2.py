#Să se scrie o funcție care primește un număr nedefinit de parametrii și
# să se calculeze suma parametrilor care reprezintă numere întregi sau reale.
#○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
#○ your_function() va returna 0.
#○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4)
def first_function(*args, **kwargs):
    a = [x for x in args if type(x)==int ]
    print(sum(a))
print(first_function())
print(first_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(first_function(2, 4, 'abc', param_1=2))

# Să se scrie o funcție recursivă care primește ca parametru un număr întreg și returnează:
#○ suma tuturor numerelor de la [0, n]
#○ suma numerelor pare de la [0, n]
#○ suma numerelor impare de la [0. n]
def second_function(n):
    if n == 0:
        return 0
    return n + second_function(n-1)
print(second_function(5))


#Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este
# un număr întreg, altfel returnează valoarea 0.
def third_function():
    your_number = input('Insert you number, please.')
    try:
        if int(your_number):
            print(your_number)
    except ValueError:
        print(0)
third_function()



