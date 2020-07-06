def my_hash(s):
    sb = s.encode()
    total = 0
    for b in sb:
        total += b
    return total % 8


i = my_hash("parth")
hash_table = [None]*8
hash_table[i] = "8 months"
# hash parth
# retrieve value at that hash


def get_length_timeatlambda(e):
    curr_hash = my_hash(e)
    return hash_table[curr_hash]


length_parth = get_length_timeatlambda("parth")
print("Parth has worked at Lambda for " + length_parth)
employees = {}
