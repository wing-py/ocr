import requests
import json


def ocr(filename, overlay=False, api_key='helloworld', language='eng'):
   
    

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    x=json.loads(r.content.decode())["ParsedResults"][0]["ParsedText"]
    print(x)
    return x


