#!/usr/bin/env python3
"""
Author : Roberto Carlos Gonzalez Retamoza <rcgr.13@gmail.com>
Date   : 2023-03-29
Purpose: Howler. Change text to all caps.
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler. Change text to all caps.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='A text to turn all to caps. Can be a text or the path of a file.')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        help='Tells if you want the text to output in a file.')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.text
    out_arg = args.outfile
    text = ''

    if os.path.isfile(pos_arg):
        with open(pos_arg, encoding='UTF-8') as in_handler:
            text = in_handler.read().upper()
    else:
        text = pos_arg.upper()

    if out_arg is not None:
        with open(out_arg, 'wt', encoding='UTF-8') as out_handler:
            out_handler.write(text)
    else:
        print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
