const { CryptoJS, CryptoJSAesJson } = require("./crypto.js");

const navigator = {
    userAgent: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36`,
};

const localStorage = {
    i: CryptoJS.MD5(navigator.userAgent).toString().substr(5, 10),
    h: JSON.stringify({ v: "101" }),
};

function obb1(e) {
    let t = parseInt(e.substr(-7, 1) + e.substr(6, 1));
    e = e.substr(0, 6) + e.substr(7, e.length - 14) + e.substr(e.length - 6);

    var o = new RegExp("(.{" + e.length / t + "})", "g");
    let a = e.replace(o, "$1|").split("|");

    for (a.pop(); a[0].split("").length > 1;)
        for (let x = 0; x < a.length; x++)
            (a[x] = a[x].split("").reverse().join("")),
                (a[x] = atob(a[x])),
                (a[x] = a[x].replace("=", ""));

    return a.join("");
}

function decrypt_resp(response) {
    json_resp = JSON.parse(response);
    json_resp.s = obb1(json_resp.s);

    console.log(json_resp);

    return atob(
        JSON.parse(
            CryptoJS.AES.decrypt(JSON.stringify(json_resp), localStorage.i, {
                format: CryptoJSAesJson,
            }).toString(CryptoJS.enc.Utf8)
        )[0]
    );
}

response = `{
    "ct":"Af+Qi3zB6LC63SvrSgMGlTFmbT1F7kXahSLzeKCrdl0pZFevzQ0fdWHzswcmMfCETywriGYgyWhj2fVEJqC5Tx7fGwXrwjbI0HhyUS3fXCFW9XnfjX4b6sj9K7yanycxPtxN2lUGIjW21ZRUcOgK4ueKkY3\/w\/cXijYzSqCr3qX4AFmfYxmXhpOss5xSbFCUBbTXghK7RA3iOfdkZzphma5HjznowtOPqDdt3KdKLvkLKDZnoKH96MlTBuft6IVVrrcqdalZqnUf5O0GgpgUJ0VPvaGVzZod4EyuIDPF9Zk2g3ii77q9dpAhT0ih67pnZB7owYEBy6s4SXdVK3RZHVfyoTMJoquKRRev\/iMfp34D1HA8z3d9sY4QnPVA44TmOtPRTRr6EnzyE6qgwBnyXl+46nZ2Ejl0Gcg62GfV\/v3nikQjP43uuUtZVSVmxYvk8jsAe3kxiWe\/METuXNRaUOS0DmmFN\/v8xdRzbBKGC4RhFOODTj5taNIOETixEbDWcMCMJfW8rde5xA5a1oy1VEcTCujhn27p4btZ\/lBGHh3BZrur7h1aumbytcDSyUWxeSWcvLI7BevCzrO2JKEMOeGoeWHyKrDF\/sReFVfekVACDc6pZeqivpiJT85zdXFNaScr7x\/lY\/vuEClvzu8kzD3ZJuI+jlMtfp9n7g3pP1ejA5tK2xaY+a\/OiUy\/AT7g+2ULvRrMV9xGrXtodrsuItfG1hQjOz84qAvYPdSoy8w+clUZxx6TbYfcBmllgN9yhFRzF4Ka96NzMRltoI3E+sH\/zfgFphcc3O3k1m3i57Hx6MrI8Udj0G9VA4PWHINdP2Vdi7I8ldCsO\/PYfeAf8QaPJvB3QWofBO3KXgg8DszKhKbJDdN2qNNz7tTRUZfsE1YRGo8fZn9v5ZGf9nKkUkw5H3IG3jc2+obILzMcBTvAD77HO5me3tzl9vRupaCXYICCuE2S2kns7KYaivBFg2K+cxNhFAQmwH8msEDv27mnk\/MIQUID5V6GajqYIs5Q6vlACRQi+fXwg8Wp7sukp2k\/7xPHgudyM6o7nazP\/Y1N0IEFtoXKvCSMJqnPCxccuaB14yT02QFWQtIbBLqDB2QLd97kvX+B4cVmxZkkzvP7NGpVZwKXtY2XxNDUbtLj17RbUIO7iOIyqzqyEUgnObKsYbqnoFxVSXcZtN7QX4Rj0loDQwUF01i\/CplTrEu42LL5RAgco\/+Sm5Le4ShP0FM2UBcMkOFGPDDO8JhyhHP0ydZ\/Sn2e\/oAdes9e8uSqu4gxw\/eq7+XWEfHdgzBaEQ==",
    "s" :"k1Zk1Z6oVU40Zk1Z0UQ8UQoVUo1Z00d00d40Zk1Zo1Z100Zk1Z"
}`;

console.log(decrypt_resp(response));
