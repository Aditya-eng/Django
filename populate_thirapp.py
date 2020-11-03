import os
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE","thirproj.settings")
import django
django.setup()

##Fake populations script
import random
from thirapp.models import Accesrecord, Topic, Webpage
from faker import Faker

fakeit  = Faker()


#Generate 5 random numbers between 10 and 30
randomlist = random.sample(range(10, 30000), 5000)

topic1= ['Search','Home','Games','News','Discord',"Products","topics"]
topic2  = ["Social",'code','HEllO','Cleo county','Flats and apartments']
topic3 = ['podcasts','lenovo','windows10','apple big sur','Bill gates',"steve jobs","marketplace",'twitter','facebook']
topic4 = ['apple','iphoneos',"android",'linux and linus torvalds','cars and automobiles','math']
topic5 = ['Search1','Home1','Games1','News1','Discord1',"Products1","topics1","Socia1l",'code1','HEllO1','Cleo county1','Flats a1nd apartments','p1odcasts','lenovo1','windo1ws10','appl1e big sur1','Bill gate1s',"steve1 jobs","marketplace1",'twitter1','facebook1',
'apple1','iphon1eos',"1android",'l1inux and linus torvalds','cars 1and automobiles','ma1th','cherry county','prateek wisteria','prateek laurel']

topics = topic1+topic4 +topic2+topic3 + randomlist + topic5


def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics)) [0]
    t.save()
    return t

def populate(N=50000000):
    for entry in range(N):
        # get the topic for teh entry
        top = add_topic()

        #Create the afake data for the entry
        fake_url = fakeit.url()
        fake_name = fakeit.name()
        fake_date = fakeit.date()

        webpag = Webpage.objects.get_or_create(topic = top,name = fake_name,url = fake_url)[0]

        #create a fake accesrecord
        acc_record = Accesrecord.objects.get_or_create(name = webpag ,date = fake_date)[0]


if __name__ == "__main__":
    print('populating script! in 10,9,8,7....')
    populate(2)
    print("population completed! ")


