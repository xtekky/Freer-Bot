import hashlib,re,requests, sys, base64, random, time, io
from urllib.parse import unquote
from utils.pycryptojs import CryptoJS; CryptoJS = CryptoJS()
from PIL import Image

while True:
    session = requests.Session()

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'

    req = session.post(url = "https://homedecoratione.com/v4.php",headers = {
        "x-requested-with": "XMLHttpRequest",
        "user-agent": user_agent,
        "origin": "https://homedecoratione.com/",})

    working = True
    while working:
        try:
            working = True
            sessid = requests.utils.dict_from_cookiejar(session.cookies)["PHPSESSID"]
            print("[ID-{}]".format(sessid))
            req = session.post(url = "https://homedecoratione.com/v4.php",headers = {
                "x-requested-with": "XMLHttpRequest",
                "user-agent": user_agent,
                "cookie": f"PHPSESSID={sessid}",
                "origin": "https://homedecoratione.com/",})

            json_data = CryptoJS.jsonify(req.text)
            key       = CryptoJS.encode_key(user_agent)
            decrypted = CryptoJS.decrypt(json_data, key)
            data      = CryptoJS.format(decrypted)

            response = session.get("https://homedecoratione.com/captcha.php",
                headers={
                    "origin": "https://homedecoratione.com/",
                    "user-agent": user_agent,
                    "x-requested-with": "XMLHttpRequest",
                    "cookie": f"PHPSESSID={sessid}"
                },
                params={
                    "_CAPTCHA": "",
                    "t": f"{round(random.random(), 8)} {int(time.time())}"
            })
            try: image = Image.open(io.BytesIO(response.content)); image.save("captcha.png")
            except: continue #sys.exit("wrong captcha")

            # image.show()
            jd =  {
                "requests": [{
                    "image": {
                        "content": str(base64.b64encode(response.content).decode())
                    },
                    "features": [{"type": "TEXT_DETECTION"}]
                }]
            }

            r = requests.post(
                url = 'https://content-vision.googleapis.com/v1/images:annotate',
                headers = {
                    'x-origin': 'https://explorer.apis.google.com',
                },
                params = {
                    'alt': 'json',
                    'key': 'AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM',
                },
                json = jd
            )

            captcha_answer = r.json()['responses'][0]["textAnnotations"][0]["description"]
            #r = requests.post(
            #    url = "https://api.xtekky.com/ocr",
            #    json = {
            #        "image": base64.b64encode(response.content).decode(),
            #    }
            #)

            #captcha_answer = r.json()["captcha"]["answer"]
            print(f'Captcha: {captcha_answer}')

            url_data = CryptoJS.parse(data, captcha_answer).split("&")


            validate_captcha = session.post(
                url = "https://homedecoratione.com/v4.php", 
                data = {
                    url_data[0].split("=")[0]: url_data[0].split("=")[1],
                    url_data[1].split("=")[0]: url_data[1].split("=")[1],
                    url_data[2].split("=")[0]: captcha_answer,
                    url_data[3].split("=")[0]: json_data#'{"ct":"1vzGiE9962WWuPHESjAhCnp/dUnyy75eHNH0RgrdjkJ0vrZrOMsjXP/I1kM17RgqgQyBJiU5Ig4VcAH3/+Vabhz0UwtkZsDXZLUhOgG+9wYQbtcvfnLEKkeVVgjxZnny0KwunyfFTEfivIQnEqnvdLqCF4BSeKlRWVGkT9KtOXWfdTqjiiDLjhP4VClF1vZEzkhDtEqQDenwBIK5d/ZjKk88Yso38kVAPUWiW79oe+fWQUAUTg/yWj/S5e5MDTKZjxW38Vs0Y8e7IkWXPheJAfvOUijkLGVUx4yC5YqjhPAzYJmQpovZyV4ceiXLEyy/+GwngE2ro/fsd9qUtpdzJprOx/hzaEDXSqTh6R2bgwHZ+Vzd4JlYGL8e5kYs5F0uE/dLe5Db0BwdFSL6oQLPyBE7JUnWRdFgorBG9zyXjQvy16JHK7qx0ffRXoVCqwtctsPh5TaxyqT9UtTrrV0vSKY5TmxbrLBN2zpK/BYa/KU3UtKvCHGNT/0vlNX7hdRbTRll9y30gI4dnKqiLLNVJN1i48uerBB/lESOBrm/Ksrs/NJ8D8m+JuM7wHMSUnNmqqS67UyzkfhZBF2NL3hCA/qOgqauw1pKRpPmh9YKDeExWYZWEwPV7Wh6/EAjQE+WuznR9nvsQca6NTLW9yppvvYAkHp0Wqe01nQvaTd8NOrMyKmRewkigkI/Nfe/OyS6Yv963Ofld+MV/dFsrpZmDUNYtxiUfxarEpGPV/R6v5s0v2bFtE+4nuaSmI70fhWGcdvKYxC/ErI3L6c9+KdsoZ/0zd7sRg6Jb4/1oQvBjswy3coLyk5UuZn00Z5LN1StrRZcgdaUStJnM76FoBAY05Umefr3XS3rVFdnNiaH67o+7zanDZ2N/qh3SzNOAbGNfum1gbbtQ6ejWgrEwJIulPv0NiJeX7F+PHKwSzkVJw49/XYu3oNuH2sdDcZZn0uDT8mYXTGr19A04l6V7RYF6F/6k+jDRHC54pdy0jFIttXxXRKjN5dVVPl+7IPImcy8JgeYYCfm94tW/e2npgk63QM47i4paiAR4sHR2jYdpKJ1NprlM6Snmmr1wPJQIGRm+h93MnKrRefDAxFyrpKXDjGaIXsZfDGEy5f0CbvG9Or8N83F+cKIM8cy7T8Xv8R6NQqfz0RouhTvXuxSzcPphLqzRnU3SxLmIOTXOhXzLjX0zp/kDY8FNXIbRw5az37gu1i7V9u+PuRI0wqUC51qtpPYKnQD3xfzPEhgrp8C+K+lHylmBoV4HauN+zKwGLhb4ZGkdM5az0aSlHtFqrpAf1qA/LNqtd+nSynzImrcOcoBZmxqYKU1OWcHDKjeLIo50AIkFHgQ0V8vscs09OV0Nf1SN/WtSrMnXfxleIUyqj2hYjuyF+2WJnskEnqeKyuRaqxSjdqqrcZgcQJ9zUBLAmwj2meSA+EXmbn037EGgc7Z5+W6YOwhxeeu0gf2HW+rk2OqcIKJv5Qj/uFgQc0xRJ9ek/Lnaziy8ZvVscQI8BdCf0+0CMlR5ky+CpcH3/+xFgSokQN87BRVd7NOpaCMrcXoEqal9aFlFUkxVqjTqYiscG6hlxq1lD/0S0Blr51BOTqm5skmdXPcNux9/8TcJR3jONyIMwgS0CzagpXDlQhaiA13HFfcNTf3+7jOEGwm","iv":"c14a1f2a26d2c849960abcb56ea528d9","s":"e4c64f691adce1b0"}'
                },
                headers = {
                    "x-requested-with": "XMLHttpRequest",
                    "user-agent": user_agent,
                    "origin": "https://homedecoratione.com/",
                    "cookie": f"PHPSESSID={sessid}"
                }
            )

            json_data = CryptoJS.jsonify(validate_captcha.text)
            key       = CryptoJS.encode_key(user_agent)
            decrypted = CryptoJS.decrypt(json_data, key)
            data      = CryptoJS.format(decrypted)
            #print(data)

            try: data_param = str(data.decode()).split("zxndnnndje(\\'")[1].split("=")[0]
            except: working=False ; continue
            
            captcha_work = True
            while captcha_work:
                captcha_work = True
                print(".")
                search_video = session.post(
                    url = "https://homedecoratione.com/v4.php", 
                    data = {
                        data_param: 'tok_free'
                    },
                    headers = {
                        "x-requested-with": "XMLHttpRequest",
                        "user-agent": user_agent,
                        "origin": "https://homedecoratione.com/",
                        "cookie": f"PHPSESSID={sessid}"
                    }
                )

                json_data = CryptoJS.jsonify(search_video.text)
                key       = CryptoJS.encode_key(user_agent)
                decrypted = CryptoJS.decrypt(json_data, key)
                data      = CryptoJS.format(decrypted)
                #print(data)
                if "10 minutes" in str(data):
                    t_s= int(str(data).split("ltm=")[1].split(";")[0])
                    print(f"Sleeping for {t_s} Seconds")
                    time.sleep(t_s)
                    continue

                vid_id = str(random.choice([7126102921699233051,7126145649317334298,7126170639429274907]))

                try: url_data = str(data.decode()).split("zxndnnndje(")[1][1:].split("&'+$")[0]
                except: captcha_work = False ; continue
                try:
                    search_video = session.post(
                        url = "https://homedecoratione.com/v4.php", 
                        data = {
                            url_data.split('&')[0].split('=')[0]: url_data.split('&')[0].split('=')[1],
                            url_data.split('&')[1].split('=')[0]: 'tok_free',
                            str(data.decode()).split('name="')[1].split('"')[0]: f"https://www.tiktok.com/@aarseetimes/video/{vid_id}"
                        },
                        headers = {
                            "x-requested-with": "XMLHttpRequest",
                            "user-agent": user_agent,
                            "origin": "https://homedecoratione.com/",
                            "cookie": f"PHPSESSID={sessid}"
                        }
                    )            
                    json_data = CryptoJS.jsonify(search_video.text)
                    key       = CryptoJS.encode_key(user_agent)
                    decrypted = CryptoJS.decrypt(json_data, key)
                    data      = CryptoJS.format(decrypted)
                    #print(data)
                except: 
                    continue    
                try: new_params = '='.join(str(data.decode()).split("zxndnnndje(\\'")[2].split('=')[0:3])
                except: captcha_work = False ; continue            
                #print(new_params)

                send_views = session.post(
                    url = "https://homedecoratione.com/v4.php", 
                    data = {
                        new_params.split('&')[0].split('=')[0]: "tok_free",#"tok_auto",
                        new_params.split('&')[1].split('=')[0]: "views",
                        new_params.split('&')[2]: vid_id#unquote(str(data.decode()).split("zxndnnndje(\\'")[2].split("\\")[0].split("=")[3])
                    },
                    headers = {
                        "x-requested-with": "XMLHttpRequest",
                        "user-agent": user_agent,
                        "origin": "https://homedecoratione.com/",
                        "cookie": f"PHPSESSID={sessid}"
                    }
                )

                json_data = CryptoJS.jsonify(send_views.text)
                key       = CryptoJS.encode_key(user_agent)
                decrypted = CryptoJS.decrypt(json_data, key)
                data      = CryptoJS.format(decrypted)

                #print(data)
                
                if "Success!" in str(data):
                    print("2k Views Sent")
                elif "views not working properly now!" in str(data):
                    data = "You have to wait before you can re-send"
                if "You have to wait before you can re-send" in str(data):
                    working = True
                    print("Sleeping 10 Mins")
                    time.sleep(600)
                else:
                    working = False
        except:
            pass
        

#
#Captcha Verification for autoview 
#captcha2_raw = unquote(re.findall(r'base64,(.+)\\\\" class=\\\\"img', unquote(str(data)))[0])
#
#try: image = Image.open(io.BytesIO(base64.urlsafe_b64decode(captcha2_raw))); image.save("captcha.png")
#except: sys.exit("wrong captcha")
## image.show()
#jd =  {
#    "requests": [{
#        "image": {
#            "content": str(captcha2_raw)
#        },
#        "features": [{"type": "TEXT_DETECTION"}]
#    }]
#}
#
#r = requests.post(
#url = 'https://content-vision.googleapis.com/v1/images:annotate',
#headers = {
#    'x-origin': 'https://explorer.apis.google.com',
#},
#params = {
#    'alt': 'json',
#    'key': 'AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM',
#},
#json = jd
#)
#
#captcha_answer = r.json()['responses'][0]["textAnnotations"][0]["description"]
#
#print(f'Captcha: {captcha_answer}')
#
#url_data = unquote(re.findall(r"zxndnnndje\(\\'(.+)=\\'\+", unquote(str(data)))[0]).split("&")
#
#
#validate_captcha = session.post(
#    url = "https://homedecoratione.com/v4.php", 
#    data = {
#        url_data[0].split("=")[0]: url_data[0].split("=")[1],
#        url_data[1].split("=")[0]: url_data[1].split("=")[1],
#        url_data[2].split("=")[0]: url_data[2].split("=")[1]+"=",
#        url_data[3].split("=")[0]: captcha_answer
#    },
#    headers = {
#        "x-requested-with": "XMLHttpRequest",
#        "user-agent": user_agent,
#        "origin": "https://homedecoratione.com/",
#        "cookie": f"PHPSESSID={sessid}"
#    }
#)
#
#json_data = CryptoJS.jsonify(validate_captcha.text)
#key       = CryptoJS.encode_key(user_agent)
#decrypted = CryptoJS.decrypt(json_data, key)
#data      = CryptoJS.format(decrypted)
#print(data)
