import  vk





def create_api(token):
    session = vk.Session(access_token=token)
    return vk.API(session)


def get_friends_list(api):
    return api.friends.get(fields=['first_name','last_name','online','sex','photo_50','relation'])


def send_msg(api, msg, users):
    for user in users:
        user = int(user)
        api.messages.send(user_id=user, message=msg)


def createList():
    api = create_api("c5bef065877b03c197c62935d7c19a57dca784a6fd2b51267e2230e2aec952742faad1f144fdf6d7cadfc")
    friends = get_friends_list(api)
    li =[]
    for friend in friends:
     try:
        ffriends= api.friends.get(user_id=friend['uid'],fields=['photo_200','sex','domain','age'])
        for ffriend in ffriends:
            if ffriend['sex']==1 :
                li.append(ffriend)
     except vk.exceptions.VkAPIError:
        print("kek")



    return li

def getuserList_test():
    api = create_api("c5bef065877b03c197c62935d7c19a57dca784a6fd2b51267e2230e2aec952742faad1f144fdf6d7cadfc")
    return  get_friends_list(api)


