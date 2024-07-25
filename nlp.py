import json,os
import types
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models

#填入腾讯云密钥
SecretId = ''
ecretKey =  ''

#打开raw目录下文件
def loadfile(path='raw/2021-03-17.json'):

    f = open(path,'r+',encoding='utf8')
    data = json.load(f)
    f.close()

    all_hot = [ title['title'] for title in data]
    
    return all_hot
    
def nlp_api(params):
    try:
        cred = credential.Credential(SecretId,ecretKey)
        
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile

        client = nlp_client.NlpClient(cred, "", clientProfile)

        req = models.ClassifyContentRequest()
        
        req.from_json_string(json.dumps(params))

        resp = client.ClassifyContent(req)
        
        back = json.loads(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)
    return back
            

def check(path):

    all_hot = loadfile(path)
    outcome = {}
    num = 1
    for trending in all_hot:
        print(num,'/',len(all_hot),end='\r')
        num += 1
        params = {
                "Title": "微博热搜",
                "Content": [trending]
            }
        back = nlp_api(params)
        outcome[trending] = back
    return outcome

if __name__ == '__main__':
    
    path = r'raw\2024-04-27.json'
    data = json.dumps(check(path),ensure_ascii=False)
    path_name = path.split('\\')[1]
    with open('output'+path_name,'a+',encoding='utf8') as f:
        f.write(data)
    
