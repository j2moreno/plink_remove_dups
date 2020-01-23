import argparse
import sys

import plink_remove_dups.app
import plink_remove_dups.release

def main():
    parser = argparse.ArgumentParser(prog='plink_remove_dups', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-v', '--version', action='version', version=plink_remove_dups.release.__version__)

    #-----------------------------------------------------------------------------------------------------
    # remove duplicates
    #-----------------------------------------------------------------------------------------------------

    parser.set_defaults(func=plink_remove_dups.app.remove_dups)

    parser.add_argument('--plink_prefix')

    parser.add_argument('-o', '--output_prefix')

    #-----------------------------------------------------------------------------------------------------
    # parse
    #-----------------------------------------------------------------------------------------------------

    if len(sys.argv) > 1:
        args = parser.parse_args(sys.argv[1:])
        args.func(vars(args))
    else:
        parser.print_help()
        sys.exit(1)
