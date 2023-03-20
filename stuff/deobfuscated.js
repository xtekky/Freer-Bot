const {CryptoJS, CryptoJSAesJson} = require('../crypto.js');

const navigator = {
    userAgent: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36`
}

const localStorage = {
    i: CryptoJS.MD5(navigator.userAgent).toString().substr(5, 10),
    h: JSON.stringify({ v: '101' })
}


function zxndnnndje(e) {
    hsipdxdcej();
    $('#loading').show();
    $.ajax({
        type: 'POST',
        url: location.origin + '/v4.php?s=' + btoa(String.fromCharCode(CryptoJS.MD5(JSON.stringify(e)).toString().match(/\d+/g).join('').split('').reduce((x, e) => parseInt(x) + parseInt(e), 0).toString()), 1).replace(/=+$/, ''),
        data: e,
        headers: JSON.parse(localStorage.h),
        success: function (x) {
            hsipdxdcej();
            try {
                var o = JSON.parse(x);
                o.s = obb1(o.s);
                var a = atob(JSON.parse(CryptoJS.AES.decrypt(JSON.stringify(o), localStorage.i, { format: CryptoJSAesJson }).toString(CryptoJS.enc.Utf8))[0]);
                new Function(a)();

            } catch (x) {
                if ('Malformed UTF-8 data' == x.message) {
                    client_log(c = {
                        type: 'browser_update',
                        js_user_agent: navigator.userAgent,
                        screen_width: window.screen.width,
                        screen_height: window.screen.height
                    });
                    askkkdsanxc('<hr><h2 class="text-danger font-weight-bold">Please update your browser or try a different one.</h2><hr>');
                } else {
                    var c = {
                        error: x.stack,
                        post: e,
                        res_dec: a
                    };
                    askkkdsanxc('<hr><h3>Error<br>Please try again later</h3><br><small class="text-muted">' + x.stack + '</small><h' + 'r>');
                    client_log(c);
                }
            }
        },
        error: function (x, e) {
            var a = JSON.stringify({
                0: x.status,
                1: x.statusText,
                2: x.responseText
            });
            if (0 !== x.status) {
                client_log([
                    'request_error',
                    a
                ]);
            }
            hsipdxdcej();
            askkkdsanxc('<hr><h3>There was a problem, please try again.</h3>' + x.status + '|' + x.statusText + '<hr>');
        }
    });
}

function check_for_clocks() {
    $('[data-clock]').each((z, t) => {
        var T = $(t).data('clock');
        if (void 0 !== window.bclocks[T]) {
            console.log('already_running');
            clearInterval(window.bclocks[T]);
            delete window.bclocks[T];
        }
        window.bclocks[T] = setInterval((c, D, n, V) => {
            try {
                if (!$('[data-clock="' + c + '"]').length) {
                    throw new Error('element_not_found');
                }
                var R = n - Math.floor(Date.now() / 1000) + D;
                var K = sectoparts(R);
                if (K.forEach((x, e) => {
                        var t = {
                            0: 'year',
                            1: 'day',
                            2: 'hour',
                            3: 'min',
                            4: 'sec'
                        };
                        if ($('#' + t[e], V).length > 0) {
                            x = x.toString().padStart(2, '0');
                            $('#' + t[e], V).html(x);
                        }
                    }), K[0] <= 0 && K[1] <= 0 && K[2] <= 0 && K[3] <= 0 && K[4] <= 0) {
                    throw void 0 !== $(V).data('callback') && eval(atob($(V).data('callback'))), new Error('time_up');
                }
            } catch (x) {
                console.log('destroy', x);
                clearInterval(window.bclocks[c]);
                delete window.bclocks[c];
            }
        }, 10, T, $(t).data('time'), Math.floor(Date.now() / 1000), t);
    });
}


function obb1(e) {
    let t = parseInt(e.substr(-7, 1) + e.substr(6, 1));
    e = e.substr(0, 6) + e.substr(7, e.length - 14) + e.substr(e.length - 6);
    
    var o = new RegExp('(.{' + e.length / t + '})', 'g');
    let a = e.replace(o, '$1|').split('|');
    
    for (a.pop(); a[0].split('').length > 1;)
        for (let x = 0; x < a.length; x++)
            a[x] = a[x].split('').reverse().join(''), a[x] = atob(a[x]), a[x] = a[x].replace('=', '');
    
    return a.join('');
}

function hsipdxdcej() {
    $('#loading').hide();
    $('#msg').hide();
}

function askkkdsanxc(e) {
    document.getElementById('msg').innerHTML = e;
    $('#msg').show();
}


x = `{"ct":"Af+Qi3zB6LC63SvrSgMGlTFmbT1F7kXahSLzeKCrdl0pZFevzQ0fdWHzswcmMfCETywriGYgyWhj2fVEJqC5Tx7fGwXrwjbI0HhyUS3fXCFW9XnfjX4b6sj9K7yanycxPtxN2lUGIjW21ZRUcOgK4ueKkY3\/w\/cXijYzSqCr3qX4AFmfYxmXhpOss5xSbFCUBbTXghK7RA3iOfdkZzphma5HjznowtOPqDdt3KdKLvkLKDZnoKH96MlTBuft6IVVrrcqdalZqnUf5O0GgpgUJ0VPvaGVzZod4EyuIDPF9Zk2g3ii77q9dpAhT0ih67pnZB7owYEBy6s4SXdVK3RZHVfyoTMJoquKRRev\/iMfp34D1HA8z3d9sY4QnPVA44TmOtPRTRr6EnzyE6qgwBnyXl+46nZ2Ejl0Gcg62GfV\/v3nikQjP43uuUtZVSVmxYvk8jsAe3kxiWe\/METuXNRaUOS0DmmFN\/v8xdRzbBKGC4RhFOODTj5taNIOETixEbDWcMCMJfW8rde5xA5a1oy1VEcTCujhn27p4btZ\/lBGHh3BZrur7h1aumbytcDSyUWxeSWcvLI7BevCzrO2JKEMOeGoeWHyKrDF\/sReFVfekVACDc6pZeqivpiJT85zdXFNaScr7x\/lY\/vuEClvzu8kzD3ZJuI+jlMtfp9n7g3pP1ejA5tK2xaY+a\/OiUy\/AT7g+2ULvRrMV9xGrXtodrsuItfG1hQjOz84qAvYPdSoy8w+clUZxx6TbYfcBmllgN9yhFRzF4Ka96NzMRltoI3E+sH\/zfgFphcc3O3k1m3i57Hx6MrI8Udj0G9VA4PWHINdP2Vdi7I8ldCsO\/PYfeAf8QaPJvB3QWofBO3KXgg8DszKhKbJDdN2qNNz7tTRUZfsE1YRGo8fZn9v5ZGf9nKkUkw5H3IG3jc2+obILzMcBTvAD77HO5me3tzl9vRupaCXYICCuE2S2kns7KYaivBFg2K+cxNhFAQmwH8msEDv27mnk\/MIQUID5V6GajqYIs5Q6vlACRQi+fXwg8Wp7sukp2k\/7xPHgudyM6o7nazP\/Y1N0IEFtoXKvCSMJqnPCxccuaB14yT02QFWQtIbBLqDB2QLd97kvX+B4cVmxZkkzvP7NGpVZwKXtY2XxNDUbtLj17RbUIO7iOIyqzqyEUgnObKsYbqnoFxVSXcZtN7QX4Rj0loDQwUF01i\/CplTrEu42LL5RAgco\/+Sm5Le4ShP0FM2UBcMkOFGPDDO8JhyhHP0ydZ\/Sn2e\/oAdes9e8uSqu4gxw\/eq7+XWEfHdgzBaEQ==","s":"k1Zk1Z6oVU40Zk1Z0UQ8UQoVUo1Z00d00d40Zk1Zo1Z100Zk1Z"}`
var o = JSON.parse(x);
o.s = obb1(o.s);
var a = atob(JSON.parse(CryptoJS.AES.decrypt(JSON.stringify(o), localStorage.i, { format: CryptoJSAesJson}).toString(CryptoJS.enc.Utf8))[0]);

console.log(a)

