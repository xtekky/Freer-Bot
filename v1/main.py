from hashlib        import md5
from base64         import b64decode, b64encode
from random         import choice, random
from string         import ascii_lowercase
from json           import loads, dumps
from Crypto.Cipher  import AES
from requests       import Session, post, get
from re             import findall
from time           import time

class CryptoJS:

    def decrypt(self, data: str, key: str):
        data = loads(data)
        dk   = key.encode() + bytes.fromhex(data["s"])

        _md5   = [md5(dk).digest()]
        result = _md5[0]
        for i in range(1, 3 + 1):
            _md5.insert(i, md5((_md5[i - 1] + dk)).digest())
            result += _md5[i]

        aes  = AES.new(result[:32], AES.MODE_CBC, bytes.fromhex(data["iv"]))
        data = aes.decrypt(b64decode(data["ct"]))
        return data

    def encrypt(self, data: str, key: str):
        data = data + chr(16 - len(data) % 16) * (16 - len(data) % 16)
        salt = b"".join(
            choice(ascii_lowercase).encode() for x in range(8)
        )
        salted, dx = b"", b""

        while len(salted) < 48:
            dx = md5(dx + key.encode() + salt).digest()
            salted += dx

        key = salted[:32]
        iv  = salted[32 : 32 + 16]
        aes = AES.new(key, AES.MODE_CBC, iv)

        encrypted_data = {
            "ct": b64encode(aes.encrypt(data.encode())).decode("utf-8"),
            "iv": iv.hex(),
            "s":  salt.hex(),
        }
        return dumps(encrypted_data, separators=(",", ":"))
    
class Freer:

    def jsonify(self, data: str):
        return (
            "{"
            + data[::-1]
            .replace("58290", ":")
            .replace("90190", '"')
            .replace("56370", ",")
            + "}"
        )

    def encode_key(self, key: str):
        return md5(key.encode()).hexdigest()[5:15]

    def format(self, data: bytes):
        return b64decode(data.decode().split('"')[1].encode())

    def parse(self, data: str, captcha: str):
        parsed1 = str(data).split(r"zxndnnndje(\'")[1].split(r"\'+")[0]
        parsed2 = str(data).split(r"zxndnnndje(\'")[1].split("\\'+")[1].split("\\'")[3]
        parsed = parsed1 + captcha + parsed2

        return parsed

    def _decrypt(self, encrypted_data, user_agent):
        json_data = self.jsonify(encrypted_data)
        key       = self.encode_key(user_agent)
        decrypted = CryptoJS().decrypt(json_data, key)
        data      = self.format(decrypted)
        
        return data
    
    @staticmethod
    def decrypt(enc: str, ua: str) -> str:
        return Freer()._decrypt(enc, ua).decode('utf-8')

class Bot(Freer):
    def __init__(self, awemeId) -> None:
        self.awemeId     = awemeId
        self.reqSession  = Session()
        self.userAgent   = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        self.baseHeaders = {
            "host"              : "freer.es",
            "connection"        : "keep-alive",
            "sec-ch-ua"         : "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
            "accept"            : "*/*",
            "content-type"      : "application/x-www-form-urlencoded; charset=UTF-8",
            "x-requested-with"  : "XMLHttpRequest",
            "sec-ch-ua-mobile"  : "?0",
            "user-agent"        : self.userAgent,
            "sec-ch-ua-platform": "\"Windows\"",
            "origin"            : "https://freer.es",
            "sec-fetch-site"    : "same-origin",
            "sec-fetch-mode"    : "cors",
            "sec-fetch-dest"    : "empty",
            "accept-language"   : "en-US,en;q=0.9",
        }
        
    def solveCaptcha(self):
        captchaResp = self.reqSession.get("https://freer.es/captcha.php",
            headers = self.baseHeaders,
            params  = {
                "_CAPTCHA": "",
                "t": f"{round(random(), 8)} {int(time())}"
        })

        solveResp = post('https://captcha.xtekky.repl.co/', json = {
            'captcha': b64encode(captchaResp.content).decode("utf-8")
        })
        
        print(solveResp.json())
    
    def initSession(self) -> None:
        self.reqSession.post(
            "https://freer.es/v4.php",
            headers = self.baseHeaders
        )
    
    def mainloop(self):
        self.initSession()
        print(self.reqSession.cookies.get_dict())
        self.solveCaptcha()


if __name__ == "__main__":
    Bot('').mainloop()
    
    quit()
    dec = Freer.decrypt(r'09109a45745bd9cd7ab2a091090928509109s0910907365091091e76cd6924907608235bd4b589e4de24091090928509109vi091090736509109=EVHbbtksppsSt1Ug2pYSO2COpRik0t0pgJCD4+WI6PDLz62jt2/\sMZLH2+BPX7oEettMS01uae4b5Ssr17L5JdmiUFpWJxR/\6raoYKAIcGQd2jYv+kgCsAhuVnB1APytGFblGZQUaAmiakveeQSQjfBndjkLiOC4wQWIHZ4f7SeHDAB8GlFuobMnlfutUZNYYkKZIaHKsfZPJqU8zV6Ry/\1T8kKD4wt38VAJQMVjkvbdxyCOU/\PXEpjcblOoETlMFhA4cDE6fprxZuF7ynz7sKfdsQCKPQcsCxuZ07luejUkXkUd9naDATIWc15HGMfohvti3sSftYx3VvobgyMSkdpt0BA5xBDd9kGplKN755zOiMlaLseCZq9bT5D3XQY9fJcW4boPgAldvmWBLzmk7tXdYyDBfROhnblCP/\eIVX8j0Pf8u361oSzvlrqOY4BHtWmqd+rXcEiZ/\clfci7KPumJaNfGV4IuvqnAOGqaKa6Xb5mQqwbYyXvmXd6D8LVcQYa6JdhN4TObN7kyUJOHFtR2GJgUyQ/\WzsSZAvZRN8MISgaD58LILQ2EV7XOEMSBtHLwLl+vyEpE2t1Q1XlaYFCAxIrhSrk+uV9MyZGr68YMltCDeVygZVEF8ChNGU6U3k/\JbDjIa3sgqzXtF6XrHdVQoxQqGdRi8LLj66WwDzDYcuzsMUyoDotQf5V6gbA51Xm+qoNyiUvhet/\+zjDQBAOdWgyIdnqh3NslB167+F2sLvZjPgBD0wIT92DIlG+j+XSyCqfTzDdGaJMVW6l8Jv0pYA6rEhFwKZWqbt8AZsb0S4jIXE6ihCkHCBAilxqRLI/\FqIAfOVaSogDjd4rsc5X+WVa5uld4PBbrqEJCE9/\avyWe6aEDNiGsShpagpR8qe35jXyh6B7seO5JHzgCsL0tSq6HVG6ZIZdQfWfSJSVE/\xscukAJq23MCKNdHKhSDNg7YHbTK72pqJaXByCc2HS6oKZ3xIoYUnyfqQJPDCATTKx/\+F11zh5dUh1sbTpTCDfc2ODTuXQOp2QfYtpHplVQVYPB5xlHTaowdDb3mr8SzCMOTOKgUP/\JWpUL6Jq+BsDR6bJzR36P3/\M/\OMy7mhbqxIozV2/\Lp3x5+gTb1GmSX2KRbBoO5oBYS+xt5F048gVNBD7RTlnrtY2IC9y2vbqHgRKwNFfqwiPEC+akqWAQfkOibQrwhnpnOUTsYsqAkGnbbWM3DXCTvTsTgQlv5CUxfW5gttwQrKTe5eKaq3mfEtZp82tasrY+F+B0g/\p8bJgPeIC3KrDU/\uQbN5gQ1uuC/\Vy3LqYh2lYvUrnGTknid6fWczRgYXRzdMO2YF/\xWKivJqFjHCAPwTjy6NUHZ1SNlOm0k+oGf1oBIvwQ/\5xQk0ieWz/\lEEJCf6ynqeY9BSeYMxtQWPV+qWbmB56iyhIcZkaiJXiyzznh0A1mm7ryJLI4Gjw/\JosQIJFoQVpp4zS9NMBeQEWAijruJMKbOpYPcj3WoiaVqB4CrPmevQpNZWcUz8eqi28aJraUweSIEtxYX3tcqixrvhoAiXBeeiZ6xq8noyyqXv7NARUMEzy56YWYGQOFwLGKEbFi60D9vMgZyMLAnhb7qTqFhxb58W66Vdhk7T2iYgAfYiyOX1T3sIdQVoMtg66CorRFCho29j7Frda7NEiN0XHP2XCBW0BARxfD4kJoGirtoYFB21No6C5F8rEn5EeR3ZlZ+spCG01+tV3KzV9lao/\Y7nagdSKqI5ptB7i7Z0Mw6gatW8ygJKtO1QMcVqvVqwHD3XGcrppRn3iUNhk4Ouo5ral5uIfnWpqgzdOdEjT0cNpF6aTtm1MjQXWsiV67jNrMb9le9n9ghLkenDptHIf3Qa8rgBvdxcOyqP/\ygEIFqjO3WQq6I87R50ycq3iNzPcTO9Zg6A5skjok2eh9caZ2I3ggOuCeSXmCRAgL1GT/\YxznyYwaCaWOyHlqT4M5In+1fhNVBOwvqOVE4GZrTCF0k4oKeLqE2R5exK4D6Y9+zm51hndlgDRs/\DydBVy1t0FwxrTUfHLjAco+Nxb2xZvGwv/\hHCTgwy9v3LwL+Nev3cUCtpfHs6U9xfWxWdzRpGfgjrmL+qTwgN4yBx85tqlFeqd6XL3iKGNAhNS6S/\pALLCA6X0j50hXElzeiJax1zBCDpn7kx4rD7DfrckQzOmpYpU7IhkamJ2bNrGTx+tNjkdnCOZzhxlbB/\orPI/\2voa7iISEdWLh7oZAeO25dxfSGDPqRiSM/\NoEm/\HZBFIFL+oWWteDuRFavISKBZI+P8hOU0vPn2rI033Dx0ha+rBYYo6WrRIv7rNf3jkXwU8J+FfCSJh6AO24n/\PxN5S7MKHIoQ/\vAPbboVeAFJXIUrCXFye7O933aLUCIQERtJNxb4xcBgRtvv6Ju9rejAnK8RE81/\X6QwG2KOOA73nnQ/\PY8ocoQq24er1jPz945GSAyrZsASQBCfu/\OGSrSfEJI/\ubfuyH/\q5r+dR9o7i6yoUz52wqwVYRgflAjHYS9u5f+b2xhMdFMT1hXE9Lsw2+iDcILjtPtziJYrjW0+rtYCXxD323hVzJbcuWIsCEd8LV3stD06v30Dc94vKpm7mPzy4wvrchvHF5t+marjF+HqPaE1ydgVLRtKsuK6RS92h0TN/\pMrAdPhTPpxO8nuzyVMVtppEwkHcQ/\EohjBLXhrzwbLMWgurMkjsCiRsx/\z9N6blFrEDCRw6a4JWnY2oujeW7H/\BCpB6mTxZF2Ich6hJR43GpyoKhTsQt54bQKvI1rx7gYHFtpVt3YxHHWAiuMCjSMLoifYstodSAtWGc17Ot2/\8EoMP5wCzBpU5kvF/\ER/\I0ILCYjgz93WQ7FqxHCHhkh0BSAkEcTlL89Z+UhRCSBhWKaZWYFHc2XXgCUdn+M+eIBTT2x/\e9pS/\Zu9SjTbT04ciAj3q089i1rFicq4leja0bNkMnTbz8I1NW6L7uxGUpYqhDQtRSQRZOB9CQAytQrHdiruF7XGpzYOvMZJoTqf+7eosrJFBNSDEMXVDf/\jHzBBZH8cx2VxdVZQ2MitEbBfMrmvZBNrolL4/\uxgjk8Wf/\nmkPzjLLxb3ZKtWrFqVgjIDRaN9wBYisd7193GeCa3o1jyWQ/\t2SHpsFgc08Wojftoszw00YiTrNtXKDSFoznFpAb/\NiVYHU2XKnYMfVncYqufq3G8jUIYpvQtnx6ID0I6ldyOCj6ElbtMqEehNenNp3aurhonDfao7PwB+Ty8r7tWbVA/\XDIkyfM+Qyg4MZCVBbdS4xpawquB+2IfCuxfF4Fdp+ei+bYq6AkPdQnHxNgehp1BikHH+21BTMAarS6Nivpve3LtknYOYk9sVk/\OLaq0WYOeVwe8FtrsfZk5RRAfLmLYJpFBh+8xZF1FLtDmJ4j0voyDON96qito5WS/\QxRh5AIk0+4UgEo6YQ/\Cjz8a/\xeq72RR2izugkaEEtTGoyTTN6ZeGTs7oc6k9sd0yQk1lMs3zqPVDxxbMkUMTJG+iOAY+n1spWxe5x+/\067ZS5Cb89C92jNX2rbAXsoGXMXJxQVVTiGJ/\KjOa/\9iVo9huAXBQK5YkXnpI6E0pZA7vZbMpXqrAAPfA7VSlgRjY97XBZOU0Ji/\Hg/\g0gvX51xPEYQFFaRN8K5dbcUQiXRpS0j1mPQ1Wj9Soal6A8sMCLMxNhMRP7YcDfcDOmi68U7wfhWpn+txyasaepxTmhMOfetAPBvvcpH/\IjQ6GJ8zys37idZiAxnXJQYWB+T/\+/\fV4ulGKeKKaC+sMBlVkq7EFtVhj9aeCrRt+gQGV9Daj9lWy2p3M2WRGBSxIqr5vrywapvq4/\0TMjrJ+p8XuU8cNq1KFkTBPNST858Q4d3u0yBaZV578ugGNl06K7ugKUfPtLbRbIg0BI5/\PpSvqixwkM6RIbZ2qk/\XiiykTs0M8p1vQ6iM3QY0ocazq/\PRR/\ncxHWJDsgLvcYEBfg9fNANPZpnZdyQgPgVxe0GNFiTaDFjVenj+eYgGOQa04Fs1umRbnvGE1ZVxQ/\BTOHFJls2M96VEIoBj6xVpzLtlX/\k/\ru8DN78yPkE+l5mYfuqH0qUDgziM2HIbPgUBfZNVUI49vKnoBIS3AhVf6HP2wv2fT6fjSUecveJD/\IkkTNo0pW+ijMHWBaQOnbwDKa1UizkObwTK5Q86attZdvCRa+h18RW4+939ygq22HDwn0uxNTcoPgH64gl7Of/\5b4W1JIK4muMUCW7tF/\hCKJ8y0rqTRBP8h/\qQhmk9tJ/\jArKBskgwLavX8RDW/\wZbGJRY0m6eSbYQHndM4Ue7egdJdfG2RjGjpUJ0HMXgNo7nKcArPPIgP/\LFGVuBWWL+6wo+5NPe9au88UpdmAugFU3H1GnWkcaN+86O3OAqyCbdZ9O3b9F+0ZUMQIti13g03Zh5dOsm/\J4B5JDbjdFfzQ8QjvfBg1cTIGQYz1PzklD0zZmEKW6gm9kAHC/\845Z5Kr0nspi9yIjfAneilIWoedy7s2TtNaQm30GS7fW17IRzgoC6GaF/\ZsjATun7ZVEvMqBl/\pmoPWdxUseD9mJS0h7sKDBMZoVTkgM5QsH0YT2dqPsD/\Iszxwa2PcIWobX6Hf82cmWlDfhgPhboH7+5cDEANbjWQ/\rzRVArp+Hw5DJAwfc/\U1NWcSnV8P3mtgH7XjP/\TdrfkxMoxL0QDryNeXG9PUuAwPMXpWwS6Xdaq+y9f43xuMyq+ujo6HBSEu6lAwhgw3c6OsbUeKD7X9J3QCusb6MnnB3cUH9fp63ny2d1mJXofY7OJNfvURJ6sd+uTKbfjELHJ299m4v9oU3O59FaMugV4T9ksK6U6jJyukmRNyfVKu6+rl7VkoC1Y840A6TfsxJW5wybFfB3+6K9YVBestjwq4UD45JuiAUX/\GG1geZsCRiK5D59UE2hebxtMm635YD1JWxFGnZXBf9tAgLlg6SVDDSB53OJawzaRQBix99iXOoHgsrke9e7Jr6rH1BvpC6vBXTTAumhKX/\bNt2OwNXKolwQrG4zrwHzxjuD2ubNoSeB+hkD3oZaftRBJpbjt8eKlw0NL8QaXuHK0ewUqSr55G8PO39aBGbp9YGs44fya451O9JrMYQSNuwjPUf7VDDUoWCaLp13Vx2JsowzInpaveCCp3+HWBtnwM0KkGr0DMH7aBCIbYcLzqyZhB0b9BttXnnR6/\zOkotdWjtxcFGYKEtVD8vdye+GpgCYhYs5PB55rhdcxpW54MSDbwvAKeaGm0PjIx2RvKlN90xJhsYDyYngBI28RT5sEXiMVje8xI5ESctj4MUrD0k+sRl7NGIkooI98YiLICymy2yrT2nP40PQUfsPY+kLcFwPbfSVjnlP/\pxuR0AWt3KOK6CbgRu4L75RHzTozDh+KUJSYH2dQevXkMffY5q0wZeY6P454J0osJ+oIWQAQkY+pwm4+5QxuxIbLp+y5HtgEaEiZVyK0tXFupg+xwcd9G3JZZ+21XXWgjdu/\0fjK2oUemPsRHtJNMcpfXhGI1PBm8P8WdkUCVC5gKbsGlTKXB7ZGJ7zCL+WuW0y6pTybzHvzakq4dOf7V4ZO5WpK2XKeS2zQ0QIq/\sMgXPjLlfAo4cyE7af+/\nWCV5tcLktj256ghCFJMYJVUW74uxVOCjNho6NvaR1A8optQc0iIC8BtMV3eOotzDAZUiBgO+dGo0WexUfd8/\qrgQtX2jhAYUFbTC7CVWbt8kM4B22CWgKqNI3PVEUmjY1HieLbepVRYDuv4xojDCbqKWNOs9qBPCweo+HMOMz75IMK1FO7dyvOG18GrWfhh29o2NcBUpGO1S5/\+sHWL3UrhIrbbjCk+7ZM2g8Z2lsJoAipv9J66sC9croPvKRpRHyh8bgREnXGQs3U+P6h3nseU2D4RBs2VW94umcegn3iu4q7oIpWfqu5NsowOMlpH/\6CnWL13d8yDF0HjSUpVjg+T3cif0FafkXC8/\Suxa7+hct2w8BN4Hk5Bb0xDVzOsC/\Gk5ZhnAVucruOXdbKCEkqgSPO82I7Rh+M2M40QOT2/\gjckBGk69Knkf5YwpMNXhX+AaxRNsJK/\K+DrEvHccbNn9brY+5C0X05I0CqiaN3feH41Fj4tTbJ5dQTAzWk6D50V62UHt6GuuEIFkl7DfJE84xkuRRDFjmCLym04Jn/\Lx+MIrGDgxjKc/\eQma5JaRXjlT6KX/\NKpsXRIh7E++b3KYhBv5e9jwFIyEwBK7pSTl6L1VhvOheK0+NWLbP5raB2npj6sSBmUu9ykARqSQcXvgnjwPRjoawZyhxx5E0sh4KZl52p6WPFTYiaUbBWuiexiAiLI2WbHOYFiSZ+8vZ9oYH90u+ECZKC/\dWwdECpg6n7YkJMadvxEKw2JY9Oz1Ql4J7M7I0pcFcqYghXh5XtBznagkCOtSlmI95pE7K8USjdPXgXpVgCs+kzwFy2XgVq602DMT4T9gpFPOFDH5fIHJk95WnZTAn2L1mUhEu1aZMAb7LjHfZoVlxqmcL/\1ecoRBDBHEcW9W7g2VBMfUPHHWcKhd0StVmn1r9kSUXokpdxImKOwsy6A4f3GvvYHiQZiKop55CBG7noBxkEbHgrbwFDJvn+iGm0Bu5hWYg5SHnD0MNDpkRU7gw5q6b1EeKra+lDctNk6mh8hsIPT3SMwJC4GsJZ3EgrvOJZINdi8qzqfOFXTtM8FdW/\RaKKdKPOXxfuSZ2YNFdmjy0x8b6jZfKH1KmVTBUDd+aiGvgPkohfq1tVmpGVYLePII9l6E4/\DRo5PWE094ykJwCiJ+rphyFOO1j3GSiHJ5Tetspajc0m9BKT7OOlKAmDOlWfvoVl8GN9IEp3a7Z1wSuPQ+8mKI/\xHG+KRMvG/\wHDskZDezWM3X8fRkzmDYoqsOmo0xAbmbXZfTd9vRIYVnQkmnXCayW3DINMiF4q4+aLWcaZ3c0fnKdfMzser1WOTz4pO1HVQIQqf5bdYaYsekKdSDySYGralQ+wksPpt0ztwRru7ffXqXEko9EuOfUGP8ePXIQPoW8EshwMbq4w1HjEKXP00ZkkKhgmOUHzVrvAjyqcJgi9ttipmeGf+gK7d4DcVWKa0gdSDXsHjPsegOXkW8wi5xZwDqzJ6EL2bEF1O6hWWjyuY5VRDT5GqLEPtxQGphB9kJVJLRPWenzX1LWbHm/\K0Eggrikas59qwBgai0HhG7JCVI2YPsM3NaNDBe7uPFukHaHqO8OKntpoNdQnZa+129AbnJb2YI+cTZXUA6wCQUQ5bBSDiN3UMb/\qULqN1tuTjs/\JLX5qolznbjxZyUmA2/\BDZO9KC/\Z2FaPtMPC8PZ0hu54kaFXBvjUvXHN8NIeKPpRQFOlxpejU1NRXptMVZMo+tPmAX5RFMwEnVeQAJ8g5+FsvyUmSeqyaPJYkrzKstlKXXUE8H+RizwAoUflo6QInGQz7UmsOx991qIZshb29O0Q9JyOCOUtIQWXihdTMWbai+1Izuoxu1WU6m+A/\W/\u5bm/\Rss9xBcSSOErZ06pbJwqbOqMzZ98y1q9Tbzhpu1gYjRdGT4rWiAY9pRJbccQlJ4ZKy8x3dP8OUyDUG4e+IpGHO5F8uEadiPHtHCO/\MgDHaRlW5ivlg52zzpWaKCJ/\SKMwQ8vnyahr2+9ZUF6oP/\uXsrzgHpNGWKmLXluRGA62OF0Rkpec3gfV19ygTBjuCFFQGPTWPNCxYWzDl07stNzPI2tnXgEWpHyAG6TKp9dYoOZ/\JhpevtthI6MjEZU3X7ve7Qx1+7dyIldb3wmQZiie/\t7mlIDADscM8fwwejyNlc3cGi1CLd2ffXUTL+eDqqmK2AgC2No9rID4dljcpdaCbbrPzXb2JlEbz/\CJVEoSv2Cu0E3NxbmCb3SZSyLrAUvJHnidWKTVbBWy5wUwyaxdPFaamNInQPmSICiEs+IAvwtSdw6sSTalZNx/\MOuFmLjE7ZrbEoxK+l5BnNekuisuGzapIljj+DcpiFRRaMS1yrnNEPg9x070Vg1zKZIwFHZAgUrxgn58suONmoAv6FKoUuQVg/\XfASK3bfJfOisFxrL8gBFwvuXIsp3AoB69ZkLQ2KNaUnsVkXzHgxxD2qei2e/\txtulx2UZZ7M49D79DTgY1N0vWIwDnhSFwi/\xOzGAEgOJwZv9R5xceB7YH8IWGxpAAxqp2QDHNyqPt47yZ+EzTGceCj5tFcZQxEQMEFnTL3KdpBVtXCdEFeiqt8dlk88fWfeEzdON1/\NS5hDCBb0IqW+0UsJR9uImD0S5OPG/\wlrKBd6sKdROh0WJpqy2xOsFavbOMJ3qW2AbWz/\IXJScIZihDEjYVWnbVgI4AGr90tOtXS6GCpLXIaIWH8ZzlQRiBUOJtgtiszjE7Xd6WNZ34bnEcYmpulOilY6FXFNsdOMkjGJUFB7Dn7WF+9KxHweUcQpoTs/\tQloOh5/\PUBqdxSHTKcocTlbAimXi9A6tDvFjdDHlmtUpouPdVilOXfTJB5wQdKtaRoLobYpwHRi1+idzQZ51ppB2zQxE6UDpvHFe7X88TmdN9NG+KL3V9kjeihNgPFzeOh5wg5RMyNfqj0HhuEas1PnLRSmt5QLXe9lCKHASnB3qRX84JgUvrKBdIe0is5K2Ip7hA2Vf9cFHGYYbELP81345f7joGTnolR16zEDcTVH4JadktAQP5t2hiDYxwbGqx6qgpj/\RbWmDYRnpV+lsA9R2zLrCtfaaismxpGN/\kx6aEKKRTZxE55+x7LgysTO/\9M9tJ4AytXDoNKSY5RYdC8q4ySnTd5m/\J06mTVsqOwDNQJGS2l7U9zcFEV1mTYo7qKFNBBVVhRMy6i7MqS/\IfihzS7w3XucKhoP6gIjYxsoL7pA3x/\W+dUXTs4CdxUEgBnOCq5w2fhQcaI3rXs6DVYwYnlubJ8m3ktc6mCj3KlWZwCvkPTKvYdC1EWWwzq7zSxnkfMIov0dOuFQIGYvT841+FACa0iYkOHrI6mfkY6vjkwdwlGaexyy0lPt61OsHQfCc5I+dAPaef5IV1KVqxEDZ26VfycZFxj4oQTtrtuSy5NDI1W9k/\2UqZJNBSQZJGzqECkVrR5AjyMqjGp3lJThWAS50QnLC4ah9XNNxNk/\RRjQuwHzJBTuRsh4oppEzoHDlNmRYgiV3iMBnh4/\q5Z2iyijPtNNgpkIZwkFUPhGXktBUSheINKXncCqiI4RZFM9p6AazlutNNwAPGQm3V9bwcl6wED3Lim5XKtzHyp1ZnbFPWW0rLC0tTHpSHTDxE047x3CjrBkJOdUwuqqzxFv91RCGDhIKObjOwaE1HX0aLVvrtaKWQAV/\rTfjJtF3Q1a8iEzYBLVprbRbX/\WUcFQqI6HhuqYLMIr3U7k6xspeRXVxnmB2jo7oBO9/\sWFY2U+U+EClrPKexdw9DgfqnfEHFiTQJPdzE1oZ8lAbgGOlW9Oafhy1ww1RT/\47sxaJ+AYl7lOS881Avwy9ROdu+kViuLrweaq5pd0vuoq4vysJZGaqfhScG4bLU/\8uZT1dtS46fD1pkVnUu+KMcCYGtUmlwf+74oBhFJxqG4G8GaIDBgGRWaiBRZVfEPYsuf7l8tiTgnaC0d7RD28g26cPTwLVhwLFqoLHdhqgBYZiv1TWvp2aBh4cB38jvtzZFAuj6gPc2zfzTsp/\th44oi6tamTUARrL/\M0wMLMSqNkKLxfOx2WNR/\ScaIuYYofmRNfjMzFwtwcW3GFy2jNvmUCHPBw/\aht50dNYaVGWVToSEYfI46m4x4AEsklhGYMljmr/\AYWzbyq1gZQp5GwkvB9FhmF/\aHX8JE0M4PszOdnvMrky/\DWdVbbep1bCj/\etiLx+Xv3wQrDZ5MXdhrIQ0CHMTPRcd6qv+HXVFQyQeJmhLYORCPlqHl1hZJ6FInrv42oNf/\FjaEo+2/\lZEfCbnatYTbRnKyUPdrx8vPiT59YgJ0d3xknl0ebQOaMEDVELk5JhJd+eKCQWP8CqvmpvHvwa+sWHRwxNvz6nTwHXD4UnqkUrq7NgA3I9uhWHBEpnRZZ1HFDWMIPUyEvIhb7dqSr4B7b8nW+ELCLGy4mjiA/\GnF1iyrlzb+Ia73GDZP8UlLDGJ7pLA4LNLql3/\dcL2S0edw4ySJCieFCiuwRULmPrx5ZiO3TYpjLr31sirVgp7yBMr2jJNobryoQd5XT3uzfA84bU3fTY0pa9gw51fry3PCw7I5p4oOSLMlfrW8VAWnbEmsVSb8xlg1G9R7a93aHWsCgKjnoZBksEcqQK0TiVHPvIgeXGcE95oaEvcKHinKR3xKFtEWwu2RiL+piBliXGpRm7KIFR6ZiwwuAZM4f9Bgw3fnSuASDIoMp0+tFdOY9mcsUIq8tbJ2UOF1CKew8LULz6XillYYd3pzBx3gIITRBUrYu/\sKYQnMBRfk+b698dZdzJ+/\AnEQeEv9pBQQh50EtWz7uAnTdxNh9uPij7s+U6PGRfob6Q9NzaQOZ1EyhDnOIdk7r5DsIrIGWjzpA0g+F7SkNR/\kObFh5NEXxlLfwZCigntHBAd4ASVVSGQNi3GuZFwIyUDwBgLSpXgDeaMt7tJLJIdTRvzjT8NtrySPG9TFl2IMyIljOwtgluRQxddgMeRBQa1Onn7xdkyQ7+uIewqF8rfkYu0b0QVUJTbN1EsD32/\SJ7jdaK6AoWBhGou9t6CFT4hw5n1L90/\/\9LyIpwj+lx00GYRvVxdse3fqbk852HkK8Dk3ZOMx/\aXGK4w5ZpcYFENSJ8rO3esQReaFLDBjaPueIw4B0IB71DuA/\+wOK33gdm9iPrOcho9urPKkxw3rO6KfXs3QmiUaZdIvtyQrUcqsZqF/\PeZlFAXSyVVWa6SqDS+z58l83C879oh4dsPhS9r7yEWi8sg6piWmQdlfuAeBzX96+k3lke9XZmM5QbMaMn1Hj4rjsLoAt46lD+FSx3YQrMPJpQ23hO/\RxMfpQRCuhietcgjRWM8MjixWFx6Y1ou6rq/\JALx7FdV0NU0KW1KwAHmNNdfbE1oeMwwVHB/\tCAwRhUQSa6l3GCO77JSET1XhRPW0r1+3mEi4XicEu4mjE9ddUODUg809gESbi5c9xuWnOXW+FyLhkbssRRrxmXsV2i4CX4ughYAyg0t2OuyPb6IpTyiC8P3Pav4NII/\/\qaOE0CIPZeA4sw6sFsoBvj7e7w57m5VKfduOSryQfslphgOjJeqWCq8jJVDJgto8q5HGjmwsFO09x091090928509109tc09109', r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')
    
    args = list(findall(
        """nnndje\('(.*)'\+encodeURIComponent\(\$\("input\[name='captcha']"\)\.val\(\)\)\+'(.*)'\+encodeURIC""",
        dec
    )[0])
    print(args)
    
    captcha_answer = 'test'
    payload = args[0] + captcha_answer + args[1] + ''
    
    print(payload)
