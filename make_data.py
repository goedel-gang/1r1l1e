"""
Make some data suitable for run-length encoding
"""

import random
import argparse
import string
import sys

def get_args():
    """
    Process argv
    """
    parser = argparse.ArgumentParser(description=__doc__)
    # make 100 megabytes of data by default
    parser.add_argument("-n", type=int, default=10 ** 8,
            help="number of bytes to write")
    return parser.parse_args()

def make_random(n):
    """
    Make some "random" data
    """
    i = 0
    while i < n:
        char = random.choice(string.printable)
        num = 0
        # make on average, runs of 1000.
        while random.random() > 1 / 1000:
            num += 1
            if i + num >= n:
                break
        i += num
        print(f"\r[{'-' * int(60 * i / n):<60}] ({i / n:4.0%})", end="",
                file=sys.stderr, flush=True)
        sys.stdout.write(char * num)
    print(file=sys.stderr)

if __name__ == "__main__":
    args = get_args()
    make_random(args.n)
