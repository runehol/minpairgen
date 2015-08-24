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



def find_min_pair(a, b, minfreq=10000, numpossibilities = 10):
    
    lw = len(a)
    allpossibilites = []
    for word, freq in wordlist:
        if freq < minfreq: break
        if a in word:
            for i in range(len(word)-lw+1):
                if word[i:i+lw] == a:
                    candidate = word[:i] + b + word[i+lw:]
                    if candidate in worddict:
                        candfreq = worddict[candidate]
                        if candfreq >= minfreq:
                            score = freq*candfreq
                            allpossibilites.append( (score, word, candidate, freq, candfreq) )

    allpossibilites.sort(reverse=True)
    if len(allpossibilites) < numpossibilities/2 and minfreq > 1:
        return find_min_pair(a, b, minfreq / 10)
    
    print("'%s' -> '%s'\t" % (a, b), end="")
    for p in allpossibilites[:numpossibilities]:
        print("(%s <=> %s) " % (p[1], p[2]), end="")
    print("")

alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"

def find_min_pair_for_word(word, minfreq=10000, numpossibilities = 10):
    
    allpossibilites = []
    for i in range(len(word)):
        for j in range(-1, len(alphabet)):
            b = alphabet[j]
            if j == -1: b = ""
            candidate = word[:i] + b + word[i+1:]
            if candidate != word and candidate in worddict:
                candfreq = worddict[candidate]
                if candfreq >= minfreq:
                    score = candfreq
                    allpossibilites.append( (score, word, candidate, candfreq) )

    allpossibilites.sort(reverse=True)
    if len(allpossibilites) < numpossibilities/2 and minfreq > 1:
        return find_min_pair_for_word(word, minfreq / 10)
    
    print("'%s'\t" % (word), end="")
    for p in allpossibilites[:numpossibilities]:
        print("(%s <=> %s) " % (p[1], p[2]), end="")
    print("")



def cross_find_min_pair(letters, prefixa="", postfixa="", prefixb="", postfixb=""):
    for i in range(len(letters)):
        a = letters[i]
        start = i+1
        if prefixa != prefixb or postfixa != postfixb: start = 0
        for j in range(start, len(letters)):
            b = letters[j]
            find_min_pair(prefixa+a+postfixa, prefixb+b+postfixb)

def find_min_pair_against_nothing(letters):
    for a in letters:
        find_min_pair(a, "")


def main(argv):
    vowels = "aeioöuıü"
    s_sounds = "çjsşz"
    consonants = "bcçdfgğhjklmnprsştvyz"

    read_file("tr-2012/tr.txt")

    find_min_pair("ağ", "a", 0)

    find_min_pair("ğ", "", 0)

    cross_find_min_pair("ğgh")
    #find_min_pair_against_nothing("ğh")

    cross_find_min_pair(vowels)
    cross_find_min_pair(s_sounds)
    cross_find_min_pair("yj")

    find_min_pair_against_nothing(consonants)

    find_min_pair_for_word("köy")
    find_min_pair_for_word("lale")
    find_min_pair_for_word("lala")
    find_min_pair_for_word("dil")
    find_min_pair_for_word("ılık")
    find_min_pair_for_word("yol")
    find_min_pair_for_word("dal")
    find_min_pair_for_word("daima")
    find_min_pair_for_word("şair")
    find_min_pair_for_word("mahsus")

    for v in vowels:
        find_min_pair(v + "ğ", v)
        find_min_pair("ğ" + v, v)



if __name__ == "__main__":
    main(sys.argv)
