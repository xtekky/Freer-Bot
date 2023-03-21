const { CryptoJS, CryptoJSAesJson } = require("./crypto.js");
const { getDevice } = require("./device.v2.js");

const navigator = {
    userAgent: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36`,
};

const localStorage = {
    i: CryptoJS.MD5(navigator.userAgent).toString().substr(5, 10),
    h: JSON.stringify({ v: "101" }),
};

const format_s = (e) => {
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

const decrypt_resp = (response) => {
    json_resp   = JSON.parse(response);
    json_resp.s = format_s(json_resp.s);

    decoded = CryptoJS.AES.decrypt(JSON.stringify(json_resp), localStorage.i, {
        format: CryptoJSAesJson}).toString(CryptoJS.enc.Utf8)

    return atob(JSON.parse(decoded)[0])
}

const get_token = (payload) => {
    if (payload === void 0) return `ZA`

    return btoa(String.fromCharCode(CryptoJS.MD5(JSON.stringify(payload)).toString()
        .match(/\d+/g)
        .join('')
        .split('')
        .reduce((x, e) => parseInt(x) + parseInt(e), 0).toString()), 1)
        .replace(/=+$/, '')
}

console.log(get_token());