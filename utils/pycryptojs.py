import requests, hashlib, json, base64, random, string, time, urllib.parse
from Crypto.Cipher import AES


class CryptoJS:

    def decrypt(self, data: str, key: str):
        data = json.loads(data)
        dk = key.encode() + bytes.fromhex(data["s"])

        md5 = [hashlib.md5(dk).digest()]
        result = md5[0]
        for i in range(1, 3 + 1):
            md5.insert(i, hashlib.md5((md5[i - 1] + dk)).digest())
            result += md5[i]

        aes = AES.new(result[:32], AES.MODE_CBC, bytes.fromhex(data["iv"]))
        data = aes.decrypt(base64.b64decode(data["ct"]))
        return data

    def encrypt(self, data: str, key: str):
        data = data + chr(16 - len(data) % 16) * (16 - len(data) % 16)
        salt = b"".join(
            random.choice(string.ascii_lowercase).encode() for x in range(8)
        )
        salted, dx = b"", b""

        while len(salted) < 48:
            dx = hashlib.md5(dx + key.encode() + salt).digest()
            salted += dx

        key = salted[:32]
        iv = salted[32 : 32 + 16]
        aes = AES.new(key, AES.MODE_CBC, iv)

        encrypted_data = {
            "ct": base64.b64encode(aes.encrypt(data.encode())).decode("utf-8"),
            "iv": iv.hex(),
            "s": salt.hex(),
        }
        return json.dumps(encrypted_data, separators=(",", ":"))

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
        return hashlib.md5(key.encode()).hexdigest()[5:15]

    def format(self, data: bytes):
        return base64.b64decode(data.decode().split('"')[1].encode())

    def parse(self, data: str, captcha: str):
        parsed1 = str(data).split(r"zxndnnndje(\'")[1].split(r"\'+")[0]
        parsed2 = str(data).split(r"zxndnnndje(\'")[1].split("\\'+")[1].split("\\'")[3]
        parsed = parsed1 + captcha + parsed2

        return parsed

    def get_fake_data(self):
        data = str(
            {
                "tz": "Europe/Paris",
                "tzo": 7200,
                "battery": {
                    "charging": 1,
                    "level": 100,
                    "chargingTime": 0,
                    "dischargingTime": None,
                },
                "sclinks": [
                    "https://cdn.jsdelivr.net/npm/chart.js@2.8.0/dist/Chart.min.js"
                ],
                "voice": [],
                "elements": {"div": 37, "ins": 13, "script": 20},
                "navi": {
                    "touch": 0,
                    "hstr": 2,
                    "wdr": 0,
                    "dv": 1,
                    "pl": "Win32",
                    "hw": 8,
                    "dm": 8,
                    "gpu": {
                        "3379": 16384,
                        "3386": {"0": 32767, "1": 32767},
                        "3410": 8,
                        "3411": 8,
                        "3412": 8,
                        "3413": 8,
                        "3414": 24,
                        "3415": 0,
                        "7936": "WebKit",
                        "7937": "WebKit WebGL",
                        "7938": "WebGL 1.0 (OpenGL ES 2.0 Chromium)",
                        "33901": {"0": 1, "1": 1024},
                        "33902": {"0": 1, "1": 1},
                        "34024": 16384,
                        "34047": None,
                        "34076": 16384,
                        "34921": 16,
                        "34930": 16,
                        "35660": 16,
                        "35661": 32,
                        "35724": "WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)",
                        "36347": 4096,
                        "36348": 30,
                        "36349": 1024,
                        "render": "ANGLE (Intel, Intel(R) UHD Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)",
                        "vendor": "Google Inc. (Intel)",
                        "id": "8e28b76ed40378221a96deb9bad65033",
                    },
                    "ps": "20030107",
                    "on": {"0": 0, "1": 1},
                    "storage": [68, 306871460658],
                    "notif": "default",
                },
                "host": "freer.in",
                "con": {"ip": "3fe89f2a-86ec-446b-87e0-fd58e9837ec0.local"},
                "rf": "",
                "ad": {"0": {"loaded": 1}, "1": {"ca-pub-5408239243580168": 1}},
                "lg": {
                    "0": "en",
                    "1": ["en", "fr-FR", "es-ES", "es", "fr", "en-US", "am", "de"],
                },
                "sc": {"height": 864, "width": 1536, "orien": "landscape-primary"},
                "ct": str(int(time.time())),
            }
        )
        key = "2!fak<=-!"

        return urllib.parse.quote(str(self.encrypt(data, key)))
