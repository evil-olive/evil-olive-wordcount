from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == "POST":
        text = request.GET["fulltext"]
        words = text.split()

        word_dictionary = {}

        for word in words:
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary[word] = 1  

        return render(request, "index.html", {'full': text, 'total': len(words), 'dictionary': word_dictionary.items()})
    else:
        return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def result(request):
    text = request.GET["fulltext"]
    words = text.split()

    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1  


    return render(request, "index.html", {'full': text, 'total': len(words), 'dictionary': word_dictionary.items()})