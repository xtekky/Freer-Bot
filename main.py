from hashlib        import md5
from base64         import b64decode, b64encode
from random         import choice
from string         import ascii_lowercase
from json           import loads, dumps
from Crypto.Cipher  import AES
from requests       import Session
from re             import findall

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
        pass
    
    def initSession(self) -> None:
        self.reqSession.post(
            "https://freer.es/v4.php",
            headers = self.baseHeaders
        )
    
    def mainloop(self):
        self.initSession()
        print(self.reqSession.cookies.get_dict())


if __name__ == "__main__":
    # Bot('').mainloop()
    dec = Freer.decrypt(r'09109b892d639fe596268091090928509109s091090736509109347cac790ee643673051b95689611040091090928509109vi091090736509109=YjR4MUYuC5wYO+7UHE3NUKhlPboJ+CnEVe+JxKKVsISL/\LbIiY4/\Hz/\Tl0ljs0FEnLLZf/\vxW3sYJMk0BBopbfdyA+UNHowslcGiwjuhES6c6qBDUZP8MdhHcmTL3iqHMGwWV8fbLpckGY0S+1FQqxP1dZgreAVAlR037mthqidcJ9qscrkMnTsseghr62v61Tg7oPwU58+1pZZw9A2tBTtuv+yRJiDyinM7+IoCvsUXtgzotcugMpjJvbKjO36Fk0ncT1mgUg+2yAqdcN5RtOiLuzStEaCT8Zj+TD5ErQTu2QqcshzFaj1z4DLNgvGcrINUhzsl9kOSI5skg9suJfg2uKYe+CHjufNePQqxRjAH741dI+pU+yHWPHY5PzB07GV5diEfH3EytjDSsHDf4ASQEzZyIjJXfjRKJ0CserYFFwe0VkZwOCOvsz1kdFUMscOO69Ai+KShjZHV6E0XgqYTBmWxQ6tmnzP28GIEUXNXQSZK/\nhhB5M+RgRmQlx4XXChq5Rs34j+FClcf3fijNXb1Z4rezZ3slX+7c65Ts6QkuSNsCyvSRS4eNgl8HrhSxmCznVTymdHJrcSSBAkKbK9Hfyn8HkeSkU6ehbhcRvlVo8p1nXuNw5dLVAdvi9W9z08MAz/\tI9QebumDi3ieTVPdzG/\uhjIzG7gy2aaeFkZGu2fC6TvG2zWflFqO8aQOE0PqiLc/\gQ2IAvodANHsrV5q4qJ17oI4Ux9qJ+LqafdyAFAUz4G4iNBre7HJg3yjl2fnvT5L1auCuMXC8i1b/\OKdX6p2kpdBCaR8rRJ9AP8JVUF9DVqkxCg98IxwGgDUex4R5+i/\we/\ZSk8W1k8YDfZ6EGYDnAPS5lX0DOYmQbl0O53e2sP5+MdGr+W4qhmiXaBNobzHYyUa71Xl+56DdFzFyf0sbk4rq9Z6vmMruOElwVB4ZaMQ1yZX0JC0+x1BZmOpbQJwKD0wYUkoRnaQbLY2BMPvPD+dkDg3/\/\Pc2dxC0Riy0GVOXCrdcx/\111yxBkjcCxh7V8CnFyrVK/\ne9JI6c1vC5wNoz5CI9y9hQj+cUT4e0wfpVLmung1KuvQWz9fxfdZxAMs7r+sdq2KKQlzLSeNFkY8gYEG39ZV6B/\Eqamh3ixqgIXDPKV48wWaMjKOYxQF9lGe3tmPjsznMVjwIIb1EOvgNdZ6gnzN31C+6WlJhJKXJML8KStVN/\TYKZOpU+8coUXHIQQQT0Yw30lvTzfcqz0D4ZlKzVU14WoLDQAr7bx58tIseraU+32VH8PSHM3Z4LSXB7lt/\RL7LErIRWakd4IxoPPpdTqjpD0L9pNMVwb5kLMWSSyOg/\l927U2fPecXMYHpUEc1OQ7IVhMV9ExV67hpMZg4CqMT7E7E5oujXrV3o07YQ9PH2tyOCD0jxL23ZBIFforC52zbYbWg1VFmjfGE1SlrnHLUaKvCOZpbn0v+K0nu6gPeSmHX84tA33gXOxfmohgAcMUCukZ0Mw2Z7QPCk/\wWhylGfhQmazuGVMnxjTGUefoafWH6OaE2iIY852wo166tdkvVd/\nYbE9plHEcbCkS/\Yguv3UyDVmJX7Wl/\iqi4KQ514YF8xwlFa+rFXA+42XuYSe5rOG2YGi7NTFoTpf75hq2qyjn6CrvAH+tfMvkVmCtF7hZ2ITkoSE6JKj/\fcXvmTyqwPGEX6NESk0mCDDrv+fEOiWk04dE+B7vKuWCxqz/\4yBqkRJZvUu0AlXV9jOcO0vzfs56HAb2z++o9BrsVlDSjRXn1IUk9OJltn/\gO9ka04DD0bgybb9oanXahQ6ndVu7xSe/\SN38+ar6CotU7zlHKLpFm/\fTT06UgiL9eIYfouvaGswGlOSsjnHLedDQ0pEi+vtiRtE23EsK2qQL1+p6KWr+QkVwUYiHV9GKBAI/\AfQICm1L2RZWynnz0G81i7fmLFgTagYJ4KqKlNSEglQL0r1fLWWYMfZ8LzARJBfK8OSH0EwMAvE4K2h877tvOtC6r9S8F1yi2s9j+70tcJ7qIRbxqlzjGywxo94qyDM2YNaPfhjxEbcjzLDI2vBVLHO3GYNdG63buRNG8yu4AA8SKi+TSMLOcUR5CzAcc5Go7fK6E/\g0pdcMtQAksbMSUGbpoxNTsMyqqazlwG8cqSZu6pKBksZrjWxrSc61h43P+EADh+5mNM28R3XDlkrAHP9SuFsPM+JIlQt6MhZMPRnkYFsbmwmbqM2Z2s0Y/\jaKw3ewvsXK6uVNYUH2aBSHTvBJf+MusdTVSZYbci6we8YBXEYlbP5wLyC0OLb28oDdoHHZUZmkdW8v4lkfgog8h/\Sm/\gbOO/\OocwlNv813Itak2G6M4Xk90mGxTn1RXS1dGTPcQIsOjWWZIONUKpLq0fFAK4ZlBSEms7hlYVI5gb6Ed49zYrQ3TMkzATfJJCT3cM5bIIuJOkdKgRV/\40oCLwJuWos+6lpSBTl1sXq88dPiJVBH0o26vDtT+UiEZPdAPmOogzvMKpA5MMXBKHVzMDEA6ra8rX4tcxVncgbVH/\P78nQhvdrDdroHA0g014JMIFVn+tCy1mN1/\YvfwvgLRYTkcrXrr0DbgRxNx2R83e0eC/\gyaMl4it74i1y846Dc2+bMLx3MR0e7B8S/\QEKeRDgwYim41PvVAJbOTfOr2d49IiIYbWqYbG0cqsZd7d6ZRl8FwqjGrty2e+R1Ro60sgfm82ssmE5NNayTVjxGfXjMxZ11uR7F2KKnod4hpsvt1/\CDsbz1R0n5sgbsxjesJHiakJHcM55+rL6DW92UZu4+7RWpkQgvRC3eqF16DrzA6jjPQgmyQmNIVRXUuLgg/\UwunmhpoTT1vv+JvpJQ4k3dQ/\jzyO7r6d5n3myMcftOe9RgtY6qOjIgMomCthg3ySh0oqiF/\z1zna1IvjL4HaNCkslO9ol6k+S8C9HhN919DOx2QOwB7VDcvRlm+/\aGDq6ZStKB7bJ+O54LRmSThWJuNBRsqOtQ/\BIpYS6absg1yyZYXjq7ohd6UtbERe5DxlChJ9/\JKbvqnGjoeOVPc08szNn+QPRkD5dsdkIqUpmZ1XcRys2Xp3PreM7s0P2xKupqshaDRoCP63b5ZRO76rKK6llbuny3jEnbHF67h9TBVHz6XNhBD7aeJu7YzCEb7Hx7xyfC2lIe1YQtsL1UdhAEvztQyByAhqiFt4pr9GTfeI6XndOqzs+Hmz51w+vNNtvUBcr6wWtPUlYLrU7H9k7SmyrwMMIp+BcqXzNKiMJ5ynRznknuV/\xknBGv96eMvFJYYB9+Rl39HzwL1ZAmHhV4VUDRY+T4cSO8wub9jp2vj8JaGgv7XolT1AdyLhYGGWLsaUGol2I2jgmZZAcbduyZhydlYH09UY956RBnw4DZPejr80h5dAo64RPu8zw6HL+MsxWHTf3MKCOprYYjIVA6J93xPmgzBi/\/\N8UZdh1OLJVvdfIu0GPbZE/\YuWsCoLh5eSZmHZJfaUSzCTraE0wP0a7rmvfeNah5snLI6rONoVOE9jDPcfIywbXWVUu7NrZOqHBtMFPNrRg5c8ksYyGrPVIZRLL164IRA+pFoXtKwC3YfKBeVj41jjI/\WsPFUCerPXLsJOkYzJU5hehCXW9m9C/\FXXIxMV4gRhNdM0h7ACKMyFfs9eaLa2f+grFXgeMsrOyGNSOYv5cdumlISYp6A4m+J1ryYTTxvEGa5lvWW1jSCPao+jj9zZtN23JCbrhkStdvLZYIYZKj4bKylX2m1Spg+Jy+60Tz2YRc+n+dtx9q5/\GFtog4QbRatvFfvV9Pb0cOORmsE3meIr3aV2VufufnOACmwxPDon5G+RjPy+OzBJT3HfRYU5UbsVTg0OHYAhEh1xlA0dq5GANN0hp+bb1YMXGZOwV6qReM8pade2ePwQbXd9eziUnKpcXtGDOhX+hQh38AfCD7veN9WTLz22dYZxhWTKnaizyRFu2sY40jYqEhiBvJiJr3fLoeaXfTGQkJ1Se0+3OFdB7ORNRb3IdxG8a9ejfKOGqJIsmw6kzTo3jVR1dmORxmsA9IYPhIMEIUCSqvKnyNr6jqHwDAhd+3wNwS5tOVOcy29jwpfdFUab/\ByhfuDNLe5frwxYqmiJ12Ie12k8TnjFiCLA/\W+fbxBGyK3UDmIuh5GhawdahNqqvao8SFSv504HPepIQZDqvlkGULSn1X44NV5EoBa7m91zVG1V48W9+pYWdIa4d8iFvm1UBjVX0VQDrfxJ4YtuO71vnumqSYCG+TbVw+AS80DiU5yeaicYIkKLJ+/\x30/\S0T5RivuFE8JC+HJ1XgHFRu8yQp601EEqIb+sJ59tT1KnZgcvvVII/\wmcTHV0/\fHq1066BmSd76vSBTmOAjcRDIuTn4VtCxmS+ih6dNhCQkg0JlXVagitx5gkBv0pQv8dSK/\wrr23yzw3tY9KDH37yZjzxbaonFdH1iLMFUExIsDfx/\eExSUPwjeuaEmwsmulM/\lqYJBp5jAczdIvLqoVlXpOLfnlstqTyYoDqdF0lY4OX4wxtpT0DFpVo8yf3l4Csx8MY4LoE/\QcbYUNqKTHXzNpZHe1o+gG9DSXhCgCWKqX8ORG81LJIt2noEq3+k4lgOIELFZdcGd4+KbL2NRu6J7nz37looUZ3wJQxh5PAxST25969iuRB8lV8rGeGj6IvjuxZ2fSDspMoYOgydBP8qWmB8OYo5VDQcGkylmThjFJWC3yuKfKE4MeLvMJ8JC9LVChCv4QvrnHFVc5TdRawR29vZwUqrr9rVNh+bOcJmAYYMpt0qOAlaJs1+dvlmvEvHvDFfm+70VohMGQhEwSIJPaj6mdQi/\AIoYvpgvFC1tk33QurXxDUQXAZhgj71N++MSHMwLqNqRF5Kg7dJ8VVn+x1Ej1XzC8ESJnjGQHneQ1y1Vn5obrnET/\is8fGu9LV9ihQTbZpnp7VDDUMQYdfZt62jZj9LSZyWK2O/\hU7CYD978/\xsdp0aHUimreydFQUgirEuDwIw1NnPEdKBCUUdCJ9NuEwh1t/\/\zUAniREI/\pfbr0ISVfCOptj5nECDcGgsQeKy3CehcSoqQ6MlAi9weG4fYmw0KB+SvDjb/\ezN1U1PEf0MT+xp9c60n8YibzwSeGDzSxtkQXy7sVcPVY3ilm+Vi2NpiRHf15rqKlEHYpy+tXFEhCCJwSkkBJlWSu/\YAB2BrqtQSFsc/\1QQVCpNqX4xlpbvl11qSh54qvE15z7T5PaCFjOTWjgq6rwrSjz2mzV8srGylQzLCL8V+Mfru7cq4YnYL9rmChfYHanS/\2tDleFALXBJwBGmKkmfUzFYyXAELb8QijPYyfh5HJ4aACihwYqPfcv5Le0xVZP+lcq05MgOIoHOW6CTodfIdVSsFj5dlqSeOQCwYLBLr6wdSMV6ZDQS30Sn8RtBFzaziFVarRaCRkgRkrqTRHGaGINNMK85nESqRwjZqSfJ2myi78JMHwa4McJMcd9tff6r76NcsLBip59kdgdWQnrx6/\lZKhNo96RQblt48V+eUmrDmLHsXUF3w7VafJx0SLDAR9fDWi0Fio7BnTeSbD4sLN9oV3rc+6gmpqjDtp3PRgr0y3dzbNUFxIE3fZ18lcrUiNXpPyTTMAhBCbAWs5VrDv/\8nC/\IB3Jb3Ce8tMoKhAmzdK6vXp7BmOc2iIxBfTFhbpQMLWBD96pxCXD7AqHx4f5yRxYksKFoOiIBHWId8tW96isE6rBtJz1rTrnuMZLyiOMFEyKVcXI0Y6c7DRA/\YBV2piw1oV2UM5UEQMDSljSWz3Zp/\kEz7oF1K06yo3aRGYYfe55OIaM0VjpIirAswpubny9o9zreZAiR9EX0l6DuV2gP8uf1VqAG/\1Wk/\qMw+dfpHrmPTg/\c7C/\FpkeIl4g/\WrTeBFba4zZ6GCZ6T0gnzwmrgTEmpaIfU1rjXTd6DwXk7JXi1ZnPqqWysTYPuY2qylYl+Lw35PzfM5N0CkZ0RBtIuFyWundo2idqjdVTdAmZJ/\IbhtjoEofA0Xeqdpx2tWQwYtkeRuilDwd8XKukUk+aYPzwpIMgnR07EkDh545qGiqD/\gjk9n+5JGZUTgl840I0ia2MP0Tk3866T4kWV5wOGAhVNfdQc3KQzvpwHSCQ3+EfDD74LLlCXl1BWyEMdDjr93yL5x+cfgcDEfePa+k9zLu0Zu9FH1NC6bG3jWwVNiLRjubH84cwDwOqmG5z+NsGRy5va0pb0xG0+bmnjg3sASqfG3syQSYQ36tSe4tJu9z2weWSG19Mb0PNpLz8fNDY6cLrf7RpsWabQ0wuw9KHCvmiNl70Qua0HUT/\HdH1oq3zgUonePSoZfNd7sCvQJW7DxiOSsB7sr1nFQDPg4nj5dmtzleByQx000XJu2+SxI0CmHfF8GrvXLNxi6IYhmYvuIAtK8PwBhT3ibzJ4qa49hGHZnd7ymHeYGBUNUHQIhmawIXdb/\XLq43Vq+fy9v06JfyBN9zXb4Dl6ev++Xvk6zfsOJq5K6ZG00YBITX+FZzjlMfqMt+6nLCNaWGMFa50DmEbSN5jbLVQAv0l2Ds/\E9Z8GhJx+8XRfSTtYtgXSoVbRq5zCz28lKjHLe/\cSQs3X4WOexAQSxqs8XhQPE6Dy6ZgZBEmizUQ6nr2u8hTOzFasQYKlR9hjefRIY/\QV+1Zo4lhuGxf4Gr2k/\mixiVCchZltnHWpyvPCQYrLPBvXzFj861L/\u1IRAY8hTtjLl99fUdSbiZh6Yl8FS/\FrWv8m3C7xFh8sZlH2hAiH9cDf3e1mibEFyjRGF4KYckI0qrM8mKk7I1PALGbibZTHbxqjtaO1tIiQdfTS6iesgFepvYKzAp8XrSUS/\pboDT2BrHQ6JkL9YbjZDA1TIU4hLnctg9mCj05NJfWRik9wg4cQwFKJjxUfy7LwVTwTnoO42ju9nNaz+6Sr5WYVcur/\mSKKS7y9aLHdoUZidutZYbTIflBZi0QGrxjmMBdall0q/\4FO3f+kW6I986H9iffUX5HX8NVY6pGaBIJmhb9rEFk0ak6GAzHsdhJwYrlmivuP+kYDwvL+tbCzoZrSXSGKoLx/\ZNxLpBcIM8jQxWCPr5OWT+2W5iTGEypfcjYgRqJIB4VFxqezWw8uCz5UT6PAkX3EnA7AyJ9aGBIXqd13R6f8NyGZHBN8PVS0bQMmeC3ad8XuxwqNY6PimH81bedydxj5v+muVkzG9u9M38Kg1mS+AYl22l0hJdQe8wjFTvsFXEgX0J98owF27aIFwp8YvW5iBG03p16HAdD9KeUmbQZpL+UhczD/\Up7akHhcgO+90bazPFwk2+sNLMBzdKGsN8qYyizDiWpciskTdKhEzjBH449vaA8Cgsw46nZCkg3UF/\NojA8HgWTTNXKKDn6QUX0MhOJ2Fl8dPQVpV0qiI9pe5nG4rvZ5r/\VcyweuS8qVdpV7lky+tnES8CTX0snsrcg3qCUwmYn2tzoN+2TWzu9WTtEcwrO/\B1hgXC80FS9rgo3iXkcA2pI/\cB/\wTOYyQ7MIQLnz2bYGCfObXTwYIi28vbQickL6uLJ9bQk1GLvaiYF7PZOhyJ9BF4ro4si0zHR5Jr8Y/\atgYFr6k9eZUutkq/\FvnGeTdNzdCzoPooEXIfqAF6axLiL8riSG+LnHYKGbXBVejS51CUJr1wC6U+fLPgYNuN2C9Rip81z0LN2lALSVLzfc7C1p++FWX/\qy1wGdwYGYzKtZodIbQ+7miYL1IV3R2/\9PxaBmH3bLWrLTGpcwswBmUZQcTlVRbJyF2IBS9SReEJbv9+6iqkJ7b8rQXMaYypZhxykOdzkwAAffqSxaN2flQbYyWARQDsY8O9BAe8QvqIEy0HgtR+3qVEbDzgpW23cB1UALegxvfioIbtFULkQT7bV1L5w1q1Fuy0GWvTbNEGpJd3dtQcKIFGkiUwDzUaHKi5I1kMIdQCys3FyG45EYL2/\jxHguGPnNWL32BBnTiYJNHnNtFZL3p2s5tmJOMgoINwIOVh/\iCC0wWTzdWfHL8BW1OZAPAb8HRNhE0jJ9Q+eoE/\PFZaD2mXxscte2XkWewKfrymf2IS14rRrE6Zf6DXBQk7ac/\MKLv3Cx4Ot8wfPIXLHIBdhy5TtKHzraKNNpCR+0lijs6MI/\NhKWdLEuw6vaw89a1moQ2+bCYbABKKyFW1aVl/\ZK4z8SeO5itfCiTpZlgQRk8EOSCWcPnUpJsVyrihGdlMUjH/\EAvpT0lV9++/\rxk5iT53rXLafeDVawVIy/\Dk8bnSibEYSACtSfJUxJhVwTn0Ta61AhBZf2tPZIa6n71b5+U14Sz145VsfluCMxeIZ6ek9KrE3B1bJRnXExiVmcSrnKP99upyZwLZfIz4fd0xem9blVp9BwnFTxN1qIh+psYa0U/\m9aZnqq4P4NSXgBt8h9sD38EpNMpXEk/\T3s9eGM043jdPiR56OZEb+BddRemeh2WNt8EQjjfI2jp3pODWx3s90Rl8nlSQ+bVjV9XZsr3oawJ+K2WsEHSLJg72mByjIMNh6GD6zlBFEB4jKvdIcYhAawtui9pEeZmXRnXR/\OCd+/\ePYGAY70rsTprD10jdMDOWabVjmALEmI0r1WHHfZf8IP+ixxeSlEFV663ODY+332V/\g6iUAYWGlhcvPGA18fXRJHHAy+gHesJOq8tnEizWZEoVS7G9pT5KVpsUQTT48kdvh70RvckDwqtlD0LHRAGZ4hWIQ7xIjamEodtC1SlNepXkqSq8Ayog/\Wgx05PKu3pAS2gFarH7cjN3yQKZBN/\BoFWgKkaJqVsdJh8ZdO8zgvEdO2bV8XEdnDp1/\zoGZ+HnJIqs0pX+xhbFvAE/\xpfd19X6cnlQynZ2JX98GwBfPyify4bsLTJo44LQePZzcjHQ0HYof0Tl2KYG8J7qDkql80W3uPDQ0TtNgLJq3HmgpV+T4toG+IPISsJ9APuNVgaPcj9kgZJbZ8pcpFy3o+6Qm28ce6LCxSwqh1nL7o1LfD4NLv5k/\Nv8zceL88eUpfI29bEk9HeXW98XsRW9UbM4iLehLMe9xI5WwcysnIdVPk1/\P+YXgeZATE0n/\w+YTmspqmelGoRuHvWJ2gqmqhtctPi2/\6vAQCSbc95wvRLJvLofUxhsK6q6EHhBEGOSzjnoBLb1NLNtDGSVO7EGHvBwmwkiM9ebhrC4hZnB6TspaUtUs11vgoy83kp7tpLiYjnwI9s9P0NEnA4MpY8NHXFqH6MUCLvSIm93GlP3UFdD+xUC25g2YYY7j6tMyuA3Qd6byts1f85UDFF57Bpbkm6Fv9NNuI7sl18LOoK3SNa1uT+ZewVHjgLX8OODtcubKqNeOBIbJJgrTrVXqS2kBt2e4usqX+A3H73ru3oyz9/\FvT+IGqC5ZJSwd5Z1kmk0XnSG4ZvxmPWVg2vvpac+ZwJDJkdCz93d4mvyuKpQoDlhIszK69RzQrTUnhwkzs2iR644ApvowmbWMjRH+OB/\JZoped7WRNBwQQ9B2pF/\IvmIlf19dFskiwOm4NhwWuAWZZN9N8Al+zf+LaOkxbe90yh3Ily1AmGEfvz7udPeAGm7iJsRy1f6sZAnrRNrlSAnsR5Tw6FZBYlHNZcjv0Tu7xzsecjbF4khOD7iuKSypKxMGEgZhKBoDdEvJ80K2OuhVo9IHS/\sxA8j+lY7JzqGzwXZk1rtcUQlKrqbqkIRKKpv9VkSlbMAJPX+3jGuWyNg/\ajZCN+sk4BcbwC2JFKTjJCN0cbt+HEmKCABiEyBab5Yyvx/\k2aYt0YLyalmOkaUkace003wq3Rw9q9V5kGtW8QT0oVgkPv0jT4s1daFXZpYPe8TFxIf4OVrzoKIc4hTmQCbmJbD6YJDcsoRNL/\DrHxqIE45PWM6/\zmtmH1Z70WVzERBuZYx4hBuw7dXedaX5C/\0D38QoxWIyiUMried7HMlunt4D1FkD8PHOuwheuKTpMnzPzXR2TRMt4jnGBjgtjrKGhUJxqoO67x1qHco31NAd7K/\sKVa+PUVk4P9ybwTn1Gd0pDe44/\fgbLJliJPaxVAbsEqw5NcopYkKpWSwAhAxmtNRwkFc9DtI0ieipO1aMDfLWpy7sgtKJWlyZgbtXd6NPZR3isB+zxWmWArvrRPXWONHK6KxJMEyLvT/\4L9yPmKEc+Kc45MAIpmV53qr41+sR3137sbB8T4YxPCNl1Yyt9KuFoG0rx1DyIlGGjW3ik8ow+SSAfKM08SofgXonPLNTaTbQOluQ8E9N3QQsByotZ9ayDzkH339WdGt8oDNGqx0opju8AdH+xjRwHUy+4rXKQDCAl/\M9ILccJgybFZY6IDiuCELOGM3kK+J+5O5gAxOLYIwEVSnhnKcbpv0V+p9AnBGJenCfrnFL/\taFJUz2T1LO3O9Iwkl8sE7eGA36r7/\9sjpSPUCWg1VBijWRm8rZCMaKUniESI8rkaDkfUhKOO1BH1pwfcHoeynt1qJLSmmde6bNazA9VTPgL32xLpu2pnDRLABhwfZem2c3wuf79E80WZfqmIGGeD6T8Mjx/\PBrVtGwsiNQpVgJ9lJSCgXmYAf6++aTmVf2jt3eBrqTNZZqbwlfZng/\Qdn51hKM6IIDFDkZrTvGjhn1ZeogDwifLd/\eijQnfphMbOgAMOrKFsBvQmEerE3pQJE/\rGDTHRGfSRs6MlX1FZA2HTO4Cf6EFqkdiLiNFC45Hgoy9jy9pbSoM5Mr3gaS/\3TrkrS6mN9i2pP4SBQTrQs5Ee/\0E0wMbYa4d5qNXTpgpPrOTtJh1RJ8k2wyBrvMdtZ0NXuwHaGVui/\HWnUKV5vRJVeGYi3U9lhU3LV1qZE4fym8LFti3oOCla5RrB5YczYpv+V5RlWRpuf+gy0zcQop2yCvbnSnGTBUyzDwEUWyz4fmuy0dk+Rx8fr305ovE+xCxWb+YhxsFl9ehPXoEhR9KnF7Bf50Q76Y51AlSFGc6Exi8Th/\5pdAacOpMS3C9reMLSvEn7aYhNTa79U2xcXj1N7Rt+Wuxfo2kdsg3QvdOHQg4XD5Gtmse1ELkpQgtlFEahmSV9pb5ty938hMifKZ1WlstNgyTYO6fVVs0YE2WhjvUUxDDyqpKKZ9DE67rLji775FfAm5fxiTm0/\NFi4uLn3PwU7Co2Veje6FpkR3bDvW3hCE0NH74DRWZR3uPDuzx7pOawPSoewZytgJ6DyMwaSGQsSa9AU6dUW3UEfBn/\5qbqV4+RJMFK5tZ/\lhaX1S0OhgUVHKaEy1PNzJiOr7iToxUTh7+CBUyfNGdTe20RNHOJPtCuUWoC83lrPJG4aiEMN6j9ywe1Svbr+/\0091090928509109tc09109', r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')
    
    args = findall(
        """nnndje\('(.*)='\+encodeURIComponent\(\$\("input\[name='captcha']"\)\.val\(\)\)\+'(.*)'\+encodeURIC""",
        dec
    )
    
    payload = args[0] + captcha_answer + args[1] + ''
    
    
