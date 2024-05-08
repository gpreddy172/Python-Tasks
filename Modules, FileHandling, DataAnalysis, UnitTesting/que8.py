original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict_1 = {k: ('old' if v > 40 else 'young')
 for (k, v) in original_dict.items()}
#here if the key contains values greater than 40 are changed to old and keys containing values less than 40 are changed to young
#the for loop is used to iterate on the keys
print(new_dict_1)