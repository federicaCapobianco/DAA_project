#design a function pos_tagging that takes in input a tuple R of roles, a tuple S of strings a dictionary T whose keys are the R roles plus the Start and the values are dictionaries T[r] such that the keys of T[r] are the roles R plus End and the values of T[r] are the transition probabilities between r and the corresponding role defined by the key , and a dictionary E whose keys are the strings in S and the values are the dictionaries E[s] such that the keys of E[s] are the roles R and the values of E[s] are the emission probabilities of s for the corresponding role defined by the key.
#the function returns a dictionary whose keys are the words in S and the values are the words in R that maximize the probability of the sequence of words in S given the roles in R.
def pos_tagging(R, S, T, E):
    #take the words in S 
    words = S
    #take the roles in R
    roles = R
    #create a dictionary that will contain the probabilities of the sequence of words in S given the roles in R
    prob = {}
    #create a dictionary that will contain the roles that maximize the probability of the sequence of words in S given the roles in R
    max_prob = {}
    #create a dictionary that will contain the roles that maximize the probability of the sequence of words in S given the roles in R
    
    #for each word in S
    for word in words:
        #create a dictionary that will contain the probabilities of the sequence of words in S given the roles in R
        prob[word] = {}
        #for each role in R
        for role in roles:
            #if the word is in the dictionary E
            if word in E:
                #if the role is in the dictionary E[word]
                if role in E[word]:
                    #the probability of the sequence of words in S given the roles in R is the probability of the word given the role
                    prob[word][role] = E[word][role]
                #otherwise
                else:
                    #the probability of the sequence of words in S given the roles in R is 0
                    prob[word][role] = 0
            #otherwise
            else:
                #the probability of the sequence of words in S given the roles in R is 0
                prob[word][role] = 0
    print(prob)
    #divide the prob dictionary into classes based on the probability of the sequence of words in S given the roles in R
    #for each word in S
    for word in words:
        #create a dictionary that will contain the roles that maximize the probability of the sequence of words in S given the roles in R
        max_prob[word] = {}
        #create a dictionary that will contain the roles that maximize the probability of the sequence of words in S given the roles in R
        max_prob[word] = max(prob[word], key=prob[word].get)
    print(max_prob)
    #return the dictionary that contains the roles that maximize the probability of the sequence of words in S given the roles in R
    return max_prob


#call the function pos_tagging with the following parameters
pos_tagging(('Start', 'Noun', 'Verb', 'End'), ('the', 'dog', 'barks'), {'Start': {'Noun': 0.5, 'Verb': 0.5}, 'Noun': {'Noun': 0.1, 'Verb': 0.9, 'End': 0.0}, 'Verb': {'Noun': 0.0, 'Verb': 0.0, 'End': 1.0}, 'End': {}}, {'the': {'Noun': 1.0}, 'dog': {'Noun': 1.0}, 'barks': {'Verb': 1.0}})
