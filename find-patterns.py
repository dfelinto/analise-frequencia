#!/usr/bin/python

# ##########################
# Imports
# ##########################
import os
import sys
import math
import time

def is_good_file(filename):
    """XXX error messages"""
    if not os.path.exists(filename):
        return False

    return True


def parse_args():
    import argparse  # to parse options for us and print a nice help message

    # get the args passed to blender after "--", all of which are ignored by
    # blender so scripts may receive their own arguments
    argv = sys.argv
    file_input = None

    if len(argv) < 2 or not is_good_file(argv[1]):
        argv = []  # as if no args are passed
    else:
        file_input = argv[1]
        argv = argv[2:]  # get all args after "myfile.ply"

    # When --help or no args are given, print this help
    usage_text = \
    "usage:\n" \
    "find-patterns.py code.txt [--minimum-size 3] [--maximum-size 4]\n" \
    "\n"
    parser = argparse.ArgumentParser(description=usage_text)

    # Example utility, add some text and renders or saves it (with options)
    # Possible types are: string, int, long, choice, float and complex.
    parser.add_argument("-n", "--minimum-size", dest="minimum_size", type=int,
            help="Minimum length of pattern to match")

    parser.add_argument("-x", "--maximum-size", dest="maximum_size", type=int,
            help="Maximum length of pattern to match")

    args = parser.parse_args(argv)

    if not argv:
        parser.print_help()
        sys.exit()

    if not file_input:
        print("Error: file argument not given, aborting.")
        parser.print_help()
        sys.exit()

    # Run the example function
    return validate_function(file_input, args.minimum_size, args.maximum_size)

    print("Parsing Process Finished.")


def validate_function(input, minimum, maximum):
    """For now simply bypass and return the passed values"""
    return input, minimum, maximum

# ##########################
# Find Patterns
# ##########################

def remove_new_lines(text):
    """"""
    data = text.splitlines()
    return "".join(data)


def find_patterns(input, minimum, maximum):
    """"""
    data = {}
    fileR = open(input, "r")
    raw_data = ""

    raw_data = remove_new_lines(fileR.read())
    size = len(raw_data)

    for i in range(minimum, maximum + 1):
        data[i] = {}

        for j in range(size - (i - 1)):
            substr = raw_data[j : j + i]
            count = raw_data.count(substr)
            if count > 1:
                data[i][substr] = count

    return data


# ##########################
# Export Data
# ##########################

def export_data(data):
    """"""
    # order the data
    print(data)

# ##########################
# Main
# ##########################

def main():
    # 1) parse args
    input, minimum, maximum = parse_args()

    # 2) find patterns
    data = find_patterns(input, minimum, maximum)

    # 5) export patterns
    export_data(data)


if __name__ == 'main':
    main()

main()
