from bisect import bisect_left
import re

class WhiteList:

    def __init__(self):
        self.sequenceList = []

    def setWords(self, words):
        self.words = words
        self.numWords = len(self.words)

    def setSequenceList(self, sequences):
        self.sequenceList = sequences

    def getSequenceList(self, word):
        return self.sequenceList[word] if word and word in self.sequenceList else None

    def cleanText(self, text):
        return text.strip('.,?!').lower()

    def isWord(self, text):
        return self.cleanText(text) in self.words

    def isPrefix(self, text):
        text = self.cleanText(text)
        i = bisect_left(self.words, text)

        return i != self.numWords and self.words[i].startswith(text)

    def getReplacement(self, text, av=None, garbler=None):
        if av and av == base.localAvatar:
            return '\x01WLDisplay\x01%s\x02' % text
        elif not garbler:
            return '\x01WLRed\x01%s\x02' % text
        return garbler.garble(av, len(text.split(' ')))

    def processText(self, text, av=None, garbler=None):
        if not self.words:
            return text

        words = text.split(' ')
        newWords = []

        for word in words:
            if (not word) or self.isWord(word):
                newWords.append(word)
            else:
                newWords.append(self.getReplacement(word, av, garbler))

        lastWord = words[-1]

        if not garbler:
            if (not lastWord) or self.isPrefix(lastWord):
                newWords[-1] = lastWord
            else:
                newWords[-1] = self.getReplacement(lastWord, av, garbler)

        return ' '.join(newWords)

    def processSequences(self, text, av=None, garbler=None):
        if not self.sequenceList:
            return text

        words = text.split(' ')

        for wordNum in xrange(len(words)):
            word = words[wordNum].lower()
            sequences = self.getSequenceList(word)

            if not sequences:
                continue

            for sequenceNum in xrange(len(sequences)):
                sequence = sequences[sequenceNum].split()
                total = wordNum + len(sequence) + 1

                if total <= len(words) and sequence == [word.lower() for word in words[wordNum + 1:total]]:
                    words[wordNum:total] = self.getReplacement(' '.join(words[wordNum:total]), av, garbler).split()

        return ' '.join(words)

    def processThroughAll(self, text, av=None, garbler=None):
        if (text.startswith('~') and not garbler):
            return text

        return self.processSequences(self.processText(re.sub(' +', ' ', text), av, garbler), av, garbler)
