import requests
import pandas as pd

def get_image_tags(image_path):
    api_key = 'acc_995ec2826f834a5'
    api_secret = '87350b4c5ecda284c6d95c2cba6f3b0c'

    response = requests.post('https://api.imagga.com/v2/tags',
    auth=(api_key, api_secret),
    files={'image': open(image_path, 'rb')})
    r = response.json()['result'].get('tags')
    x = pd.DataFrame(r)
    tags = []
    for item in x['tag']:
        tags.append(item.get('en'))

    return (tags)
