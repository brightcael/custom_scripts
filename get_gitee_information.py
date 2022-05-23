import requests
import json
import csv
from datetime import date
repo_list=[
'linklabdata',
'webide-vscode-extension',
'LinkLab-live-server',
'saas-auth-frontend',
'sim-3d',
'saasfront',
'arduino-avr-mega-virtual',
'fakehub',
'nginx-for-living',
'sso-auth-server',
'saas-mobile',
'virtual-sensor',
'saasbackend',
'webide',
'linklab-ldc'
]
select_time = '2022-05-16T00:00:00+08:00'
save_path='git_commit.csv'

def send_requests(Url,Data,Header):
    return requests.get(url = Url,params = Data,headers = Header)
if __name__ == "__main__":
    f = open(save_path,'w',encoding='utf-8',newline='')
    print(date.today())
    writer=csv.writer(f)
    writer.writerow([str(date.today()) + '记录如下'])
    for repo in repo_list:
        url='https://gitee.com/api/v5/repos/emnets/'+repo+'/events'
        data={
            'access_token':'c09f4bf5426962785d210b04b80ea380',##定期重置token
            'limit':'20'
        }
        headers = {
            'Content-Type':'application/json'
        }
        response = json.loads(send_requests(url,data,headers).text)
        for list in response:
            print(list)
            if list['created_at'] > select_time:
                record=[]
                record.append(list['created_at'])
                record.append(list['type'])
                record.append(repo)
                record.append(list['actor']['name'])
                try:
                    record.append(list['payload']['ref'].replace('refs/heads/', ''))
                    message=''
                    for info in list['payload']['commits']:
                        message+=info['message'].replace('\n','',1)+';'
                    record.append(message)
                except:
                    print('not push event')
                print(record)
                writer.writerow(record)

