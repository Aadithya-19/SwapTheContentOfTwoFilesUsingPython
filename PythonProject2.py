def swap():

    i1 = (input("Enter the first file you want to swap: "))
    i2 = (input("Enter the second file you want to swap: "))

    file_1 = (i1, 'r')
    file_2 = (i2, 'r')
    file_1 = (i1, 'w')
    file_2 = (i2, 'w')

    with open(i1, 'r') as a:
        data_a = a.read()

    with open(i2, 'r') as b:
        data_b = b.read()

    with open(i1, 'w') as a:
        a.write(data_b)

    with open(i2, 'w') as b:
        b.write(data_a)


    print("The two given files have been swapped")

swap()