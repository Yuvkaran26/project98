def project():
    file1 = input("Enter the file name: ")
    file2 = input("Enter the file name: ")

    # file_a = open(file1, "r")
    # file_a.read()

    # file_b = open(file2, "r")
    # file_b.read()

    # file_a = open(file2, "w")
    # file_a.write(file2)

    # file_b = open(file1, "w")
    # file_b.write(file1)

    with open(file1, "r") as file_a:
        data_a = file_a.read()

    with open(file2, "r") as file_b:
        data_b = file_b.read()

    with open(file1, "w") as file_a:
        file_a.write(data_b)

    with open(file2, "w") as file_b:
        file_b.write(data_a)
        
project()