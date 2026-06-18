

import json

with open ("C:\\Users\\Lenovo\\Desktop\\PP2\\Practice4\\JSON\\sample-data.json", "r", encoding="utf-8") as f:
  data = json.load (f)


data = (data ["imdata"])

print ("Interface Status")
print ("================================================================================")
print ("DN                                                 Description           Speed    MTU")
print ("-------------------------------------------------- --------------------  ------  ------")

for i in range (len (data)):
  for j in data [i]:
      tmp = data [1]["l1PhysIf"]["attributes"]
      print (tmp ["dn"], "                         ", tmp ["descr"], " ", tmp ["speed"], " ", tmp ["mtu"])
