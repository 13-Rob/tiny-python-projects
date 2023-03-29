#!/usr/bin/env python3
"""
Author : Roberto Carlos Gonzalez Retamoza <rcgr.13@gmail.com>
Date   : 2023-03-28
Purpose: Add an article depending if the next word starts with a vocal or a
consonant.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- Add an article depending if the next word"
        + "starts with a vocal or a consonant.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='Any word')
    parser.add_argument('-s',
                        '--side',
                        help='To indicate if the object is on the starboard of the boat',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """
    If it is narwhal says 'a narwhal',
    if it is an octopus says 'an octopus'
    """
    args = get_args()
    word = args.word
    flag = args.side

    article = 'An' if word[0].lower() in 'aeiou' else 'A'
    # If the positional argument is a vocal then the set article to 'an',
    # else if it is not a vocal the article will be 'a'.

    article = article.lower() if word[0].islower() else article

    side = 'starboard' if flag else 'larboard'

    print(f'Ahoy, Captain, {article} {args.word} off the {side} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
