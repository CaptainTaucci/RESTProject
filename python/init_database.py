'''
(C) ete&boys 2017

@package rojekts
'''
from pymongo import MongoClient

db=None


def bulk_add():
    bars_list = [{"name": "A21 Coctail Lounge",
            "lon": "24.9350741",
            "lat": "60.1667658",
            "beerprize":"3.5",
            "jagermaister":"3.5",
            "openhours":"Open 17:00-00:00"},
            {"name": "Amarillo",
            "lon": "24.943363",
            "lat": "60.1699405",
            "beerprize":"4.0",
            "jagermaister":"3.0",
            "openhours":"Open 18:00-03:00"},
            {"name": "American Bar",
            "lon": "24.9366677",
            "lat": "60.1677306",
            "beerprize":"5.5",
            "jagermaister":"3.5",
            "openhours":"Open 10:00-21:00"},
            {"name": "Amigo",
            "lon": "24.9477636",
            "lat": "60.1582523",
            "beerprize":"3.0",
            "jagermaister":"2.0",
            "openhours":"Open 12:00-02:00"},
            {"name": "Apollo",
            "lon": "24.937463",
            "lat": "60.168802",
            "beerprize":"5.0",
            "jagermaister":"3.2",
            "openhours":"Open 15:00-00:00"},
            {"name": "Aussie Bar",
            "lon": "24.9306634",
            "lat": "60.1704208",
            "beerprize":"6.5",
            "jagermaister":"4.0",
            "openhours":"Open 20:00-02:00"},
            {"name": "Baker’s Bar",
            "lon": "24.9382992",
            "lat": "60.1678628",
            "beerprize":"4.5",
            "jagermaister":"3.5",
            "openhours":"Open 21:00-02:00"},
            {"name": "Bar Bäkkäri",
            "lon": "24.9260335",
            "lat": "60.1701094",
            "beerprize":"4.8",
            "jagermaister":"3.0",
            "openhours":"Open 21:00-04:00"},
            {"name": "Bar Loose",
            "lon": "24.9350497",
            "lat": "60.1667908",
            "beerprize":"3.8",
            "jagermaister":"2.0",
            "openhours":"Open 19:00-00:00"},
            {"name": "Bones",
            "lon": "24.9391696",
            "lat": "60.163494",
            "beerprize":"6.0",
            "jagermaister":"3.0",
            "openhours":"Open 20:00-02:00"},
            {"name": "Cafe Bar No 9",
            "lon": "24.9397509",
            "lat": "60.1650269",
            "beerprize":"5.2",
            "jagermaister":"3.5",
            "openhours":"Open 12:00-22:00"},
            {"name": "Boothill",
            "lon": "24.9310283",
            "lat": "60.1646309",
            "beerprize":"4.2",
            "jagermaister":"2.5",
            "openhours":"Open 10:00-02:00"},
            {"name": "Club Capital",
            "lon": "24.9318099",
            "lat": "60.1670911",
            "beerprize":"8.2",
            "jagermaister":"4.0",
            "openhours":"Open 22:00-04:00"},
            {"name": "Hercules",
            "lon": "24.9259589",
            "lat": "60.1700591",
            "beerprize":"6.5",
            "jagermaister":"3.5",
            "openhours":"Open 22:00-04:00"},
            {"name": "Steam Helsinki",
            "lon": "24.9309551",
            "lat": "60.1709307",
            "beerprize":"5.5",
            "jagermaister":"2.5",
            "openhours":"Open 20:00-03:30"},
            {"name": "Colorado",
            "lon": "24.9327473",
            "lat": "60.1690952",
            "beerprize":"7.5",
            "jagermaister":"4.5",
            "openhours":"Open 14:00-22:30"},
            {"name": "Eerikin Kulma",
            "lon": "24.9293363",
            "lat": "60.1657849",
            "beerprize":"4.5",
            "jagermaister":"3.5",
            "openhours":"Open 12:00-00:00"},
            {"name": "Molly Malones",
            "lon": "24.9440555",
            "lat": "60.1706207",
            "beerprize":"6.5",
            "jagermaister":"5.0",
            "openhours":"Open 15:00-04:00"},
            {"name": "On the rocks",
            "lon": "24.9429848",
            "lat": "60.1709418",
            "beerprize":"7.0",
            "jagermaister":"6.0",
            "openhours":"Open 18:00-01:30"},
            {"name": "Cafe Mascot",
            "lon": "24.9518714",
            "lat": "60.1816431",
            "beerprize":"7.5",
            "jagermaister":"2.5",
            "openhours":"Open 18:00-00:00"}]
    db.bars.insert_many(bars_list)
    

def dropColl():
    db.bars.drop()
   

def init():
    client = MongoClient('localhost:27017')
    global db
    db = client.BarDB
    bulk_add()

def main():
    init()
    

main()
