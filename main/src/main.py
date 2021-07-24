import argparse
import sys

import sort
import maxelement

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sort a given array in descending order')
    parser.add_argument('--array', dest='array', required=False, default=[3,2,7,5,8,4,9,6], type=list, help='enter an array of int to sort')
    args = parser.parse_args()

    new_array = []
    new_array = sort.sorted_array(args.array)
    print(sort.sorted_array(args.array))
    print(maxelement.max_element(new_array))
