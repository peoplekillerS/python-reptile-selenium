#1找到为加密参数         #window.arsea(参数，xxxx,xxx,xxx)
#2想办法把参数进行加密（必须参考网易的逻辑） params==>encText encseckey==>encSecKey
#3请求网易 拿到评论信息
import requests
from crypto.Cipher import AES
from base64 import b64encode
import requests
import json

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

data={
    "crsf_token":"",
    "cursor":"-1",
    "offset":"0",
    "ordertype":"1",
    "pageNo":"1",
    "pageSize":"20",
    "rid":"R_SO_4_1325905146",
    "threadID":"R_SO_4_1325905146"
}

# 服务于d的
e="010001"
f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g="0CoJUm6Qyw8W8jud"
i="7XxnOjm6oaSnpGdB" # 手动固定的 人家函数是随机的

def get_encSecKey(): # 由于i是固定的 那么 encSecText是固定的
    return "9c21fce2ec67d211c983c7f44c3af70c79084daab6797f7f4fff775d4be478144bb1f9a1340327e90ef5a369e727bb99198342cf627d24be067560d67778102a29e02e90164d819e2bb53e9be29476e47d737dc66f39cca0150a1ef057189acb6426cc5f2de35cd1b42ed13e898bb1bafed0cbdbfcdf5a8d480c7258b84e2ea6"

# 把参数加密
def get_params(data): # 默认这里收到的是字符串
    first = enc_params(data,g)
    second = enc_params(data,i)
    return second # 返回的就是params
# 转化成16的倍数，
def to_16(data):
    pad = 16-len(data) % 16
    data += chr(pad)*pad
    return data

# 加密过程
def enc_params(data,key): # 加密过程
    iv="0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"),IV=iv.encode("utf-8"),mode=AES.MODE_CBC) #创建加密器
    bs=aes.encrypt(data.encode("utf-8")) # 加密,加密的内容的长度必须是16的倍数,
    return str(b64encode(bs),"utf-8") # 转化成字符串返回

# 处理加密过程
"""
 function a(a) { #a是要加密的内容
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1) #循环16次 
            e = Math.random() * b.length, #随机数
            e = Math.floor(e), # 取整
            c += b.charAt(e); #取字符串的xxx位置 
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b) #b是密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a) #e是数据
          , f = CryptoJS.AES.encrypt(e, c, {# 缺少一个加密的秘钥
            iv: d, #偏移量
            mode: CryptoJS.mode.CBC #模式是 cbc
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {  #a就是我们的data
        var h = {}
          , i = a(16); # i就是一个16位的随机值,把i设置成定值
        return h.encText = b(d, g), #g是密钥
        h.encText = b(h.encText, i),# 返回的就是params i也是密钥
        h.encSecKey = c(i, e, f), # 得到的就是encSeckey,e和f是定死的 如果此时我把i固定 得到的key一定是固定的
        h
    }
    两次加密
    数据+g=》b =》第一次加密 +i-》b=params
"""

#发送请求 得到响应
resp = requests.post(url, data={
    "params":get_params(json.dumps(data)),
    "enSecKey":get_encSecKey()
})
print(resp.text)
resp.close()




















