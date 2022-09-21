import urllib.request

#Lấy data từ server
weburl = urllib.request.urlopen("http://google.com")
#in ra kêt quả fetching
print("result code: ", weburl.getcode())

#Lấy data
data = weburl.read()
print(data) # html

#Làm việc với json data
urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"

webUrl = urllib.request.urlopen(urlData)
print ("result code: " + str(webUrl.getcode()))

#Nhớ coi thêm json encode and decode trên docs