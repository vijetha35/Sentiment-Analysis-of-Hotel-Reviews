from __future__ import division
import sys,json,re,collections,math
def preprocessCorpus(sentence):
    sentence = re.sub(r'[^\w\s]', ' ', sentence).lower()
    return sentence
with open("nbmodel.txt", 'r') as model:
    dumpedlist = json.load(model)
    bag_of_words = dumpedlist[0]
    likelihood = dumpedlist[1]
    number_positive_sentences = dumpedlist[2]
    number_negative_sentences = dumpedlist[3]
    number_true_sentences = dumpedlist[4]
    number_fake_sentences = dumpedlist[5]
    bag_of_words = collections.defaultdict(lambda: dict, bag_of_words)
    likelihood = collections.defaultdict(lambda: dict, likelihood )


def main(argv):
    sentences=[]
    id=[]
    with open(argv[1],'r') as fileHandle:
         for eachline in fileHandle.readlines():
             eachline = eachline.decode("utf-8")
             splitSentence = eachline.replace("\n", "").split(" ")
             id.append(splitSentence[0])
             sentences.append(" ".join(splitSentence[1:]))
    unique_words = len(bag_of_words)
    predictSentiment= []
    predictTruth =[]
    prior_positive =number_positive_sentences/(number_positive_sentences+number_negative_sentences)
    prior_negative =number_negative_sentences/(number_positive_sentences+number_negative_sentences)
    prior_true =number_true_sentences/(number_true_sentences+number_fake_sentences)
    prior_fake= number_fake_sentences/(number_true_sentences+number_fake_sentences)
    i=0
    for eachSentence in sentences:

        eachSentence=preprocessCorpus(eachSentence).split()
        positiveProb =math.log(prior_positive)
        negativeProb=math.log(prior_negative)
        trueProb=math.log(prior_true)
        fakeProb = math.log(prior_fake)
        for eachWord in eachSentence:
            if likelihood.has_key(eachWord):
                positiveProb+=math.log(likelihood[eachWord]['positive'])
                negativeProb+=math.log(likelihood[eachWord]['negative'])
                trueProb +=math.log( likelihood[eachWord]['true'])
                fakeProb += math.log(likelihood[eachWord]['fake'])
        if positiveProb > negativeProb:
            predictSentiment.append("Pos")
        else:
            predictSentiment.append("Neg")
        if trueProb > fakeProb:
            predictTruth.append("True")
        else:
            predictTruth.append("Fake")


    writeFile = open("nboutput.txt", "w+")

    for i in range(0, len(id)):
        writeString = id[i] +" " +predictTruth[i] +" "+predictSentiment[i]+"\n"
        writeString = writeString.encode("utf-8")
        writeFile.write(writeString)
    writeFile.close()

if __name__ == "__main__":
        main(sys.argv)
