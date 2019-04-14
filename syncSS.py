import json

dest = '/run/media/magnolia/Microsoft/shadowsocks/gui-config.json'
src = '/etc/shadowsocks/shadowsocks.json'

with open(dest) as f:
    DestDic = json.load(f)

with open(src) as f:
    SrcDic = json.load(f)

DestDic['configs'][0]['server'] = SrcDic['server']
DestDic['configs'][0]['server_port'] = SrcDic['server_port']
DestDic['configs'][0]['password'] = SrcDic['password']

with open(dest, 'w') as f:
    json.dump(DestDic, f)
