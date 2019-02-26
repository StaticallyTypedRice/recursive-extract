# The main startup file

import argparse

def startup(path:str, extractor:str='7zip'):
    '''The program startup function.

    Arguments:
     - path: The path of the file to extract (only one path at a time)
     - extractor: The extraction software to use.
    '''

    print(f'path:\t\t{path}')
    print(f'extractor:\t{extractor}')
    print()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Recursively extract a file.')
    parser.add_argument('paths', type=str, nargs='+',
                        help='A list of file paths to extract.')
    parser.add_argument('--extractor', type=str, default='7zip',
                        help='The extraction software to use (tar, zip, etc...)')

    args = parser.parse_args()
    print(args)

    for path in args.paths:
        startup(path, args.extractor)