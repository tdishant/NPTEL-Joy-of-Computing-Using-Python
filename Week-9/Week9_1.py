#author name: [list of papers written by him]
papers = {'Madison':[10, 14, 37, 38, 39, 40, 41]}
#some papers are disputed, we need to figure out who wrote them

def read_file(filename):
    #name of the author:all the papers he wrote as a single string
    strings = []
    
    for file in filename:
        with open(f'/data/fedralist_{file}.txt') as f:
            strings.append(f.read())
    
    return ('\n'.join(strings))

#name of the author:all the papers he wrote as a single string
fedral_list_by_authors = {}
for author, files in papers.items():
    fedral_list_by_authors[author] = read_file(files)
    
authors = ('Hamilton', 'Madison', 'Disputed', 'Jay', 'Shared')

author_tokens = {}
length_distribution = {}

for author in authors:
    #takes a string and creates tokens out of it
    tokens = nltk.word_tokenize(fedral_list_by_authors[author])
    
    #discarding all the puncuations etc, only keeping alphabets
    author_tokens[author] = ([token for token in tokens if any(c.isalpha() for c in token)])
    
    #length of each token(word)
    token_lengths = [len(token) for token in author_tokens[author]]
    
    length_distribution[authors] = nltk.FreqDist(token_lengths)
    
    #plot(15, title = author) => max word length = 15
    length_distribution[author].plot(15, title = author)
    
    
    
    
    