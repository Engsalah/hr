import argparse
# This starts building up our own little parser that does what we want
def create_parser():
    parser = argparse.ArgumentParser()
    # These will add some arguments to the parser. First is the path to the export file.
    # csv or json.
    parser.add_argument('--path', help='the path to the export file')
    parser.add_argument('--format', default='json', choices=['json', 'csv'], type=str.lower)
    return parser



def main():

    import sys

    from hr import export, users

    from hr import users as u

    args = create_parser().parse_args()

    # This reads in the user information (from the pwd module
    users = u.fetch_users()

    if args.path:

        file = open(args.path, 'w', newline='')

    else:
        file = sys.stdout

    if args.format == 'json':
        export.to_json_file(file, users)

    else:
        export.to_csv_file(file, users)
