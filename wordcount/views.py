from django.shortcuts import render

def wordcount(request):
    return render(request, 'wordcount.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    full = request.GET['fulltext']
    words = full.split()
    words_dic = {}
    for word in words:
        if word in words_dic:
            words_dic[word]+=1
        else:
            words_dic[word]=1

    return render(request, 'result.html', {'full' : full, 'length' : len(words), 'dic' : words_dic.items()})
