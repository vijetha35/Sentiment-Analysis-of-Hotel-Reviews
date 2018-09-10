from __future__ import division
import sys


from collections import Counter,defaultdict
# old stopWords=[ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]
stopWords=[]
# new stopWords which I'm reading from file is below :
stopWords=['a', 'able', 'about', 'above', 'abst', 'accordance', 'according', 'accordingly', 'across', 'act', 'actually', 'added', 'adj', 'affected', 'affecting', 'affects', 'after', 'afterwards', 'again', 'against', 'ah', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'an', 'and', 'announce', 'another', 'any', 'anybody', 'anyhow', 'anymore', 'anyone', 'anything', 'anyway', 'anyways', 'anywhere', 'apparently', 'approximately', 'are', 'aren', 'arent', 'arise', 'around', 'as', 'aside', 'ask', 'asking', 'at', 'auth', 'available', 'away', 'awfully', 'b', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'begin', 'beginning', 'beginnings', 'begins', 'behind', 'being', 'believe', 'below', 'beside', 'besides', 'between', 'beyond', 'biol', 'both', 'brief', 'briefly', 'but', 'by', 'c', 'ca', 'came', 'can', 'cannot', "can't", 'cause', 'causes', 'certain', 'certainly', 'co', 'com', 'come', 'comes', 'contain', 'containing', 'contains', 'could', 'couldnt', 'd', 'date', 'did', "didn't", 'different', 'do', 'does', "doesn't", 'doing', 'done', "don't", 'down', 'downwards', 'due', 'during', 'e', 'each', 'ed', 'edu', 'effect', 'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end', 'ending', 'enough', 'especially', 'et', 'et-al', 'etc', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'ex', 'except', 'f', 'far', 'few', 'ff', 'fifth', 'first', 'five', 'fix', 'followed', 'following', 'follows', 'for', 'former', 'formerly', 'forth', 'found', 'four', 'from', 'further', 'furthermore', 'g', 'gave', 'get', 'gets', 'getting', 'give', 'given', 'gives', 'giving', 'go', 'goes', 'gone', 'got', 'gotten', 'h', 'had', 'happens', 'hardly', 'has', "hasn't", 'have', "haven't", 'having', 'he', 'hed', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes', 'hi', 'hid', 'him', 'himself', 'his', 'hither', 'home', 'how', 'howbeit', 'however', 'hundred', 'i', 'id', 'ie', 'if', "i'll", 'im', 'immediate', 'immediately', 'importance', 'important', 'in', 'inc', 'indeed', 'index', 'information', 'instead', 'into', 'invention', 'inward', 'is', "isn't", 'it', 'itd', "it'll", 'its', 'itself', "i've", 'j', 'just', 'k', 'keep\tkeeps', 'kept', 'kg', 'km', 'know', 'known', 'knows', 'l', 'largely', 'last', 'lately', 'later', 'latter', 'latterly', 'least', 'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'line', 'little', "'ll", 'look', 'looking', 'looks', 'ltd', 'm', 'made', 'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'me', 'mean', 'means', 'meantime', 'meanwhile', 'merely', 'mg', 'might', 'million', 'miss', 'ml', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs', 'much', 'mug', 'must', 'my', 'myself', 'n', 'na', 'name', 'namely', 'nay', 'nd', 'near', 'nearly', 'necessarily', 'necessary', 'need', 'needs', 'neither', 'never', 'nevertheless', 'new', 'next', 'nine', 'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone', 'nor', 'normally', 'nos', 'not', 'noted', 'nothing', 'now', 'nowhere', 'o', 'obtain', 'obtained', 'obviously', 'of', 'off', 'often', 'oh', 'ok', 'okay', 'old', 'omitted', 'on', 'once', 'one', 'ones', 'only', 'onto', 'or', 'ord', 'other', 'others', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'outside', 'over', 'overall', 'owing', 'own', 'p', 'page', 'pages', 'part', 'particular', 'particularly', 'past', 'per', 'perhaps', 'placed', 'please', 'plus', 'poorly', 'possible', 'possibly', 'potentially', 'pp', 'predominantly', 'present', 'previously', 'primarily', 'probably', 'promptly', 'proud', 'provides', 'put', 'q', 'que', 'quickly', 'quite', 'qv', 'r', 'ran', 'rather', 'rd', 're', 'readily', 'really', 'recent', 'recently', 'ref', 'refs', 'regarding', 'regardless', 'regards', 'related', 'relatively', 'research', 'respectively', 'resulted', 'resulting', 'results', 'right', 'run', 's', 'said', 'same', 'saw', 'say', 'saying', 'says', 'sec', 'section', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems', 'seen', 'self', 'selves', 'sent', 'seven', 'several', 'shall', 'she', 'shed', "she'll", 'shes', 'should', "shouldn't", 'show', 'showed', 'shown', 'showns', 'shows', 'significant', 'significantly', 'similar', 'similarly', 'since', 'six', 'slightly', 'so', 'some', 'somebody', 'somehow', 'someone', 'somethan', 'something', 'sometime', 'sometimes', 'somewhat', 'somewhere', 'soon', 'sorry', 'specifically', 'specified', 'specify', 'specifying', 'still', 'stop', 'strongly', 'sub', 'substantially', 'successfully', 'such', 'sufficiently', 'suggest', 'sup', 'sure\tt', 'take', 'taken', 'taking', 'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that', "that'll", 'thats', "that've", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'thered', 'therefore', 'therein', "there'll", 'thereof', 'therere', 'theres', 'thereto', 'thereupon', "there've", 'these', 'they', 'theyd', "they'll", 'theyre', "they've", 'think', 'this', 'those', 'thou', 'though', 'thoughh', 'thousand', 'throug', 'through', 'throughout', 'thru', 'thus', 'til', 'tip', 'to', 'together', 'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try', 'trying', 'ts', 'twice', 'two', 'u', 'un', 'under', 'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up', 'upon', 'ups', 'us', 'use', 'used', 'useful', 'usefully', 'usefulness', 'uses', 'using', 'usually', 'v', 'value', 'various', "'ve", 'very', 'via', 'viz', 'vol', 'vols', 'vs', 'w', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome', "we'll", 'went', 'were', 'werent', "we've", 'what', 'whatever', "what'll", 'whats', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whim', 'whither', 'who', 'whod', 'whoever', 'whole', "who'll", 'whom', 'whomever', 'whos', 'whose', 'why', 'widely', 'willing', 'wish', 'with', 'within', 'without', 'wont', 'words', 'world', 'would', 'wouldnt', 'www', 'x', 'y', 'yes', 'yet', 'you', 'youd', "you'll", 'your', 'youre', 'yours', 'yourself', 'yourselves', "you've", 'z', 'zero']

# with open('stopwords_withnopunct.txt','r') as stopWordHandle:
#     for eachline in stopWordHandle.readlines():
#         stopWords.append(eachline.replace("\n",""))
# print stopWords
# print len(stopWords)
import re,json
def preprocessCorpus(positive_corpus,negative_corpus,true_corpus,false_corpus):
    positive_corpus = re.sub(r'[^\w\s]', ' ', positive_corpus).lower().split()
    positive_corpus=" ".join([w for w in positive_corpus if not w in stopWords])
    negative_corpus = re.sub(r'[^\w\s]', ' ', negative_corpus).lower().split()
    negative_corpus=" ".join([w for w in negative_corpus if not w in stopWords])
    true_corpus = re.sub(r'[^\w\s]', ' ', true_corpus).lower().split()
    true_corpus=" ".join([w for w in true_corpus if not w in stopWords])
    false_corpus = re.sub(r'[^\w\s]', ' ', false_corpus).lower().split()
    false_corpus=" ".join([w for w in false_corpus if not w in stopWords])
    return positive_corpus,negative_corpus,true_corpus,false_corpus
def main(argv):
    line =[[]]
    id=[]
    truthValues=[]
    reviewSentiment=[]
    corpus_sentences=[]

    with open(argv[1]) as fileHandle:
         for eachline in fileHandle.readlines():
             eachline =eachline.decode(encoding ="utf-8")
             splitSentence = eachline.replace("\n", "" ).split(" ")
             id.append(splitSentence[0])
             truthValues.append(splitSentence[1])
             reviewSentiment.append(splitSentence[2])
             corpus_sentences.append(" ".join(splitSentence[3:]))

    #print id, corpus_sentences[1]
    number_of_sentences = len(id)
    pos_vs_neg = Counter(reviewSentiment)
    true_vs_fake = Counter(truthValues)

    number_of_positive_sentence =pos_vs_neg['Pos']
    number_of_negative_sentence = pos_vs_neg['Neg']
    number_of_true_sentence =true_vs_fake['True']
    number_of_fake_sentence = true_vs_fake['Fake']

    #print pos_vs_neg, true_vs_fake,number_of_sentences,number_of_fake_sentence,number_of_negative_sentence,number_of_positive_sentence,number_of_true_sentence
    positive_corpus=""
    negative_corpus=""
    true_corpus=""
    fake_corpus=""

    # for i in range(0, number_of_sentences):
    #     words= corpus_sentences[i].split()
    #     filtered_sentence = [w for w in words if not w in stopWords]
    #     corpus_sentences[i]=" ".join(filtered_sentence)

    for i in range(0,number_of_sentences):
        if reviewSentiment[i] =='Pos':
            positive_corpus+=corpus_sentences[i]+"\n"


        elif reviewSentiment[i]=='Neg':
            negative_corpus+=corpus_sentences[i]+"\n"
        if truthValues[i] == 'True':
            true_corpus+=corpus_sentences[i]+"\n"
        elif truthValues[i] =='Fake':
            fake_corpus+=corpus_sentences[i]+"\n"


    bag_of_words= defaultdict(dict)
    # print positive_corpus,negative_corpus

    #print string.punctuation #  punctuations : !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    #training corpus given has these punctuations !    ! #"%$'&)(+*-,/.;:=<?>@[]~
    #print "".join(set(positive_corpus) | set(negative_corpus) | set(true_corpus) | set(fake_corpus))
    # for i in range(0,len(corpus_sentences)):
    #     words_in_sentence = re.sub(r'[^\w\s\']', ' ',corpus_sentences[i]).lower().split()
    #     if reviewSentiment[i] =='Pos':
    #         for eachWord in set(words_in_sentence):
    #             if bag_of_words[eachWord].has_key('PosNumDoc'):
    #                 bag_of_words[eachWord]['PosNumDoc'] =bag_of_words[eachWord]['PosNumDoc']+1
    #             else:
    #                 bag_of_words[eachWord]['PosNumDoc']=1
    #
    #     elif reviewSentiment[i]=='Neg':
    #         for eachWord in set(words_in_sentence):
    #             if bag_of_words[eachWord].has_key('NegNumDoc'):
    #                 bag_of_words[eachWord]['NegNumDoc'] =bag_of_words[eachWord]['NegNumDoc']+1
    #             else:
    #                 bag_of_words[eachWord]['NegNumDoc']=1
    #     if truthValues[i] =='True':
    #         for eachWord in set(words_in_sentence):
    #             if bag_of_words[eachWord].has_key('TrueNumDoc'):
    #                 bag_of_words[eachWord]['TrueNumDoc'] =bag_of_words[eachWord]['TrueNumDoc']+1
    #             else:
    #                 bag_of_words[eachWord]['TrueNumDoc']=1
    #
    #     elif truthValues[i] =='Fake':
    #         for eachWord in set(words_in_sentence):
    #             if bag_of_words[eachWord].has_key('FakeNumDoc'):
    #                 bag_of_words[eachWord]['FakeNumDoc'] =bag_of_words[eachWord]['FakeNumDoc']+1
    #             else:
    #                 bag_of_words[eachWord]['FakeNumDoc']=1

    positive_corpus,negative_corpus,true_corpus,fake_corpus=preprocessCorpus(positive_corpus,negative_corpus,true_corpus,fake_corpus)
    count=0
    for eachWord in positive_corpus.split():
        count+=1
        if bag_of_words[eachWord].has_key('positive'):
            bag_of_words[eachWord]['positive']= bag_of_words[eachWord]['positive']+1
        else:
            bag_of_words[eachWord]['positive']=1

    for eachWord in negative_corpus.split():
        count += 1
        if bag_of_words[eachWord].has_key('negative'):
            bag_of_words[eachWord]['negative']= bag_of_words[eachWord]['negative']+1
        else:
            bag_of_words[eachWord]['negative']=1
    for eachWord in true_corpus.split():
        count += 1
        if bag_of_words[eachWord].has_key('true'):
            bag_of_words[eachWord]['true']= bag_of_words[eachWord]['true']+1
        else:
            bag_of_words[eachWord]['true']=1
    for eachWord in fake_corpus.split():
        count += 1
        if bag_of_words[eachWord].has_key('fake'):
            bag_of_words[eachWord]['fake']= bag_of_words[eachWord]['fake']+1
        else:
            bag_of_words[eachWord]['fake']=1
    #print count
    vocabulary = len(set(bag_of_words))
    #print len(bag_of_words),vocabulary
    likelihood = defaultdict(dict)
    # tags =  [word_class for word,count_word_class in bag_of_words.iteritems() for word_class,count in count_word_class.iteritems() ]
    # print bag_of_words
    total =sum([count for word,count_word_class in bag_of_words.iteritems() for word_class,count in count_word_class.iteritems() if word_class=='positive' or word_class == 'negative' or word_class=='true' or word_class=='fake'])
    words_in_positive = sum([count for word,count_word_class in bag_of_words.iteritems() for word_class,count in count_word_class.iteritems() if word_class=='positive'])
    words_in_negative = sum([count for word, count_word_class in bag_of_words.iteritems() for word_class, count in count_word_class.iteritems() if word_class == 'negative'])
    words_in_true =sum([count for word,count_word_class in bag_of_words.iteritems() for word_class,count in count_word_class.iteritems() if word_class=='true'])
    words_in_fake = sum([count for word,count_word_class in bag_of_words.iteritems() for word_class,count in count_word_class.iteritems() if word_class=='fake'])
    # print words_in_positive,words_in_negative,words_in_true,words_in_fake,total,vocabulary

    # y = sorted(bag_of_words, reverse=True, key=lambda x: ('positive' not in bag_of_words[x],int(bag_of_words[x].get('positive',0))))
    # print y
    # y = sorted(bag_of_words, reverse=True, key=lambda x: ('positive' not in bag_of_words[x],int(bag_of_words[x].get('negative',0))))
    # print y
    # y = sorted(bag_of_words, reverse=True, key=lambda x: ('positive' not in bag_of_words[x],int(bag_of_words[x].get('true',0))))
    # print y
    # y = sorted(bag_of_words, reverse=True, key=lambda x:('positive' not in bag_of_words[x],int(bag_of_words[x].get('fake',0))))
    # print y

    for eachWord in bag_of_words.keys():
        if bag_of_words[eachWord].has_key("positive"):
            likelihood[eachWord]["positive"] = (bag_of_words[eachWord]["positive"] +1)/(words_in_positive +vocabulary )

        else:
            likelihood[eachWord]["positive"] =  1 / (words_in_positive + vocabulary)

        if bag_of_words[eachWord].has_key("negative"):
            likelihood[eachWord]["negative"] = (bag_of_words[eachWord]["negative"] + 1 )/ (words_in_negative + vocabulary)
        else:
            likelihood[eachWord]["negative"] = 1 / (words_in_negative + vocabulary)

        if bag_of_words[eachWord].has_key("true"):
            likelihood[eachWord]["true"] = (bag_of_words[eachWord]["true"] + 1) / (words_in_true + vocabulary)
        else:
            likelihood[eachWord]["true"] = 1 / (words_in_true + vocabulary)

        if bag_of_words[eachWord].has_key("fake"):
            likelihood[eachWord]["fake"] = (bag_of_words[eachWord]["fake"] + 1) / (words_in_fake + vocabulary)
        else:
            likelihood[eachWord]["fake"] = 1 / (words_in_fake + vocabulary)

    # print likelihood['chinese']
    with open('nbmodel.txt', 'w') as f:
        dump_text = [bag_of_words,likelihood,number_of_positive_sentence,number_of_negative_sentence,number_of_true_sentence,number_of_fake_sentence]
        json.dump(dump_text, f)

if __name__ == "__main__":
    main(sys.argv)

