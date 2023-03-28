#!/usr/bin/env python3
"""
Author  : Roberto Carlos Gonzalez Retamoza <rcgr.13@gmail.com>
Date    : 2023-03-28
Purpose : Say Hello
"""

import argparse


def get_args():
    """
    To get arguments
    """
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument(
        "-n", "--name", metavar="name",
        default="World", help="Name to greet"
    )
    return parser.parse_args()


def main():
    """
    Say Hello
    """
    args = get_args()
    print("Hello, " + args.name + "!")


if __name__ == '__main__':
    main()
