import sys
import os
import datetime


terminal = sys.argv
d_passed = False
f_passed = False
f_written = False
path = os.getcwd()
file_name = ""

if len(sys.argv) > 2:
    for index in range(1, len(sys.argv)):
        if sys.argv[index - 1] == "-f":
            file_name = sys.argv[index]
            f_passed = True
            continue
        if sys.argv[index] == "-d":
            d_passed = True
            continue
        if d_passed and sys.argv[index] != "-f":
            path = os.path.join(path, sys.argv[index])

if d_passed:
    os.makedirs(path)
if f_passed:
    with open(os.path.join(path, file_name), "a") as file:

        if file.tell() != 0:
            file.write("\n")

        format_time = "%Y-%m-%d %H:%M:%S"
        file.write(datetime.datetime.now().strftime(format_time) + "\n")

        line_count = 1
        while True:
            line = input("Enter content line: ")

            if line == "stop":
                break

            file.write(f"{line_count} {line}\n")
            line_count += 1
