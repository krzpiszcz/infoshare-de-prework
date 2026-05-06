### Info
# list       # ordered, mutable
# set        # unordered, mutable
# tuple      # ordered, immutable
# dictionary # ordered, mutable (*key cannot be mutable)

### common translation
# list = shopping list → you can change it, and order matters
# set = bag of unique items → you can add/remove, but no fixed order
# tuple = locked list → order matters, but you can’t change it
# dictionary = real dictionary → word → meaning pairs, and you can update entries

my_list = [1, 2, 3]
my_list[0] = 9

my_set = {1, 2, 3}
my_set.add(4)

my_tuple = (1, 2, 3)
# can't change items

my_dict = {"name": "Ana", "age": 20}
my_dict["age"] = 21
