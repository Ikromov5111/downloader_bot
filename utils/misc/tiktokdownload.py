import requests
import json

def tiktokDownload(link):
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "fcbb9ba712mshcff1432cfdabadfp108761jsncaf3fda879a5",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)


    if 'error' in rest:
        return "Bad"
    else:
        dict={}
        dict['video'] = rest['video'][0]
        return dict

