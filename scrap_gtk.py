from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import datetime

session = requests.session()

login_url = 'https://peerreview.jabarprov.go.id/api-siap-mobile-gtk/api/login?kinerja_session_id=b8zv43d8shfrqi73ciafij5gyd2elmd8v008wcapgw_2880x1800&browser_id=97fba28291f78adcd204e6b389a69203'

payload = {'username': 'user10',
        'password': '123456'
        }

s = session.post(login_url, data=payload)
response = s.text
response_dict = json.loads(response)
token = response_dict['token']

x = datetime.datetime.now()
df_ = pd.DataFrame()

for i in range(11,101):
    data_url = 'https://peerreview.jabarprov.go.id/api-siap-mobile-gtk/api/data-pegawai-gtk?'
    payload_get = {#'params': '%7B%22search%22:%22%22,%22tipeOrder%22:%22akhir%22,%22ascending%22:%22desc%22,%22orderBy%22:null,%22kcd%22:null,%22satuan%22:null,%22sekolah%22:null,%22tipe%22:null,%22nm_gol%22:[],%22tipe_pegawai%22:null%7D',
                'page': '{}'.format(i),
                'perpage': '20',
                'kinerja_session_id': 'b8zv43d8shfrqi73ciafij5gyd2elmd8v008wcapgw_2880x1800',
                'browser_id':'97fba28291f78adcd204e6b389a69203'}
    head = head = {'Authorization': 'Bearer {}'.format(token)}

    req = requests.get(data_url, headers=head, params=payload_get)

    req_dict = req.json()
    req_json = json.dumps(req_dict['data'])
    df = pd.read_json(req_json)
    # df.to_pickle('hasil{}.pkl'.format(i))
    df_ = df_.append(df, ignore_index=True)
    
print(df_)
df_.to_pickle('hasil{}.pkl'.format(x))
    
