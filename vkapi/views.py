import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from vkapi import FriendsList
from vkapi.FriendsList import createList, getuserList_test, create_api, get_friends_list
from vkapi.forms import TokenConfirm, Message

app_secret="v4v8sdeSxBLZKP272Vqu"
domen_name="127.0.0.1"
port=":8000/"
code_redirect="get_code"
token_redirect="save_token"


def getFriends(request,token):
    api=create_api(token)
    print(token)
    if request.method == "POST" and request.is_ajax():
        data = request.POST.get('post_text')
        print(data)
        users = request.POST.get('users_list')
        users=json.loads(users)
        FriendsList.send_msg(api,data,users)

        return  HttpResponse({data})
def send_message(request):

    if request.method=="POST":
        print(request.POST.getlist('data'))

    else:
        return  render(request,'tokenform.html',{'form':TokenConfirm})

def get_token(request,code):
    return redirect("https://oauth.vk.com/access_token",client_id=5446940,client_secret="v4v8sdeSxBLZKP272Vqu",redirect_uri="https://krakenvkapp.herokuapp.com/fFriends",code=code)


def confirmtoken(request):
    if request.method=="POST":
        form = TokenConfirm(request.POST)
        if form is not None and form.is_valid():
            token = form.cleaned_data['token']
            print(token)
        return  render(request,"sendmessage.html",{"users": get_friends_list(create_api(token)),"form_msg":Message})
    else:
        return  render(request,'tokenform.html',{'form':TokenConfirm})




