recurrence_dict = {
'current_location': 'Usa',
'job': 'sofware engineer',
'older_location': 'Canada'
}
print("Before popping: ", recurrence_dict)
# Lets remove the last item
recurrence_dict.popitem() #pop method in dictionary is used to pop key values
print("After popping: ", recurrence_dict)

l1=["hello","world","popping"]
l1.pop() # here in this l1 list if pop method is used it pops the last item because no index is provided 
print(l1)
print(l1.pop(0)) #if the index is given it shows what element is popped
print(l1)