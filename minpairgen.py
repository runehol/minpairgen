#!/usr/bin/env python3

import sys


wordlist = []
worddict = {}


def read_file(fname):
    global wordlist, worddict

    for line in open(fname):
        word, freq = line.strip().split(" ")
        word = word.lower()
        freq = int(freq)
        #print(word, freq)
        wordlist.append( (word, freq) )
        worddict[word] = freq



def find_min_pair(a, b, minfreq=1000):
    assert len(a) == 1
    allpossibilites = []
    for word, freq in wordlist:
        if freq < minfreq: break
        if a in word:
            for i in range(len(word)):
                if word[i] == a:
                    candidate = word[:i] + b + word[i+1:]
                    if candidate in worddict:
                        candfreq = worddict[candidate]
                        if candfreq >= minfreq:
                            score = freq*candfreq
                            allpossibilites.append( (score, word, candidate, freq, candfreq) )

    allpossibilites.sort(reverse=True)
    if len(allpossibilites) < 2 and minfreq > 1:
        return find_min_pair(a, b, minfreq / 10)
    
    print("'%s' -> '%s'\t" % (a, b), end="")
    for p in allpossibilites[:10]:
        print("(%s <=> %s) " % (p[1], p[2]), end="")
    print("")



def cross_find_min_pair(letters):
    for i in range(len(letters)):
        a = letters[i]
        for j in range(i+1, len(letters)):
            b = letters[j]
            find_min_pair(a, b)

def find_min_pair_against_nothing(letters):
    for a in letters:
        find_min_pair(a, "")


def main(argv):
    vowels = "aeioöuıü"
    s_sounds = "çjsşz"
    alphabet = "abcçdefgğhıijklmnoöpqrsştuüvyz"
    consonants = "bcçdfgğhjklmnpqrsştvyz"

    read_file("tr-2012/tr.txt")

    find_min_pair("ğ", "", 0)

    cross_find_min_pair("ğgh")
    #find_min_pair_against_nothing("ğh")

    cross_find_min_pair(vowels)
    cross_find_min_pair(s_sounds)
    cross_find_min_pair("yj")

    find_min_pair_against_nothing(consonants)


if __name__ == "__main__":
    main(sys.argv)
