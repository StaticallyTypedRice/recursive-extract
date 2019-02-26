# The main startup file

import argparse
from modules.extract import *

def startup(path:str, extractor:str='7z'):
    '''The program startup function.

    Arguments:
     - path: The path of the file to extract (only one path at a time)
     - extractor: The extraction software to use.
    '''
    # Check the extraction software selection
    if extractor == '7z':
        extract_7z(path)
    else:
        raise ExtractionError(f'The extraction software \'{extractor}\' is not recognized.')

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Recursively extract a file.')
    parser.add_argument('paths', type=str, nargs='+',
                        help='A list of file paths to extract.')
    parser.add_argument('--extractor', type=str, default='7z',
                        help='The extraction software to use (tar, zip, etc...)')

    args = parser.parse_args()

    for path in args.paths:
        try:
            startup(path, args.extractor)
        except ExtractionError as e:
            print(str(e))
            break