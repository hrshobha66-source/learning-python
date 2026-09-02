# list mutable (we can change the number)
#marks = [ 99,98,97,96,95]
# print(marks,type(marks))

# # lenght
# print(len(marks))

# #index
# print(marks[0])
# print (marks[-2])

#slicing
# print(marks[0:-3])

# for score in marks:
#     print(score)

# marks.append(56)
# print(marks)

# marks.insert(1,23)
# print(marks)

# print(23 in marks)
# print(96 in marks)


# marks.clear()
# print(marks,len(marks))

#tuples (immutable)
# marks = (98,97,96,93,99)
# print(marks,type(marks))
# print(marks[3])
# print(marks.count(99))
# print(marks.index(98))
# print(marks.index(99))

#set => unique items collection

# marks = {77,34,65,66,65,87,87}
# print(len(marks))

# for score in marks:
#     print(score)

#Dictionary => collection of keys

marks = {"math":99, "physics": 97, "chemistry":98}
# print(marks,type(marks))

# marks["hindi"]= 67
# print(marks["hindi"])
# print(marks["physics"])

for key in marks:
    print(key,marks[key])



