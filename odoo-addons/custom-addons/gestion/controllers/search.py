from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    "f_name": "",
    "l_name": "",
    "sexe": "",
    "idendity_card": "",
    "address": "",
    "birthday": "",
    "registration_date": "",
    "email": "",
    "phone": "",
}

resp = es.index(index="you2", id=1, document=doc)
print(resp['result'])

# resp = es.get(index="you2", id=1)
# # print(resp['_source'])

# es.indices.refresh(index="you2")

# resp = es.search(index="you2", query={"match_all": {}})
# print("Got %d Hits:" % resp['hits']['total']['value'])
