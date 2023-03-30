#!/usr/bin/env python3
"""
Author : Roberto Carlos Gonzalez Retamoza <rcgr.13@gmail.com>
Date   : 2023-03-28
Purpose: Picnic List
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Item(s) list for a picnic.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('list',
                        metavar='list',
                        nargs='+',
                        help='Item(s) to bring')
    parser.add_argument('-s',
                        '--sorted',
                        help='To indicate if you want the list sorted',
                        action='store_true')
    parser.add_argument('-nc',
                        '--nocomma',
                        help="Indicate if you don't want to use the oxford comma",
                        action='store_true')
    parser.add_argument('-c',
                        '--character',
                        help='The separator character',
                        metavar='str',
                        type=str,
                        default=',')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.list
    comma_arg = args.nocomma
    sep_arg = args.character
    items = ''

    if args.sorted:
        pos_arg.sort()

    if len(pos_arg) == 1:
        items = pos_arg[0]
    elif len(pos_arg) == 2:
        items = ' and '.join(pos_arg)
    else:
        if comma_arg:
            items = ' and '.join([f'{sep_arg} '.join(pos_arg[:-1]), pos_arg[-1]])
        else:
            items = f'{sep_arg} and '.join([f'{sep_arg} '.join(pos_arg[:-1]), pos_arg[-1]])

    print(f'You are bringing {items}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
