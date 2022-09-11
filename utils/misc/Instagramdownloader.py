import json

import requests
def instagramdownloader(link):
	url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

	querystring = {"url":link}

	headers = {
		"X-RapidAPI-Key": "fcbb9ba712mshcff1432cfdabadfp108761jsncaf3fda879a5",
		"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	rest = json.loads(response.text)

	if 'error' in rest:
		return 'Bad'
	else :
		dict={}
		if rest['Type'] == 'Post-Image':
			dict['type'] = 'image'
			dict['media'] = rest['media']
			return dict

		elif rest['Type'] == 'Post-Video':
			dict['type'] = 'video'
			dict['media']= rest['media']
			return dict

		elif rest['Type'] == 'Carousel':
			dict['type'] = 'carousel'
			dict['media'] = rest['media']
			return dict
		else:
			return 'Bad'


