from django.shortcuts import render
from . import Api
api = Api.APITwitterClass()

def mainViews(request):

    if request.method == 'POST':
        text = request.POST['text']
        text = text.split()
        userInfoList = []

        for i in text:
            user = i.split('https://twitter.com/')
            userInfoList.append(api.GetUserInfo(name=user[-1]))
        return render(request, 'main/mainHtml.html', {'userInfoList': userInfoList})

    return render(request, 'main/mainHtml.html')


def twViews(request, pk):

    userInfoList = api.GetUserTw(name=pk)
    return render(request, 'main/tw.html', {'userInfoList': userInfoList, 'pk': pk})

