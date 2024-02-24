import json
with open('sample-data.json') as f:
    data = json.load(f)
print("Interface Status")
print("=======================================================================================")
print("DN                                                 Description           Speed    MTU   ")
print("-------------------------------------------------- --------------------  ------  ------")
for info in data['imdata']:
    dn = info['l1PhysIf']['attributes']['dn']
    descr = info['l1PhysIf']['attributes']['descr']
    speed = info['l1PhysIf']['attributes']['speed']
    mtu = info['l1PhysIf']['attributes']['mtu']
    print(f"{dn:<52}  {descr:<18}  {speed:<6}  {mtu:<4}")