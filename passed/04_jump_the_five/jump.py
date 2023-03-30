#!/usr/bin/env python3
"""
Author : Roberto Carlos Gonzalez Retamoza <rcgr.13@gmail.com>
Date   : 2023-03-29
Purpose: Jump the five. Encode numbers.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five. Encode the numbers from a text.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='A text. The characters to encode are the numbers.')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.text
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0', '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    # for key in jumper:
    #     print(jumper[key], end='')
    # print('\n')

    # My solution
    for char in pos_arg:
        if char in jumper:
            print(jumper[char], end='')
        else:
            print(char, end='')

    # Another solution
    # for char in pos_arg:
    #     print(jumper.get(char, char), end='')

    # Yet another solution
    # print(pos_arg.translate(str.maketrans(jumper)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
