from django.http import HttpResponse
from django.shortcuts import render
from github import Github


def index(request):
    # using an access token

    g = Github("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")
    #print(g.get_user().get_repos())
    #return render(request, 'nvpcSite/index.html')
    for repo in g.get_user().get_repos():
        print(repo.name)
        #print(dir(repo))
    return render(request, 'nvpcSite/index.html')
