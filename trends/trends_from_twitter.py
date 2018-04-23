import glob2

file_names = glob2.glob('*.txt')  # list of all .txt files in the directory

<<<<<<< HEAD
with open('twitter_trends.txt', 'w') as f:
=======
with open('twitter_trend.txt', 'w') as f:
>>>>>>> dc4e6cf78b52506e8eb12ba8b1e1ec2604b8933e
    for file in file_names:
        with open(file) as infile:
            f.write(infile.read())