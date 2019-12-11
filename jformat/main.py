from . import reformat
import argparse
import os
import pkg_resources
import sys
import logging

# utilities

def str_to_bool(val):
    """
    Convert a string representation of truth to True or False

    True values are 'y', 'yes', or ''; case-insensitive
    False values are 'n', or 'no'; case-insensitive
    Raises ValueError if 'val' is anything else.
    """
    true_vals = ['yes', 'y', '']
    false_vals = ['no', 'n']
    try:
        val = val.lower()
    except AttributeError:
        val = str(val).lower()
    if val in true_vals:
        return True
    elif val in false_vals:
        return False
    else:
        raise ValueError("Invalid input value: %s" % val)


def prompt_bool(question):
    try:
        return str_to_bool(response)
    except ValueError:
        print('Valid true responses are: y, yes, <Enter>')
        print('Valid false responses are: n, no')
        print('That response was invalid, please try again')
        return prompt_bool(question)


def main(argv=None):
    argv = argv or sys.argv
    parser = argparse.ArgumentParser(
        prog='jformat',
        description='Format JSON files!',
    )

    parser.add_argument(
        '--file',
        help='JSON file'
    )

    parser.add_argument(
        '--indent',
        default=4,
        help='Indentation spaces, defaults to 4',
    )

    parser.add_argument(
        '--sort',
        action='store_true',
        help='Sort the keys alphabetically',
    )

    parser.add_argument(
        '--inline',
        action='store_true',
        help='Replace/rewrite the file inline',
    )

    args = parser.parse_args()

    if args.inline and args.file:
        with open(args.file, 'r') as _f:
            result = reformat.formatter(
                _f.read(),
                sort_keys=args.sort,
                indent=args.indent
            )

        with open(args.file, 'w') as _f:
            _f.write(result)
        return

    if args.file:
        with open(args.file, 'r') as _f:
            print(
                reformat.formatter(
                    _f.read(),
                    sort_keys=args.sort,
                    indent=args.indent
                )
            )
