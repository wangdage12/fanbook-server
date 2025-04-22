from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
import time
import random

true=True
false=False
null=None

app = Flask(__name__)
CORS(app)

def fbid():
    "获取一个随机fbid"
    return str(int(time.time()*1000))
def gettime():
    "获取当前时间戳（13位），保留整数"
    return int(time.time()*1000)


@app.route('/api/a1/api/common/alipay', methods=['POST'])
def get_alipaya():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "a77653ac8b658ed80a585a42d8dc3924",
  "data": {
    "alipay": {
      "rule": "",
      "max_len": 80
    },
    "readHistory": true,
    "ledou": 0,
    "nft": 0,
    "welogin": 1,
    "applelogin": 1,
    "notification": {
      "total": 5,
      "open": true
    },
    "redbag": {
      "single_max_money": 20000,
      "max_num": 2000,
      "period": 86400
    },
    "setting": {
      "risk_switch": 1,
      "risk_domain": "https://risk.fanbook.cn",
      "risk_intercept_url": "https://fb-cdn.fanbook.cn/fanbook/app/link_ban.html"
    },
    "official_operation_bot_id": "398308634552958976",
    "pay_plat_switch": 0,
    "t_captcha": {
      "app_id": "197534779"
    },
    "open_screen_ads": {
      "switch": 1,
      "limit": 99,
      "out_priority": 0
    }
  }
})
    
@app.route('/api/a1/api/login/qrcode', methods=['POST'])
def login_qrcode():
    return jsonify({
  "status": false,
  "code": 1145,
  "message": "1145",
  "desc": "不支持的登录方式（扫码登录）",
})
    
@app.route('/api/a1/api/common/verification', methods=['POST'])
def login_verification():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "dc14d1f50fdaa719c7c4f3f5a08a674c"
})
    
@app.route('/api/a1/api/user/login', methods=['POST'])
def login():
    # 读取login.json
    with open('login.json', 'r',encoding='utf-8') as file:
        data = json.load(file)
    # 获取请求体中的mobile
    mobile = request.json.get('mobile')
    # 查找对应的用户数据
    user_data = None
    try:
        user_data = data[mobile]
    except:
        user_data={
    "admin_role_id": "",
    "user_id": fbid(),
    "avatar": None,
    "avatar_nft": "",
    "username": str(random.randint(100000,999999)),
    "mobile": "",
    "encryption_mobile": "",
    "joined_at": gettime(),
    "email": null,
    "gender": 1,
    "presence_status": 1,
    "discriminator": "12956140",
    "nickname": None,
    "ban_type": 0,
    "level": 0,
    "integral": 0,
    "sign": str(random.randint(10000000000,999999999999)),
    "expire_time": 9746079988,
    "area_code": 86
  }
        # 保存用户数据到login.json
        with open('login.json', 'w',encoding='utf-8') as file:
            data[mobile] = user_data
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "279b642c34459e3c63fa58bcb12f90a8",
  "data": user_data
})
    
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "279b642c34459e3c63fa58bcb12f90a8",
  "data": user_data
})

@app.route('/api/a1/api/common/setting', methods=['POST'])
def get_setting():
    # 读取 JSON 文件
    with open('apisetting.json', 'r',encoding='utf-8') as file:
        data = json.load(file)
    
    # 返回 JSON 数据
    return jsonify(data)

dids=[]

@app.route('/api/a1/api/v3/guild/myGuild', methods=['POST'])
def my_guild():
    #获取cookie中的did
    did = request.cookies.get('did')
    # 如果did在列表中，返回错误信息
    if did in dids:
        return jsonify({
            "status": false,
            "code": 1001,
            "message": "1001",
            "desc": "参数错误",
            "request_id": "233ec5f0cc5fffd60acd7d784ed02c9f",
            "data": ""
        })
    # 如果did不在列表中，添加到列表中
    else:
        dids.append(did)
#     return {  "status": true,
#   "code": 1000,
#   "message": "1000",
#   "desc": "成功",
#   "request_id": "b3b693a8b2fb9f0c8848bca801e7046b","data":""}
    # 读取response.json
    with open('response.json', 'r',encoding='utf-8') as file:
        data = json.load(file)
    
    
    return jsonify(data)

@app.route('/api/a1/api/user/remarkList', methods=['POST'])
def remarkList():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "b3b693a8b2fb9f0c8848bca801e7046b",
  "data": {
    "records": [],
    "size": 1000,
    "list_id": "0",
    "next": "0"
  }
})

@app.route('/api/a1/api/dm/dmList2', methods=['POST'])
def dmList2():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "ce760458ebfd0d26b99416002e15e6b8",
  "data": {
    "time": 1743487989,
    "lists": [
      {
        "guild_id": "0",
        "icon": "",
        "name": "",
        "type": null,
        "user_icon": [],
        "recipient_id": "448828939389894656",
        "channel_id": "547368740443254785",
        "top": 1741244247,
        "top_sort": 1741244247,
        "offline": 0,
        "status": 0,
        "stick_sort": 0,
        "stranger_state": null,
        "flags": 0
      }
    ]
  }
})

@app.route('/api/a1/api/blacklist/getBlacklist', methods=['POST'])
def getBlacklist():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "29854c077d32f4f1bfa18077ba7ae18f",
  "data": []
})

@app.route('/api/a1/api/relation/list', methods=['POST'])
def relation_list():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "f0c21ad1fbd814ddbb96607a5cfb3cc4",
  "data": [
    {
      "user_id": "513621760122671104"
    }
  ]
})


    
@app.route('/api/a1/api/userSetting/get', methods=['POST'])
def userSetting_get():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "ebe72417da1e9ddc8452e2c0f51f38f4",
  "data": {
    "user_id": "513621760122671104",
    "default_guilds_restricted": false,
    "friend_source_flags": {
      "all": true,
      "mutual_friends": true,
      "mutual_guilds": true
    },
    "restricted_guilds": null,
    "mute": {
      "channel": []
    },
    "guild_notices": false,
    "channel_notices": [],
    "notification_count": false,
    "notification_mute": false,
    "guild_folders": [
      {
        "guild_ids": [
          "317701996708634624"
        ]
      },
      {
        "guild_ids": [
          "303383118843215872"
        ]
      },
      {
        "guild_ids": [
          "433204455396081664"
        ]
      },
      {
        "guild_ids": [
          "545092248111800320"
        ]
      },
      {
        "guild_ids": [
          "359183537678589952"
        ]
      },
      {
        "guild_ids": [
          "400926618899456000"
        ]
      },
      {
        "guild_ids": [
          "387575305969086464"
        ]
      },
      {
        "guild_ids": [
          "395848617346215936"
        ]
      },
      {
        "guild_ids": [
          "481087610740391936"
        ]
      },
      {
        "guild_ids": [
          "533202442159239168"
        ]
      },
      {
        "guild_ids": [
          "429086076850667520"
        ]
      },
      {
        "guild_ids": [
          "474585803709075456"
        ]
      },
      {
        "guild_ids": [
          "543395863498969088"
        ]
      },
      {
        "guild_ids": [
          "614418133188726784"
        ]
      },
      {
        "guild_ids": [
          "643030421772554240"
        ]
      },
      {
        "guild_ids": [
          "283767513341235200"
        ]
      }
    ],
    "guild_positions": [
      "317701996708634624",
      "303383118843215872",
      "433204455396081664",
      "545092248111800320",
      "359183537678589952",
      "400926618899456000",
      "387575305969086464",
      "395848617346215936",
      "481087610740391936",
      "533202442159239168",
      "429086076850667520",
      "474585803709075456",
      "543395863498969088",
      "614418133188726784",
      "643030421772554240",
      "283767513341235200"
    ],
    "receive_stranger_message": true,
    "receive_friend_request": true,
    "dm_notices": [
      "1296514193",
      "597066047220469760",
      "559644180427952128",
      "547368740443254785",
      "523835033602355200",
      "517311686743810048",
      "515864631756312576",
      "514749863922352128",
      "514369403392221184",
      "514251448528523264",
      "513635080552697856",
      "657974566043631616",
      "697759564862709760",
      "731015233950576640"
    ],
    "guild_notices2": {
      "474585803709075456": 0,
      "317701996708634624": 0,
      "433204455396081664": 0,
      "359183537678589952": 0,
      "303383118843215872": 0,
      "400926618899456000": 0,
      "395848617346215936": 0,
      "481087610740391936": 0,
      "429086076850667520": 0,
      "387575305969086464": 0
    },
    "channel_notices_all": [],
    "new_notice": "3",
    "personalized_recommendation": true,
    "allow_view_follow": true
  }
})

@app.route('/api/a1/api/user/getUser', methods=['POST'])
def getUser():
    # 读取请求体的user_ids的值
    user_ids = request.json.get('user_ids')
    print(user_ids)
    # 读取 JSON 文件
    with open('user.json', 'r',encoding='utf-8') as file:
        data = json.load(file)
    # 查找对应的用户数据
    user_data = []
    for user in data['data']:
        if user['user_id'] in user_ids:
            user_data.append(user)
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "67eb893ce5e095.77711760",
  "data": user_data,
})
    
@app.route('/api/a1/api/announce/info', methods=['POST'])
def announce_info():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "67eb893ce5e095.77711760",
  "data": []
})
    
@app.route('/api/guild/guild/zhuli/getHierarchy', methods=['POST'])
def getHierarchy():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "成功",
  "desc": "",
  "request_id": "f536b8dfc228d5237af10ebd7b675c05",
  "data": {
    "config": {
      "hierarchy0_points": 20,
      "hierarchy1_points": 50,
      "hierarchy2_points": 150
    },
    "guild_list": [
      {
        "guild_id": "433204455396081664",
        "hierarchy": 0,
        "points": 1
      }
    ]
  }
})
@app.route('/api/a1/api/pullMsg/pullMessage', methods=['POST'])
def pullMessage():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "67eb893ce5e095.77711760",
  "data": ""
})
@app.route('/api/a1/api/relation/totalUnread', methods=['POST'])
def totalUnread():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "0fb8c280509c2a08fe5b54973987cc5b",
  "data": {
    "count": 0
  }
})
    
@app.route('/api/a1/api/message/TopList', methods=['POST'])
def TopList():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "3567eb77e26f18014f8c9f1081fcf473",
  "data": {
    "records": []
  }
})
@app.route('/api/a1/api/message/getList', methods=['POST'])
def getList():
    # 获取请求体中的channel_id
    channel_id = request.json.get('channel_id')
    # 读取 JSON 文件
    with open('message.json', 'r',encoding='utf-8') as file:
        data = json.load(file)
    # 查找对应的消息数据
    message_data = []
    try:
        message_data = data[channel_id]
    except:
        message_data = [{
  "channel_id": "748088273783869440",
  "message_id": "748088274463346688",
  "content": "{\"type\": \"start\"}",
  "user_id": "389320179948986368",
  "quote_l1": null,
  "quote_l2": null,
  "guild_id": "545092248111800320",
  "reactions": [],
  "recall": null,
  "pin": "0",
  "nonce": null,
  "mentions": null,
  "mention_roles": null,
  "mention_everyone": null,
  "reply_markup": null,
  "message_card": null,
  "deleted_user": null,
  "deleted": null,
  "extra_data": null,
  "display_role_id": null,
  "message_reference": null,
  "quoted": null,
  "time": gettime(),
  "recalled": 0,
  "author": {
    "nickname": "王大哥",
    "username": "4562997",
    "avatar": "https://fb-cdn.fanbook.cn/fanbook/app/files/service/headImage/5444a0a72e787ca35d1b62dfe6910afe.png",
    "avatar_nft": null,
    "bot": false,
    "flags": 2
  },
  "member": {
    "nick": null,
    "roles": [
      "545092248220852224"
    ],
    "guild_card": []
  }
}]
    # 倒序排列消息数据
    message_data.sort(key=lambda x: x['message_id'], reverse=True)
    
    return jsonify({
    "status": true,
    "code": 1000,
    "message": "1000",
    "desc": "\u6210\u529f",
    "request_id": "db58aa472fe794b396a3aad4e358898b",
    "data": message_data}
    )

@app.route('/api/a1/api/bot/getBot', methods=['POST'])
def getBot():
    # 从请求体中获取 bot_id
    bot_id = request.json.get('bot_id')
    print(bot_id)
    # 读取 JSON 文件
    with open('bot.json', 'r',encoding='utf-8') as file:
        data = json.load(file)
    # 查找对应的 bot 数据
    bot_data = []
    for bot in data['data']:
        if bot['bot_id'] == bot_id:
            bot_data.append(bot)
            
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "67eb893ce5e095.77711760",
  "data": bot_data[0]
})

@app.route('/api/a1/api/invite/codeInfo', methods=['POST'])
def codeInfo():
  # 读取codeInfo.json
    with open('codeInfo.json', 'r',encoding='utf-8') as file:
        data = json.load(file)
    # 获取请求体中的code
    code = request.json.get('c')
    # 查找对应的code数据
    guild_id = None
    post_id = None
    expire_time = "0"
    status="0"
    inviter_id=""
    for item in data['data']:
        if item['code'] == code:
            guild_id = item['guild_id']
            post_id = item['post_id']
            expire_time = item['expire_time']
            status=item['status']
            inviter_id=item['inviter_id']
            break
        
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "233ec5f0cc5fffd60acd7d784ed02c9f",
  "data": {
    "channel_id": "0",
    "guild_id": guild_id,
    "post_id": post_id,
    "is_used": "1",
    "number": "-1",
    "expire_time": expire_time,
    "inviter_id": inviter_id,
    "type": "0",
    "status": status,
    "extra_data": "",
    "is_current_user": "0",
    "channel_on_del": "0",
    "banned_level": false,
    "is_new_permission": 1,
    "invite_permission": 1,
    "is_joined": false
  }
})
    
@app.route('/api/a1/api/guild/getInfo', methods=['POST'])
def getInfo():
    # 读取 JSON 文件
    with open('guild.json', 'r',encoding='utf-8') as file:
        data = json.load(file)
    ginfo = None
    try:
        # 获取请求体中的 guild_id
        guild_id = request.json.get('guild_id')
        print(guild_id)
        ginfo=data[guild_id]
        return jsonify({
    "status": true,
    "code": 1000,
    "message": "1000",
    "desc": "成功",
    "request_id": "233ec5f0cc5fffd60acd7d784ed02c9f",
    "data":ginfo})
    except:
        return jsonify({
            "status": false,
            "code": 1001,
            "message": "1001",
            "desc": "参数错误",
            "request_id": "233ec5f0cc5fffd60acd7d784ed02c9f",
            "data":ginfo
        })
            
    
@app.route('/api/a1/api/verify/info', methods=['POST'])
def verify_info():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "8b44667ff138f20ab3a84cbf0d4ed697",
  "data": {
    "guild": {
      "guild_id": "100001",
      "name": "test",
      "icon": "https://fb-cdn.fanbook.cn/fanbook/app/files/chatroom/image/a9d18ca46e82db253666deb8d838729c.png",
      "description": "",
      "member_count": 1145,
      "verification_level": 1,
      "user_pending": false
    },
    "verify_info": {

    }
  }
})
    
@app.route('/api/a1/api/guild/join', methods=['POST'])
def guild_join():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "518a9d84848d0e3070965d3b861564b5",
  "data": {
    "inviter": "389320179948986368",
    "code": "PmIGWFDj",
    "order": 1908,
    "guild_note_channel_id": "3651483424"
  }
})

@app.route('/api/a1/api/guild/getGuild', methods=['POST'])
def getGuild():
    # 读取 JSON 文件
    with open('guild2.json', 'r',encoding='utf-8') as file:
        data = json.load(file)
    ginfo=None
    try:
        # 获取请求体中的 guild_id
        guild_id = request.json.get('guild_id')
        print(guild_id)
        ginfo=data[guild_id]
        return jsonify({
    "status": true,
    "code": 1000,
    "message": "1000",
    "desc": "成功",
    "request_id": "233ec5f0cc5fffd60acd7d784ed02c9f",
    "data":ginfo})
    except:
        return jsonify({
            "status": false,
            "code": 1001,
            "message": "1001",
            "desc": "参数错误",
            "request_id": "233ec5f0cc5fffd60acd7d784ed02c9f",
            "data":ginfo
        })

# 发送消息/api/a1/api/message/clientSend/387575305969086464/387575306023600131(服务器id/频道id)
@app.route('/api/a1/api/message/clientSend/<string:guild_id>/<string:channel_id>', methods=['POST'])
def clientSend(guild_id,channel_id):
    # 获取请求体中的消息内容
    message = request.json.get('content')
    print(message)
    msgid=fbid()
    # 读取 JSON 文件
    with open('message.json', 'r',encoding='utf-8') as file:
        data = json.load(file)
    message={
  "message_id": msgid,
  "guild_id": "433204455396081664",
  "channel_id": "433212507046281216",
  "type": 0,
  "user_id": "513621760122671104",
  "content": message,
  "quote_l1": null,
  "quote_l2": null,
  "reply_markup": null,
  "status": 0,
  "pin": "0",
  "recall": null,
  "nonce": "748084269234067660",
  "mentions": null,
  "mention_roles": null,
  "ctype": 0,
  "deleted": null,
  "deleted_user": null,
  "display_role_id": null,
  "quote_write": true,
  "mention_everyone": null,
  "message_card": null,
  "extra_data": "",
  "time": gettime(),
  "recalled": 0,
  "reactions": [],
  "author": {
    "nickname": "wdgTest",
    "username": "14211359",
    "avatar": "https://fb-cdn.fanbook.mobi/fanbook/app/files/service/headImage/529a2573796da9983810f67aa1230cd0",
    "avatar_nft": null,
    "bot": false,
    "flags": 0
  },
  "member": {
    "nick": null,
    "roles": [
      "433225883453489152",
      "523343798802427904",
      "528814335771127808"
    ],
    "guild_card": []
  }
}
    # 添加消息到对应的频道
    if channel_id in data:
        data[channel_id].append(message)
    else:
        data[channel_id] = [{
  "channel_id": "748088273783869440",
  "message_id": "0",
  "content": "{\"type\": \"start\"}",
  "user_id": "389320179948986368",
  "quote_l1": null,
  "quote_l2": null,
  "guild_id": "545092248111800320",
  "reactions": [],
  "recall": null,
  "pin": "0",
  "nonce": null,
  "mentions": null,
  "mention_roles": null,
  "mention_everyone": null,
  "reply_markup": null,
  "message_card": null,
  "deleted_user": null,
  "deleted": null,
  "extra_data": null,
  "display_role_id": null,
  "message_reference": null,
  "quoted": null,
  "time": 0,
  "recalled": 0,
  "author": {
    "nickname": "王大哥",
    "username": "4562997",
    "avatar": "https://fb-cdn.fanbook.cn/fanbook/app/files/service/headImage/5444a0a72e787ca35d1b62dfe6910afe.png",
    "avatar_nft": null,
    "bot": false,
    "flags": 2
  },
  "member": {
    "nick": null,
    "roles": [
      "545092248220852224"
    ],
    "guild_card": []
  }
}]
        data[channel_id].append(message)
    
    # 将更新后的数据写回文件
    with open('message.json', 'w',encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    return jsonify({
  "action": "arrival",
  "data": {
    "time": gettime(),#时间戳保留整数
    "message_id": msgid,
    "status": 0,
    "assist_level": 0
  },
  "ack": -1,
  "seq": 0,
  "status": true
})
    
@app.route('/api/a1/api/file/cosTmpKey', methods=['POST'])
def cosTmpKey():
    return jsonify({
  "status": true,
  "code": 1000,
  "message": "1000",
  "desc": "成功",
  "request_id": "1042b3d3095d18ce0ae1b080c6f8e9de",
  "data": {
    "app_id": "1251001060",
    "bucket": "fanbook-1251001060",
    "token": "DICLieXSSVw60ePrpHLWboVK5uOnaxga5adfa12d95175ab5ac86422b7c2ed55aJzwkQSlPEPDxR6oGtnyOuqAshqrOM5YClUUgUZoCLiSj06V-VXRfi1nSiH6kPnVdhexOR7D5Li0KjpmfhD1vv9WKqzv0lQv3RA7NrLUWibI8Guk2JlhWqz27Huv-1V6ZhEyxQ_799Y-rUDlruGoXEQqBkcrAWXIPoL0bAj8VVzynUdu-LliE7nm3Jc9RpWo47hlfBNYGrx4xT6T8GuYmMgdBck-3BWSniUvkFZsmuAN8qlWW047BGCzdfI27Hd0hlV7tHyvfJLVBliLJMBh1j_ugbtN-tkqOf705JJGRSzsncRf0dmkZLDCUEVxoDKzg2otUEDLHsSQEzRoSnoCAcFWZCYnxwnvVK1hJXo0CzfXG2WCWlkJdj6jAw_cASGjnSZxAmZ6G17_ZLQurIOTyc3JmuoJCH-9xvWsOH0fdgN9y8nng6hZa8_sp2xh38xiFO72nlAyzVpp74o3kMSz_qS9ZO7nCJWyS15HGOT3oK4JLgx1ovY40x8FACO7pNi5QjvjREtQmDMBjYmawVAG0PvSUdBXzOiDQTL3O1X8TI3GIABlzcl5nHFARAzAs_E5BdSi4hoReoDqcfQQyMAR8hPKoy1xZtH1diYTcmKp5yo0uvgXfPNrn1JTcgSDTso_HuTIRmtvorklX02MCEuOd9lUoY_CV9cYTsF-sf4yIC5GOGPM8kzSEJFbFYnnR59fT2UK2AM-BFH34oex8Di5kViH1Kx9SZdcPGep4FJLlMiQ",
    "host": "https://fanbook-1251001060.cos.accelerate.myqcloud.com",
    "url": "https://fb-cdn.fanbook.cn",
    "secretId": "AKID73d6SPrQWWnfubWnu5NA8fvGyqb35g16aSPcgmBW7sO1u-wrBCfISnFOQEE8U1s1",
    "secretKey": "ulCJWZbOs42zLffd1WA0uhfK6YSe54vHIZv/Fg9aXvuc4NSO9aHKY+eBzQ/nNhMRaF6HhL/sd9nJD73O8EpmHI0AWCeFV6ngpdgP7ugTaAJuNeX3G3OUPOqpJyfOUyC6DbkMsSv7N2ubwLJlTkR25C0WHds9MM+sFPvRscRJ/Ic=",
    "audit_app_id": "1251001060",
    "audit_bucket": "fanbook-video-1251001060",
    "audit_token": "DICLieXSSVw60ePrpHLWboVK5uOnaxgacbce9c4643fa7b3614b06ce427ddef41JzwkQSlPEPDxR6oGtnyOuqAshqrOM5YClUUgUZoCLiSAY5W0P8JEDvUVLOwcrL4MRCr7OHoBfdUXG3QLkUpU3DgpIEOzTheNoFapw-PBMRW5PUw9fFRfysDv64z8hDi_H46ZMq5nXFPkQFad8zYKsE5V4Vu9ywZlTiUR0lZbC0DaSCXiIHl-7AZrj6k6qfpcErATm45LIn7zwVJU1rG07QCy_mZIAggQ83k6fmHVyMhRLYw7-ctQSiCr68W8XR1YCv55FXHzCV4gQeWuYjcoOYAUNwTgbDTkAbJ1VzjdwwhyLj-VwMrc3B3Qvx-vOru2zmtZDdxbDrXHXPENkcTliZbwdkZ1s2RfJKB9NVR0FBQk3JoH4518Brko-WKbiB785GXpfe_gC1e1EzAk86fZFk9zmBcIKRPzQeyG7S_ez8TVo3qPEW8NHB5D2QKapYKwHquGvCzqFmJtiyVd3oA1nnVXI10XX7tjJB4UZG97AFaa1r7Lmrev3QgA27MHK1wGTPNq73lmp4RjBlf-N4ZloQf4_bjCDMDUCe8zzsdfSxH_SVZs7d5QwZ15o7qePJNwXkmMHj8NUb5B56O5ksZTz-LiOEN3oOEZY9PRY6jOLIhV_wYUQdoVbi50cwU_23-2_zv3Gq5cX2FDPXH9wb-PKRYWAqkX01pR4TTxkpPQLW5xg76yVZA7bgrlt0Cnv07TXYRL5yzvI91g8IeVHEU2fSML5nAxUWP0mcmahf3_jF1ZvJEzgkwgYLTEq1T7eea5",
    "audit_host": "https://fanbook-video-1251001060.cos.accelerate.myqcloud.com",
    "audit_url": "https://fb-cdn-video.fanbook.cn",
    "audit_secretId": "AKIDv8tGHSWSCGkjAy5BMCqNk8kU7NbV5FU0AQOLLRtxVWIw8g8YVoqmisThMnjllcAa",
    "audit_type": "video,audio,picture,document",
    "audit_secretKey": "ubrnaQg1l6pMbGXLAgzxdwFNJhm/Xd9KOwqpClgSM+12WtowpUWZ9eQvapI7ebtoR76WEh9qogYUAFEyB/tWH2FxFZnMydkhEhah1xc/sVU/JNN+tZw7b5uAJC2IOOU9kmetdTSHdhh8Y9cVO5dQgQms13Qn9OBDDuz/dgobuWs=",
    "upload_path": "fanbook/app/files/chatroom/",
    "upload_path_service": "fanbook/app/files/service/",
    "expired_time": 1743623967,
    "start_time": 1743580767
  }
})

@app.route('/api/a1/api/user/updateInfo', methods=['POST'])
def updateInfo():
    # 获取请求体中的数据
    avatar= request.json.get('avatar')
    nickname = request.json.get('nickname')
    gender=request.json.get('gender')
    # 从请求头获取authorization
    authorization = request.headers.get('authorization')
    # 获取login.json中


if __name__ == '__main__':
    app.run(port=5111)
