import os
import argparse 
import sys

## no shifting == bytes
## rigth shift 10 == kb
## rigth shift 20 == mb
## rigth shift 30 == gb


def FileZize(File, fitte, constant):
    return str(os.stat(File).st_size >> fitte) +" {:}".format(constant)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Size.py', usage='%(prog)s [--size kb|mb|gb] [--file fitte.exe')
    parser.add_argument("--size", help='displays how big a file is in kb|mb|gb')
    parser.add_argument("--file", help='give me a file or fitte, both is good')
    args = parser.parse_args()

    
    if args.size == "":
        print FileZize(args.file, 0, args.size)

    elif args.size == "kb":
        print FileZize(args.file, 10, args.size)

    elif args.size == "mb":
        print FileZize(args.file, 20, args.size)

    elif args.size == "gb":
        print FileZize(args.file, 30, args.size)

    else:
        sys.exit(1)
