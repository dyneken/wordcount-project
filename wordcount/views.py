
from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordict = {}

    for word in wordlist:
        if word in wordict:
            wordict[word] += 1
        else:
            wordict[word] = 1

    sortedwords = sorted(wordict.items(), key=operator.itemgetter(1), reverse=True)


    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords})
