import xml.dom.minidom
import urllib
import os as os

api_key = '&api_key=293255c9bf4ffaaf4af162e345955705'
method1 = '?method=flickr.places.find'
method2 = '?method=flickr.photos.search'
method3 = '?method=flickr.photos.getInfo'

root_input = raw_input('Input your workspace, for example, C:\\Users\\Lu\\Desktop\\PythonUrllib\\ \n')
root = root_input

if not os.path.exists(root+'page'):
    os.mkdir(root+'page')
if not os.path.exists(root+'photo'):
    os.mkdir(root+'photo')
if not os.path.exists(root+'finalist'):
    os.mkdir(root+'finalist')

print urllib.urlopen('https://api.flickr.com/services/rest/'+method1+api_key+'&query=sanya').read()
location_id = raw_input("Input the location id\n")
place = '&place_id=' + location_id

for page in range(1, 28):
    output1 = urllib.urlopen('https://api.flickr.com/services/rest/'+method2+api_key+place+'&page=' + str(page)).read()
    g = open(root+'page\\' + str(page) + '.xml', 'w+')
    g.write(output1)
    g.close()
    DOMTree = xml.dom.minidom.parse(root+'page\\' + str(page) + '.xml')
    collection = DOMTree.documentElement
    photos = collection.getElementsByTagName('photo')
    for photo in photos:
        print '*****Photo*****'
        if photo.hasAttribute('id'):
            print 'Id: %s' % photo.getAttribute('id')
            photo_id = photo.getAttribute('id')
            output2 = urllib.urlopen('https://api.flickr.com/services/rest/'+method3+api_key+'&photo_id=' + photo_id).read()
            f = open(root+'photo\\' + photo_id + '.xml', 'w+')
            f.write(output2)
            f.close()
            DOMTree = xml.dom.minidom.parse(root+'photo\\' + photo_id + '.xml')
            collection = DOMTree.documentElement
            photo_details = collection.getElementsByTagName('photo')
            for photo_detail in photo_details:
                if photo_detail.hasAttribute('id'):
                    if photo_detail.hasAttribute('views'):
                        print '*****Photo Detail*****'
                        print 'Id: %s' % photo_id
                        views = photo_detail.getAttribute('views')
                        print 'Views: %s' % views
                        taken_time = photo_detail.getElementsByTagName('dates')[0].getAttribute('taken')
                        print 'Taken Time: %s' % taken_time
                        latitude = photo_detail.getElementsByTagName('location')[0].getAttribute('latitude')
                        print 'Latitude: %s' % latitude
                        longitude = photo_detail.getElementsByTagName('location')[0].getAttribute('longitude')
                        print 'Longitude: %s' % longitude
                        final_info = photo_id + ',' + views + ',' + taken_time + ',' + latitude + ',' + longitude
                        print final_info
                        p = open(root+'finalist\\finalist.csv', 'a')
                        p.write(final_info)
                        p.write('\n')
                        p.close()