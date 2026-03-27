# Anagram program (without using built-in sort)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# convert to lowercase
str1 = str1.lower()
str2 = str2.lower()

# check length first
if len(str1) != len(str2):
    print("Not an Anagram")
else:
    # convert to list
    list1 = list(str1)
    list2 = list(str2)

    # manual sorting (bubble sort)
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] > list1[j]:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp

    for i in range(len(list2)):
        for j in range(i + 1, len(list2)):
            if list2[i] > list2[j]:
                temp = list2[i]
                list2[i] = list2[j]
                list2[j] = temp

    # compare lists
    if list1 == list2:
        print("Anagram")
    else:
        print("Not an Anagram")