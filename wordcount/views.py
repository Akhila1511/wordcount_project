from django.http import HttpResponse
from django.shortcuts import render
import operator

# def homepage(request):
#     return HttpResponse('This is Home Page.....')

def homepage(request):
    return render(request, 'home.html', {'data': 'This is Home page...'})

def countpage(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    soretedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordlist),
                                          'soretedwords':soretedwords})