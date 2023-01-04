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

def pos_tag(possible_tags, sentence, transitions, emissions):
  # Initialize the matrices
  V = [{}]
  path = {}

  # Initialize the base cases
  for tag in possible_tags:
    print("tag: ", tag)
    print("transitions[Start][tag]: ", transitions["Start"].get(tag))
    V[0][tag] = transitions["Start"].get(tag) * emissions[sentence[0]].get(tag)
    print("V[0][tag]: ", V[0][tag])
    path[tag] = [tag]

  # Run the dynamic programming algorithm
  for t in range(1, len(sentence)):
    V.append({})
    new_path = {}

    for tag in possible_tags:
      (prob, state) = max([(V[t-1][prev_tag] * transitions[prev_tag].get(tag) * emissions[sentence[t]].get(tag), prev_tag) for prev_tag in possible_tags])
      V[t][tag] = prob
      new_path[tag] = path[state] + [tag]

    # Don't need to remember the old paths
    path = new_path

  # Find the most probable sequence backwards
  (prob, state) = max([(V[len(sentence) - 1][tag], tag) for tag in possible_tags])
  res = path[state]
  #make a dictionary that contains the words in S as keys and the roles in res as values
  d = dict(zip(sentence, res))
  return d




def pos_tag2(sentence, possible_tags, transitions, emissions):
  # Add a special start tag to the list of possible tags
  possible_tags = ["start"] + possible_tags

  # Initialize the matrices
  V = [{}]
  path = {}

  # Initialize the base cases
  for tag in possible_tags:
    V[0][tag] = transitions["start"][tag] * emissions[tag][sentence[0]]
    path[tag] = [tag]

  # Run the dynamic programming algorithm
  for t in range(1, len(sentence)):
    V.append({})
    new_path = {}

    for tag in possible_tags:
      (prob, state) = max([(V[t-1][prev_tag] * transitions[prev_tag][tag] * emissions[tag][sentence[t]], prev_tag) for prev_tag in possible_tags])
      V[t][tag] = prob
      new_path[tag] = path[state] + [tag]

    # Don't need to remember the old paths
    path = new_path

  # Find the most probable sequence backwards
  (prob, state) = max([(V[len(sentence) - 1][tag], tag) for tag in possible_tags])
  return path[state]


def pos_tag3(possible_tags, sentence, transitions, emissions):
  # Initialize the matrices
  V = [{}]
  path = {}

  # Initialize the base cases
  for tag in possible_tags:
    V[0][tag] = transitions["Start"][tag] * emissions[tag][sentence[0]]
    path[tag] = [tag]

  # Run the dynamic programming algorithm
  for t in range(1, len(sentence)):
    V.append({})
    new_path = {}

    for tag in possible_tags:
      (prob, state) = max([(V[t-1][prev_tag] * transitions[prev_tag][tag] * emissions[tag][sentence[t]], prev_tag) for prev_tag in possible_tags])
      V[t][tag] = prob
      new_path[tag] = path[state] + [tag]

    # Don't need to remember the old paths
    path = new_path

  # Find the most probable sequence backwards
  (prob, state) = max([(V[len(sentence) - 1][tag], tag) for tag in possible_tags])
  return path[state] + ["end"]


#call the function pos_tagging with the following paramete
