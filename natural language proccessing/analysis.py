import nltk

papers={ "Madison":[10, 14, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
        "Hamilton": [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24, 25,
            26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60, 61, 65, 66, 67,
            68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
            85],
        "Jay":[2, 3, 4, 5],
        "Shared":[18, 19, 20],
        "Disputed":[49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63]
        }

def read_files(filename):
    #key : author's name
    # value : all author's data
    strings = []

    for file in filename:
        with open(f'./data/federalist_{file}.txt') as f: # ie federalist_1,then 2,....
            strings.append(f.read())
    return ('\n'.join(strings))

federalist_by_author  = {}

for author, files in papers.items():
    # here i, j = (author ,[list of paper numbers]) the values get assigned
    # accordingly
    federalist_by_author[author] = read_files(files)
    #this assigns all the files with writting whihc were joined together
    #earlier to their author
'''   
for i in federalist_by_author:
    print (federalist_by_author[i][:100])
'''

authors = ("Hamilton", "Madison", "Disputed", "Jay", "Shared")

author_tokens = {}
length_distribution = {}

for author in authors:
    tokens = nltk.word_tokenize(federalist_by_author[author])
    # a token here means set of elements seprated by spaces or other special
    # characters like "hell",".","''",......... 
    #print(tokens)
    author_tokens[author] = ([token for token in tokens if any(c.isalpha() for c in
        token)])
    #only those tokens are considered that at least jae one alphabet so that
    # its length is taken
    token_lengths = [len(token) for token in author_tokens[author]]

    length_distribution[author] = nltk.FreqDist(token_lengths) # it must be [author] wrong in video
    length_distribution[author].plot(15, title = author)
    # here 15 signifies length of max word

