import sys,re,json
from copy import copy
from collections import Counter,defaultdict
stopWords=['a', 'able', 'about', 'above', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 'added', 'adj', 'affected', 'affecting', 'affects', 'after', 'afterwards', 'again', 'against', 'ah', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'announce', 'another', 'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apparently', 'approximately', 'are', 'aren', 'arent', 'arise', 'around', 'as', 'aside', 'ask', 'asking', 'at', 'auth', 'available', 'away', 'awfully', 'b', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'between', 'beyond', 'biol', 'both', 'brief', 'briefly', 'but', 'by', 'c', 'ca', 'came', 'can', 'cannot', "can't", 'cause', 'causes', 'certain', 'certainly', 'co', 'com', 'come', 'comes', 'contain', 'containing', 'contains', 'could', 'couldnt', 'd', 'date', 'did', "didn't", 'different', 'do', 'does', "doesn't", 'doing', 'done', "don't", 'down', 'downwards', 'due', 'during', 'e', 'each', 'ed', 'edu', 'effect', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'especially', 'et', 'et-al', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'except', 'f', 'far', 'few', 'ff', 'fifth', 'first', 'five', 'fix', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'found', 'four', 'from', 'further', 'furthermore', 'g', 'gave', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'go', 'goes', 'gone', 'got', 'gotten', 'h', 'had', 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', 'hed', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hi', 'hid', 'him', 'himself', 'his', 'hither', 'home', 'how', 'howbeit', 'however', 'hundred', 'i', 'id', 'ie', 'if', "i'll", 'im', 'immediate', 'immediately', 'importance', 'important', 'in', 'inc', 'indeed', 'index', 'information', 'instead', 'into', 'invention', 'inward', 'is', "isn't", 'it', 'itd', "it'll", 'its', 'itself', "i've", 'j', 'just', 'k', 'keep\tkeeps', 'kept', 'kg', 'km', 'know', 'known', 'knows', 'l', 'largely', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'line', 'little', "'ll", 'look', 'looking', 'looks', 'ltd', 'm', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'me', 'mean', 'means', 'meantime', 'meanwhile', 'merely', 'mg', 'might', 'million', 'miss', 'ml', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'mug', 'must', 'my', 'myself', 'n', 'na', 'name', 'namely', 'nay', 'nd', 'near', 'nearly', 'necessarily', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'normally', 'nos', 'not', 'noted', 'nothing', 'now', 'nowhere', 'o', 'obtain', 'obtained', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'omitted', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'ord', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'owing', 'own', 'p', 'page', 'pages', 'part', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'poorly', 'possible', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'previously', 'primarily', 'probably', 'promptly', 'proud', 'provides', 'put', 'q', 'que', 'quickly', 'quite', 'qv', 'r', 'ran', 'rather', 'rd', 're', 'readily', 'really', 'recent', 'recently', 'ref', 'refs', 'regarding', 'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted', 'resulting', 'results', 'right', 'run', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'sec', 'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sent', 'seven', 'several', 'shall', 'she', 'shed', "she'll", 'shes', 'should', "shouldn't", 'show', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'since', 'six', 'slightly', 'so', 'some', 'somebody', 'somehow', 'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specifically', 'specified', 'specify', 'specifying', 'still', 'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such', 'sufficiently', 'suggest', 'sup', 'sure\tt', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that'll", 'thats', "that've", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'thered', 'therefore', 'therein', "there'll", 'thereof', 'therere', 'theres', 'thereto', 'thereupon', "there've", 'these', 'they', 'theyd', "they'll", 'theyre', "they've", 'think', 'this', 'those', 'thou', 'though', 'thoughh', 'thousand', 'throug', 'through', 'throughout', 'thru', 'thus', 'til', 'tip', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'ts', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'ups', 'us', 'use', 'used', 'useful', 'usefully', 'usefulness', 'uses', 'using', 'usually', 'v', 'value', 'various', "'ve", 'very', 'via', 'viz', 'vol', 'vols', 'vs', 'w', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome', "we'll", 'went', 'were', 'werent', "we've", 'what', 'whatever', "what'll", 'whats', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whim', 'whither', 'who', 'whod', 'whoever', 'whole', "who'll", 'whom', 'whomever', 'whos', 'whose', 'why', 'widely', 'willing', 'wish', 'with', 'within', 'without', 'wont', 'words', 'world', 'would', 'wouldnt', 'www', 'x', 'y', 'yes', 'yet', 'you', 'youd', "you'll", 'your', 'youre', 'yours', 'yourself', 'yourselves', "you've", 'z', 'zero']


corpus_sentences=[]
def main(argv):
    id=[]
    truthValues=[]
    reviewSentiment=[]
    global corpus_sentences

    with open(argv[1]) as fileHandle:
         for eachline in fileHandle.readlines():
             eachline =eachline.decode(encoding ="utf-8")
             splitSentence = eachline.replace("\n", "" ).split(" ")
             id.append(splitSentence[0])
             truthValues.append(splitSentence[1])
             reviewSentiment.append(splitSentence[2])
             sentence = splitSentence[3:]
             sentence = [w for w in splitSentence[3:] if not w in stopWords]
             # sentence = [ item for item in sentence if len(item)>1]
             sentence=" ".join(sentence)
             sentence= re.sub(r'\'','',sentence)
             sentence = re.sub(r'[^\w\s]', ' ', sentence).lower()
             corpus_sentences.append(sentence)
    number_of_sentences = len(id)


    maxIterations = 50




    vocabulary = defaultdict(dict)

    for i in range(0, number_of_sentences):
       for eachWord in corpus_sentences[i].split():
           if vocabulary.has_key(eachWord):
               vocabulary[eachWord] = vocabulary[eachWord] +1
           else:
               vocabulary[eachWord] = 1
    number_of_unique_words = len(vocabulary)

    weight_vector = defaultdict(int)
    updatedCache = defaultdict(int)

    for eachWord in vocabulary:
        weight_vector[eachWord] =0
        updatedCache[eachWord] = 0


    word_vector_sentiment,bias_sentiment,word_vector_sentiment_averaged,bias_sentiment_averaged = perceptron_train( maxIterations,reviewSentiment,0,weight_vector,"Pos",updatedCache,0)

    weight_vector = defaultdict(int)
    updatedCache = defaultdict(int)

    for eachWord in vocabulary:


        weight_vector[eachWord] =0
        updatedCache[eachWord]=0

    word_vector_truthValues, bias_truthValues,word_vector_truthValues_averaged,bias_truthValues_averaged = perceptron_train( maxIterations, truthValues, 0, weight_vector,"True",updatedCache,0)


    with open('vanillamodel.txt', 'w') as f:
        dump_text = [word_vector_sentiment,bias_sentiment,word_vector_truthValues, bias_truthValues]
        json.dump(dump_text, f)
    with open('averagedmodel.txt', 'w') as f:
        dump_text = [word_vector_sentiment_averaged, bias_sentiment_averaged, word_vector_truthValues_averaged, bias_truthValues_averaged]
        json.dump(dump_text, f)

def perceptron_train(maxIterations,classifer_vector,bias, word_weight,classifer_type,updatedCacheVector,beta):
    countIter=1

    for i in range(0,maxIterations):


        for j in range(0,len(corpus_sentences)):

            eachSentence= corpus_sentences[j]

            words_in_sentence = eachSentence.split()
            feature_vector = defaultdict(dict)
            for eachWord in words_in_sentence:
                if feature_vector.has_key(eachWord):
                    feature_vector[eachWord] = feature_vector[eachWord] +1
                else:
                    feature_vector[eachWord] = 1
            activation = 0
            for eachWord in feature_vector.keys():
                activation += word_weight[eachWord] * feature_vector[eachWord]
            activation +=bias

            if classifer_vector[j]==classifer_type:
                ySentiment=1
            else:
                ySentiment=-1

            if( (activation * ySentiment) <=0 ):
                for eachWord in feature_vector.keys():
                    word_weight[eachWord] = word_weight[eachWord] + (ySentiment *feature_vector[eachWord])
                    updatedCacheVector[eachWord]+=(ySentiment *countIter *feature_vector[eachWord])
                bias +=ySentiment
                beta +=(ySentiment*countIter)
            countIter = countIter+1


    for eachWord in updatedCacheVector.keys():
        updatedCacheVector[eachWord] = word_weight[eachWord] - (updatedCacheVector[eachWord]/float(countIter))
    beta = bias - (beta/float(countIter))
    return word_weight,bias,updatedCacheVector,beta
if __name__ == "__main__":
    main(sys.argv)