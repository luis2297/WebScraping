import urllib.request, json

target_url = 'https://www.metal-archives.com/browse/ajax-country/c/SE/json/1?sEcho=1&iColumns=4&sColumns=&iDisplayStart=0&iDisplayLength=500&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=false&_=1505682951191'
with urllib.request.urlopen(target_url) as url:
    data = json.loads(url.read().decode())
    print(data["aaData"][0][0])

with open('data.json', 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=4)
