import glob2

file_names = glob2.glob('*.csv')  # list of all .txt files in the directory

with open('tweets.csv', 'w') as f:
    for file in file_names:
        with open(file) as infile:
            f.write(infile.read())