import sys
import csv
import os

# get a csv file name from the specified directory
def get_csv_filename(dir):
    filename = ''

    # get a list of all csv files in the current directory
    csvs = [f for f in os.listdir(dir) if f.lower().endswith('.csv')]

    try:
        if len(csvs) == 1:
            filename = csvs[0]

        elif len(csvs) < 1:
            print('No .csv files found.')
            sys.exit(0)

        else:
            # print a list of all csv files and have the user choose which to use
            for i, fname in list(enumerate(csvs)):
                print(f'{i + 1}. {fname}')

            file_num = int(input('\nWhich .csv file should be used? Enter the number of the file: '))
            file_index = file_num - 1
            filename = csvs[file_index]

    except TypeError:
        print('Please enter a valid integer.')

    except IndexError:
        print('Please enter a valid integer.')

    except:
        print('Unexpected error: ', sys.exc_info()[0])
        sys.exit(0)

    return filename


if __name__ == "__main__":

    try:
        filename = get_csv_filename('.')

        with open(filename) as csvfile:
            csvreader = csv.reader(csvfile)

            row1 = next(csvreader)

            # check column headers
            col2header = row1[2].lower().endswith('url')
            col3header = row1[3].lower().endswith('url')
            col4header = row1[4].lower().endswith('url')

            if row1[1].lower() != 'username':
                print('Expected header not found: Expected second column header to be "Username".')
                sys.exit(0)

            elif not col2header or not col3header or not col4header:
                print('Expected header not found: Expected third, fourth, and fifth column header to end with "URL".')
                sys.exit(0)

            # write each row to output file
            with open('out.txt', 'w+') as f:
                for row in csvreader:
                    u = row[1].strip()
                    front = row[2].strip()
                    alt = row[3].strip()
                    deets = row[4].strip()

                    s = f'{u}: [Front]({front})'

                    if alt:
                        s += f', [Alternate]({alt})'

                    if deets:
                        s += f', [Details]({deets})'

                    s += '\n'

                    f.write(s)

    except:
        print('Unexpected error: ', sys.exc_info()[0])
        sys.exit(0)