import urllib.request, time, json, requests
from urlextract import URLExtract
from bs4 import BeautifulSoup

def current_target_url(page, display_start):
    target_url = 'https://www.metal-archives.com/browse/ajax-country/c/SE/json/1'
    target_url += '?sEcho={}&iColumns=4&sColumns=&iDisplayStart={}&iDisplayLength=500'.format(page, display_start)
    target_url += '&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&iSortCol_0=0'
    target_url += '&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true'
    target_url += '&bSortable_2=true&bSortable_3=false&_=1505682951191'

    return target_url

def get_total_records(target_url):
    with urllib.request.urlopen(target_url) as url:
        data = json.loads(url.read().decode())
        total_records = data["iTotalRecords"]

    return total_records

def get_json_data(target_url):
    with urllib.request.urlopen(target_url) as url:
        data = json.loads(url.read().decode())

    return data


def crawler():
    extractor = URLExtract()


    target_url = 'https://www.metal-archives.com/browse/ajax-country/c/SE/json/1'
    target_url += '?sEcho=1&iColumns=4&sColumns=&iDisplayStart=0&iDisplayLength=500'
    target_url += '&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&iSortCol_0=0'
    target_url += '&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true'
    target_url += '&bSortable_2=true&bSortable_3=false&_=1505682951191'

    total_records = get_total_records(target_url)
    json_data = get_json_data(target_url)

    page = 1
    display_start = 0
    current_records = 0

    while current_records <= total_records:
        print("{} / {}".format(current_records, total_records))
        for x in range(500):
            s_json_data = str(json_data["aaData"][x][0])
            extracted_url = extractor.find_urls(s_json_data)
            r = requests.get(extracted_url[0])
            time.sleep(.5)
            soup = BeautifulSoup(r.text, 'html.parser')
            with open('band_pages/{}.html'.format(x), 'w', encoding="utf-8") as bp:
                bp.write(str(soup))
            time.sleep(1)

        page += 1
        display_start += 500
        if current_records + 500 < total_records:
            current_records += 500
        else:
            current_records += total_records - current_records

        target_url = current_target_url(page, display_start)
        json_data = get_json_data(target_url)


if __name__ == '__main__':
    crawler()


    """
    with urllib.request.urlopen(target_url) as url:
        data = json.loads(url.read().decode())
        print(data["aaData"][0][0])

    with open('data.json', 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4)
    """
