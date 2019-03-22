# generating randomized alphanumeric code of length 6
def group_id(size=6, chars=(string.ascii_uppercase+string.digits)):
    return ''.join(random.choice(chars) for _ in range(size))

# testing function
print(group_id(3))
print(group_id())
print(group_id(10))