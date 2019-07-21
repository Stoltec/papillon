import pandas as df

# This function will find the intersetion of wordsbetween an existing wordlist
# and a provided pandas dataframe of sentences. It will also output what is 
# present in the dataframe but not the wordlist for you to review and add.
def find_in_and_out(data):
    wordlist = {*()}
    intersect = {*()}
    outersect = {*()}

    with open('data/wordlist.txt', 'r') as f:
        count = 0
        for line in f:
            word = f.readline()[:-1]
            if (word not in wordlist):
                count += 1
                wordlist.add(word)

    for _, row in data.iterrows(): 
        words = row.iat[0].split(' ')
        for word in words:
            if (word in wordlist):
                intersect.add(word)
            else:
                outersect.add(word)

    with open('data/intersection.txt', 'w') as i:
        for word in intersect:
            i.write(word + '\n')

    with open('data/outersection.txt', 'w') as o:
        for word in outersect:
            o.write(word + '\n')
