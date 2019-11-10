from django.http import HttpResponse
from django.shortcuts import  render
import operator



def home(request):
    return render(request,'homepage.html')
def count(request):
    fulltext = request.GET['fulltext']
    word=fulltext.split()
    worddict={}
    for item in word:
        if item in worddict:
            worddict[item]+=1
        else:
            worddict[item]=1

        sortedwords=sorted(worddict.items(), key= operator.itemgetter(1), reverse= True)
    return render(request, 'count.html', {'full':fulltext, 'count':len(word),'sorted':sortedwords})

def about(request):
    return render(request,'about.html')
