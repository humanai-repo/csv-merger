import argparse
import csv


def build_parser():
    parser = argparse.ArgumentParser(
        description='Merge CSV files together.')
    parser.add_argument('-i', '--input', action='append', required=True,
                        help='input files to merge.')
    parser.add_argument('-o', '--output', required=False,
                        help='Output file path.')
    return parser


def main():
    # Initialise vars
    parser = build_parser()
    parsed = parser.parse_args()

    writer = csv.writer(open(parsed.output, 'w'))
    header = None
    for inputPath in parsed.input:
        reader = csv.reader(open(inputPath))
        iHeader = None
        for row in reader:
            if iHeader is None:
                iHeader = row
                if header is None:
                    header = iHeader
                    writer.writerow(header)
                else:
                    if header != iHeader:
                        raise Exception("Columns in header do not match")
            else:
                writer.writerow(row)


if __name__ == "__main__":
    main()
