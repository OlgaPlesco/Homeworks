#Crea?i un script Python care îndepline?te următoarele func?ii:

# declară o listă care con?ine elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
# afi?ează lista ini?ială ordonată ascendent (lista ini?ială trebuie păstrată în aceea?i formă)
my_list_sorted_asc = sorted(my_list)
# afi?ează lista ini?ială ordonată descendent (lista ini?ială trebuie păstrată în aceea?i formă)
my_list_sorted_desc = my_list_sorted_asc[::-1]
# afi?ează o listă ce con?ine numerele pare din lista ordonată (folosind slice)
even_numbers = my_list_sorted_desc[::2]
# afi?ează o listă ce con?ine numerele impare din lista ordonată (folosind slice)
odd_numbers = my_list_sorted_asc[::2]
# afisează o listă ce con?ine numerele ce sunt multipli ai numărului 3 (folosind slice).
other_numbers = my_list_sorted_asc[2::3]
print(my_list)
print(my_list_sorted_asc)
print(my_list_sorted_desc)
print(even_numbers)
print(odd_numbers)
print(other_numbers)
