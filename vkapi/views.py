import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from vkapi import FriendsList
from vkapi.FriendsList import createList, getuserList_test, create_api
from vkapi.forms import TokenConfirm, Message

app_secret="v4v8sdeSxBLZKP272Vqu"
domen_name="127.0.0.1"
port=":8000/"
code_redirect="get_code"
token_redirect="save_token"

def getFriends(request):
    if request.method == "POST" and request.is_ajax():
        data = request.POST.get('post_text')
        print(data)
        users = request.POST.get('users_list')
        users=json.loads(users)
       #FriendsList.send_msg(create_api("c5bef065877b03c197c62935d7c19a57dca784a6fd2b51267e2230e2aec952742faad1f144fdf6d7cadfc"),data,users)

        return  HttpResponse({data})
    return render(request,"sendmessage.html",{"users": getuserList_test(),"form_msg":Message})

def send_message(request):

    if request.method=="POST":
        print(request.POST.getlist('data'))

    else:
        return  render(request,'tokenform.html',{'form':TokenConfirm})

def get_token(request):
    if request.method=="POST":
        form = TokenConfirm(request.POST)
        if form is not None and form.is_valid():
            token = form.cleaned_data['token']
            print(token)
        return  redirect(domen_name+port+"msg")
    else:
        return  render(request,'tokenform.html',{'form':TokenConfirm})




