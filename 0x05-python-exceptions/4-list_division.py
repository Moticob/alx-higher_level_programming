#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0  # Initialisation de l'indice
    while i < list_length:
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
            i += 1  # Incrémentation de l'indice

# Exemple d'utilisation
list1 = [10, 20, 30]
list2 = [2, 0, 10]
length = len(list1)
list_division(list1, list2, length)
print(new_list)
