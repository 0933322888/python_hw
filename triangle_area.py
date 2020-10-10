import argparse
import math 

parser = argparse.ArgumentParser(exit_on_error=False)
parser.add_argument('integers', metavar='N', type=int, nargs=3, help='integeres for triangle sides')
try:
    args = parser.parse_args()
    p = (args.integers[0] + args.integers[1] + args.integers[2] ) / 2
    s = math.sqrt(p * (p-args.integers[0]) * (p-args.integers[1]) * (p-args.integers[2]))
    print(s)
except argparse.ArgumentError:
    print("Whooops, an error in arguments")