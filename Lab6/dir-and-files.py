# Exercise 1
import os


def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]


def list_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


def list_all(path):
    return os.listdir(path)


path = '/path/to/directory'

print("Directories:")
print(list_directories(path))

print("\nFiles:")
print(list_files(path))

print("\nAll:")
print(list_all(path))

# Exercise 2
import os


def check_access(path):
    print(f"Checking access for {path}:\n")

    if os.path.exists(path):
        print(f"The path {path} exists.\n")
    else:
        print(f"The path {path} does not exist.\n")
        return

    if os.access(path, os.R_OK):
        print(f"The path {path} is readable.\n")
    else:
        print(f"The path {path} is not readable.\n")

    if os.access(path, os.W_OK):
        print(f"The path {path} is writable.\n")
    else:
        print(f"The path {path} is not writable.\n")

    if os.access(path, os.X_OK):
        print(f"The path {path} is executable.\n")
    else:
        print(f"The path {path} is not executable.\n")


path = '/path/to/directory'
check_access(path)

# Exercise 3
import os


def check_path(path):
    if os.path.exists(path):
        print(f"The path {path} exists.")
        directory, filename = os.path.split(path)
        print(f"The directory is: {directory}")
        print(f"The filename is: {filename}")
    else:
        print(f"The path {path} does not exist.")


path = '/path/to/file'
check_path(path)


# Exercise 4
def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return len(lines)


filename = 'yourfile.txt'
num_lines = count_lines(filename)

print(f"The file {filename} has {num_lines} lines.")


# Exercise 5
def write_list_to_file(lst, filename):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

my_list = ['apple', 'banana', 'cherry']
filename = 'my_file.txt'
write_list_to_file(my_list, filename)

print(f"The list has been written to {filename}.")


# Exercise 6
for i in range(65, 91):  # ASCII values for A-Z
    filename = chr(i) + '.txt'
    with open(filename, 'w') as f:
        f.write(f"This is file {chr(i)}.txt")


# Exercise 7
def copy_file(source_filename, destination_filename):
    with open(source_filename, 'r') as source_file:
        contents = source_file.read()

    with open(destination_filename, 'w') as destination_file:
        destination_file.write(contents)

source_filename = 'source.txt'
destination_filename = 'destination.txt'
copy_file(source_filename, destination_filename)

print(f"The contents of {source_filename} have been copied to {destination_filename}.")


# Exercise 8
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"The file {path} has been deleted.")
        else:
            print(f"The file {path} is not accessible.")
    else:
        print(f"The file {path} does not exist.")

path = '/path/to/file'
delete_file(path)


