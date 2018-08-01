"""https://stevenloria.com/tf-idf/"""
import math
import re


def tf(word, blob):
    return re.findall(r"[a-zA-Z]+", blob).count(word) / len(re.findall(r"[a-zA-Z]+", blob))


def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in re.findall(r"[a-zA-Z]+", blob))


def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))


def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)
