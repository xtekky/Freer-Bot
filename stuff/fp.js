// fingerprint ??

askkkdsanxc(
    '<hr><div class="row"><div class="col-12 text-center"><h2><small>Type the following security word in the box.</small></h2></div></div><div class="card border-info mb-3" style="width: 18rem;"><img src="/captcha.php?_CAPTCHA&amp;t=0.99982400+1679328662" class="img-thumbnail card-img-top" alt="CAPTCHA code"><div class="card-body p-1"><form id="cat"><input class="form-control form-control-lg text-center rounded-0" type="text" maxlength="20" name="captcha" placeholder="Enter the word" pattern="[a-zA-Z-]+" autocomplete="off" required><div class="modal-footer p-0"><button type="submit" class="btn btn-dark btn-lg btn-block rounded-0 mt-1"><i class="fa-regular fa-square-check fa-2x"></i></button></div></form></div></div><hr>'
);

$("input[name='captcha']").focus();

function ookjjj_a(a, s = {}) {
    for (v in a) {
        if (
            typeof a[v] === "string" ||
            typeof a[v] === "number" ||
            typeof a[v] === "boolean"
        ) {
            s[v] = a[v];
        } else if (typeof a[v] === "function") {
            s[v] = a[v].toString();
        } else if (typeof a[v] === "object") {
            s[v] = ookjjj_a(a[v]);
        }
    }
    return s;
}
try {
    window.RTCPeerConnection =
        window.RTCPeerConnection ||
        window.mozRTCPeerConnection ||
        window.webkitRTCPeerConnection;
    var pc = new RTCPeerConnection({ iceServers: [] }),
        noop = function () { };
    pc.createDataChannel("");
    pc.createOffer(pc.setLocalDescription.bind(pc), noop);
    pc.onicecandidate = function (ice) {
        if (ice && ice.candidate && ice.candidate.candidate) {
            try {
                window.localip =
                    /([0-9]{1,3}(\.[0-9]{1,3}){3}|[a-f0-9]{1,4}(:[a-f0-9]{1,4}){7})/.exec(
                        ice.candidate.candidate
                    )[1];
                pc.onicecandidate = noop;
            } catch (e) {
                window.localip = ice.candidate.address;
            }
        }
    };
} catch (e) { }

try {
    navigator.getBattery().then((a) => {
        window.battery = {
            isc: a.charging,
            lvl: a.level * 100,
            ct: a.chargingTime,
            dct: a.dischargingTime,
        };
    });
} catch (e) {
    if (e.message.indexOf("undefined") !== -1) {
        window.battery = undefined;
    } else {
        window.battery = e.message;
    }
}
try {
    const words = Object.keys(window);
    const sil = [
        "window",
        "self",
        "document",
        "name",
        "location",
        "customElements",
        "history",
        "locationbar",
        "menubar",
        "personalbar",
        "scrollbars",
        "statusbar",
        "toolbar",
        "status",
        "closed",
        "frames",
        "length",
        "top",
        "opener",
        "parent",
        "frameElement",
        "navigator",
        "origin",
        "external",
        "screen",
        "innerWidth",
        "innerHeight",
        "scrollX",
        "pageXOffset",
        "scrollY",
        "pageYOffset",
        "visualViewport",
        "screenX",
        "screenY",
        "outerWidth",
        "outerHeight",
        "devicePixelRatio",
        "clientInformation",
        "screenLeft",
        "screenTop",
        "defaultStatus",
        "defaultstatus",
        "styleMedia",
        "onsearch",
        "isSecureContext",
        "performance",
        "onappinstalled",
        "onbeforeinstallprompt",
        "crypto",
        "indexedDB",
        "webkitStorageInfo",
        "sessionStorage",
        "localStorage",
        "onbeforexrselect",
        "onabort",
        "onblur",
        "oncancel",
        "oncanplay",
        "oncanplaythrough",
        "onchange",
        "onclick",
        "onclose",
        "oncontextlost",
        "oncontextmenu",
        "oncontextrestored",
        "oncuechange",
        "ondblclick",
        "ondrag",
        "ondragend",
        "ondragenter",
        "ondragleave",
        "ondragover",
        "ondragstart",
        "ondrop",
        "ondurationchange",
        "onemptied",
        "onended",
        "onerror",
        "onfocus",
        "onformdata",
        "oninput",
        "oninvalid",
        "onkeydown",
        "onkeypress",
        "onkeyup",
        "onload",
        "onloadeddata",
        "onloadedmetadata",
        "onloadstart",
        "onmousedown",
        "onmouseenter",
        "onmouseleave",
        "onmousemove",
        "onmouseout",
        "onmouseover",
        "onmouseup",
        "onmousewheel",
        "onpause",
        "onplay",
        "onplaying",
        "onprogress",
        "onratechange",
        "onreset",
        "onresize",
        "onscroll",
        "onsecuritypolicyviolation",
        "onseeked",
        "onseeking",
        "onselect",
        "onslotchange",
        "onstalled",
        "onsubmit",
        "onsuspend",
        "ontimeupdate",
        "ontoggle",
        "onvolumechange",
        "onwaiting",
        "onwebkitanimationend",
        "onwebkitanimationiteration",
        "onwebkitanimationstart",
        "onwebkittransitionend",
        "onwheel",
        "onauxclick",
        "ongotpointercapture",
        "onlostpointercapture",
        "onpointerdown",
        "onpointermove",
        "onpointerup",
        "onpointercancel",
        "onpointerover",
        "onpointerout",
        "onpointerenter",
        "onpointerleave",
        "onselectstart",
        "onselectionchange",
        "onanimationend",
        "onanimationiteration",
        "onanimationstart",
        "ontransitionrun",
        "ontransitionstart",
        "ontransitionend",
        "ontransitioncancel",
        "onafterprint",
        "onbeforeprint",
        "onbeforeunload",
        "onhashchange",
        "onlanguagechange",
        "onmessage",
        "onmessageerror",
        "onoffline",
        "ononline",
        "onpagehide",
        "onpageshow",
        "onpopstate",
        "onrejectionhandled",
        "onstorage",
        "onunhandledrejection",
        "onunload",
        "alert",
        "atob",
        "blur",
        "btoa",
        "cancelAnimationFrame",
        "cancelIdleCallback",
        "captureEvents",
        "clearInterval",
        "clearTimeout",
        "close",
        "confirm",
        "createImageBitmap",
        "fetch",
        "find",
        "focus",
        "getComputedStyle",
        "getSelection",
        "matchMedia",
        "moveBy",
        "moveTo",
        "open",
        "postMessage",
        "print",
        "prompt",
        "queueMicrotask",
        "releaseEvents",
        "reportError",
        "requestAnimationFrame",
        "requestIdleCallback",
        "resizeBy",
        "resizeTo",
        "scroll",
        "scrollBy",
        "scrollTo",
        "setInterval",
        "setTimeout",
        "stop",
        "structuredClone",
        "webkitCancelAnimationFrame",
        "webkitRequestAnimationFrame",
        "chrome",
        "caches",
        "cookieStore",
        "ondevicemotion",
        "ondeviceorientation",
        "ondeviceorientationabsolute",
        "launchQueue",
        "onbeforematch",
        "getScreenDetails",
        "showDirectoryPicker",
        "showOpenFilePicker",
        "showSaveFilePicker",
        "originAgentCluster",
        "trustedTypes",
        "navigation",
        "speechSynthesis",
        "onpointerrawupdate",
        "crossOriginIsolated",
        "scheduler",
        "openDatabase",
        "webkitRequestFileSystem",
        "webkitResolveLocalFileSystemURL",
        "$",
        "jQuery",
        "Popper",
        "bootstrap",
        "Chart",
        "CryptoJS",
        "CryptoJSAesJson",
        "formtojson",
        "sectoparts",
        "check_for_clocks",
        "bclocks",
        "adsbygoogle",
        "wbpo",
        "firebase",
        "up_noti_tkn",
        "dataLayer",
        "gtag",
        "closest",
        "hsipdxdcej",
        "askkkdsanxc",
        "client_log",
        "zxndnnndje",
        "obb1",
        "token",
        "google_tag_manager",
        "google_tag_data",
        "gaGlobal",
        "onbeforeinput",
        "onorientationchange",
        "orientation",
        "oncontentvisibilityautostatechange",
        "ontouchcancel",
        "ontouchend",
        "ontouchmove",
        "ontouchstart",
        "getDigitalGoodsService",
        "J",
        "mY",
        "mI",
        "I",
        "p",
        "winobjectss",
        "gpu",
        "val12",
        "sclinks",
        "hg21vgjwh",
        "btdect",
        "battery",
        "navi_usage",
        "fonnnts",
        "localip",
        "device",
        "0",
        "1",
        "2",
        "3",
        "google_js_reporting_queue",
        "google_srt",
        "google_logging_queue",
        "tmod",
        "google_ad_modifications",
        "ggeac",
        "google_persistent_state_async",
        "google_measure_js_timing",
        "google_reactive_ads_global_state",
        "_gfp_a_",
        "google_sa_queue",
        "google_process_slots",
        "google_ama_state",
        "google_spfd",
        "google_unique_id",
        "google_sv_map",
        "google_lpabyc",
        "google_rum_task_id_counter",
        "google_user_agent_client_hint",
        "google_sa_impl",
        "googleToken",
        "googleIMState",
        "processGoogleToken",
        "google_global_correlator",
        "google_prev_clients",
        "ampInaboxIframes",
        "ampInaboxPendingMessages",
        "googletag",
        "GoogleGcLKhOms",
        "google_image_requests",
        "push_status",
        "google_llp",
        "credentialless",
        "S",
        "crc32",
        "c_hash",
        "j",
        "l",
        "x",
        "aufzp",
        "_injected_print",
        "_injected_setup_frame",
        "_injected_autofill_controller",
        "_injected_suggestion_controller",
        "_injected_start_main_frame",
        "_injected_navigation",
        "_injected_edge_media_sniffer",
        "_injected_start_all_frames",
        "_injected_message",
        "_injected_fill",
        "_injected_scroll_helper",
        "_injected_form",
        "_injected_share_workaround",
        "_injected_password_controller",
        "webkitConvertPointFromPageToNode",
        "webkitConvertPointFromNodeToPage",
        "webkitCancelRequestAnimationFrame",
        "ongamepaddisconnected",
        "_injected_gcrweb",
        "_gfp_p_",
        "__gCrWeb",
    ];
    window.winobjectss = words.filter((word) => !sil.includes(word));
} catch (e) {
    window.winobjectss = e.message;
}
try {
    const fontCheck = new Set(
        ["Baskerville", "Candara", "BIZ UDGothic", "Joom129381"].sort()
    );
    const fontAvailable = new Set();
    for (const font of fontCheck.values()) {
        if (document.fonts.check("12px '" + font + "'")) {
            fontAvailable.add(font);
        }
    }
    window.fonnnts = [...fontAvailable.values()];
} catch (e) {
    window.fonnnts = e.message;
}
var canvas = document.createElement("canvas");
var webgl =
    canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
try {
    var debugInfo = webgl.getExtension("webgl_debug_renderer_info");
} catch (e) {
    var debugInfo = e;
}
try {
    window.gpu = {
        render: webgl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL),
        vendor: webgl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL),
        p: window.c_hash([
            (webgl.getParameter(33901) || { 1: 0 })[1],
            webgl.getParameter(3413),
            webgl.getParameter(3412),
            webgl.getParameter(3411),
            webgl.getParameter(3410),
            webgl.getParameter(3414),
            webgl.getParameter(35661),
            webgl.getParameter(34076),
            webgl.getParameter(36349),
            webgl.getParameter(34024),
            webgl.getParameter(34930),
            webgl.getParameter(3379),
            webgl.getParameter(36348),
            webgl.getParameter(34921),
            webgl.getParameter(35660),
            webgl.getParameter(36347),
            webgl.getParameter(3415),
        ]),
    };
    var canvas = document.createElement("canvas");
    var ctx = canvas.getContext("2d");
    canvas.height = 150;
    canvas.width = 205;
    ctx.textBaseline = "top";
    ctx.font =
        "\x62\x6f\x6c\x64\x20\x31\x30\x70\x78\x20\x27\x41\x72\x69\x61\x6c\x27";
    ctx.textBaseline = "alphabetic";
    ctx.fillStyle = "#f60";
    ctx.fillRect(0, 0, canvas.width, 0.7);
    ctx.fillStyle = "rgba(0,0,0,0.7)";
    var gpuidparts = window.gpu.render.match(/.{1,37}/g);
    var indexi = 10;
    for (val12 of gpuidparts) {
        ctx.fillText(val12, 1, indexi);
        var indexi = indexi + 13;
    }
    ctx.fillText(
        decodeURIComponent(
            "%3C%F0%9F%8D%8F%F0%9F%8D%8E%F0%9F%8D%90%F0%9F%8D%8A%F0%9F%8D%8B%F0%9F%8D%8C%F0%9F%8D%89%F0%9F%8D%87%F0%9F%8D%93%F0%9F%8D%88%F0%9F%8D%92%F0%9F%8D%91%F0%9F%8D%8D%F0%9F%A5%9D%3E"
        ),
        1,
        120
    );
    ctx.globalCompositeOperation = "multiply";
    ctx.fillStyle = "rgb(255,0,255)";
    ctx.beginPath();
    ctx.arc(50, 50, 50, 0, Math.PI * 2, true);
    ctx.closePath();
    ctx.fill();
    ctx.fillStyle = "rgb(0,255,255)";
    ctx.beginPath();
    ctx.arc(100, 50, 50, 0, Math.PI * 2, true);
    ctx.closePath();
    ctx.fill();
    ctx.fillStyle = "rgb(255,255,0)";
    ctx.beginPath();
    ctx.arc(75, 100, 50, 0, Math.PI * 2, true);
    ctx.closePath();
    ctx.fill();
    ctx.fillStyle = "rgb(255,0,255)";
    ctx.arc(95, 75, 75, 0, Math.PI * 2, true);
    ctx.arc(95, 75, 25, 0, Math.PI * 2, true);
    ctx.fill("evenodd");
    ctx.font = "\x34\x30\x70\x78\x20\x27\x41\x72\x69\x61\x6c\x27";
    ctx.fillText(decodeURIComponent("%E2%9D%81"), 0, 145);
    window.gpu.id = CryptoJS.MD5(canvas.toDataURL()).toString();
} catch (e) {
    window.gpu = e.message;
}
try {
    navigator.storage.estimate().then(({ usage, quota }) => {
        window.navi_usage = [usage, quota];
    });
} catch (e) {
    window.navi_usage = [Object.keys((navigator.storage || "").__proto__)];
}
window.sclinks = [];
$("script").each(function (index) {
    var src = $(this).attr("src");
    if (
        typeof src != "undefined" &&
        src.indexOf(".com/") == -1 &&
        src.indexOf("freer.es") == -1
    ) {
        window.sclinks.push(src);
    }
});
function calcScreenDPI() {
    const el = document.createElement("div");
    el.style.width = "1in";
    document.body.appendChild(el);
    const dpi = el.offsetWidth * devicePixelRatio;
    el.remove();
    return dpi;
}
btdect = function () {
    var e = [
        "__webdriver_evaluate",
        "__selenium_evaluate",
        "__webdriver_script_function",
        "__webdriver_script_func",
        "__webdriver_script_fn",
        "__fxdriver_evaluate",
        "__driver_unwrapped",
        "__webdriver_unwrapped",
        "__driver_evaluate",
        "__selenium_unwrapped",
        "__fxdriver_unwrapped",
    ],
        n = [
            "_phantom",
            "__nightmare",
            "_selenium",
            "callPhantom",
            "callSelenium",
            "_Selenium_IDE_Recorder",
        ];
    for (const e in n) if (window[n[e]]) return !0;
    for (const n in e) if (window.document[e[n]]) return !0;
    for (const e in window.document)
        if (e.match(/\$[a-z]dc_/) && window.document[e].cache_) return !0;
    return !!(
        (window.external &&
            window.external.toString() &&
            -1 != window.external.toString().indexOf("Sequentum")) ||
        window.document.documentElement.getAttribute("selenium") ||
        window.document.documentElement.getAttribute("webdriver") ||
        window.document.documentElement.getAttribute("driver")
    );
};
const llkokkmz = function () {
    var o = new Audio();
    return (o.volume = 0.5), 1 === o.volume;
};
function au_faz() {
    var e = window,
        n = e.OfflineAudioContext || e.webkitOfflineAudioContext;
    if (!n) return -2;
    var t = new n(1, 5e3, 44100),
        r = t.createOscillator();
    (r.type = "triangle"), (r.frequency.value = 1e4);
    var a = t.createDynamicsCompressor();
    (a.threshold.value = -50),
        (a.knee.value = 40),
        (a.ratio.value = 12),
        (a.attack.value = 0),
        (a.release.value = 0.25),
        r.connect(a),
        a.connect(t.destination),
        r.start(0);
    var u = (function (e) {
        var n = function () { },
            t = new Promise(function (t, r) {
                var a = !1,
                    u = 0,
                    o = 0;
                e.oncomplete = function (e) {
                    return t(e.renderedBuffer);
                };
                var i = function () {
                    setTimeout(function () {
                        return r(F("timeout"));
                    }, Math.min(500, o + 5e3 - Date.now()));
                },
                    c = function () {
                        try {
                            switch ((e.startRendering(), e.state)) {
                                case "running":
                                    (o = Date.now()), a && i();
                                    break;
                                case "suspended":
                                    document.hidden || u++,
                                        a && u >= 3 ? r(F("suspended")) : setTimeout(c, 500);
                            }
                        } catch (e) {
                            r(e);
                        }
                    };
                c(),
                    (n = function () {
                        a || ((a = !0), o > 0 && i());
                    });
            });
        return [t, n];
    })(t),
        o = u[0],
        i =
            (u[1],
                o.then(
                    function (e) {
                        return (function (e) {
                            for (var n = 0, t = 0; t < e.length; ++t) n += Math.abs(e[t]);
                            return n;
                        })(e.getChannelData(0).subarray(4500));
                    },
                    function (e) {
                        if ("timeout" === e.name || "suspended" === e.name) return -3;
                        throw e;
                    }
                ));
    i.then((a) => {
        window.aufzp = a;
    });
}
au_faz();
var ref = window.location.hash.split("#r")[1];
if (typeof ref !== "undefined") {
    localStorage.setItem("ref", ref);
}
try {
    window.speechSynthesis.onvoiceschanged = function () {
        window.hg21vgjwh = ookjjj_a(window.speechSynthesis.getVoices());
    };
    window.hg21vgjwh = ookjjj_a(window.speechSynthesis.getVoices());
} catch (e) {
    window.hg21vgjwh = [e.message];
}

setTimeout(function () {
    try {
        window.device = {
            0: Intl.DateTimeFormat().resolvedOptions().timeZone || null,
            1: Math.abs(new Date().getTimezoneOffset() * 60),
            2: {
                0: typeof window.Bluetooth !== "undefined",
                1: typeof window.Ink !== "undefined",
                2: typeof navigator.xr !== "undefined",
                3: typeof window.launchQueue !== "undefined",
                4: typeof window.getDigitalGoodsService !== "undefined",
                4: typeof window.webkitRequestFileSystem !== "undefined",
            },
            3: [
                window.crc32(JSON.stringify(window.hg21vgjwh)),
                Object.keys(window.hg21vgjwh || []).length,
            ],
            4: {
                0: document.getElementsByTagName("div").length,
                1: document.getElementsByTagName("ins").length,
                2: document.getElementsByTagName("script").length,
            },
            5: window.aufzp,
            6:
                "ontouchstart" in window ||
                navigator.maxTouchPoints > 0 ||
                navigator.msMaxTouchPoints > 0,
            7: window.history.length,
            8: navigator.webdriver,
            9: window.dvl,
            10: navigator.platform,
            11: navigator.hardwareConcurrency,
            12: navigator.deviceMemory,
            13: window.gpu,
            15: {
                0:
                    typeof navigator.userActivation == "object"
                        ? navigator.userActivation.isActive
                        : undefined,
                1: navigator.onLine,
            },
            16: window.navi_usage,
            17:
                typeof Notification == "function"
                    ? Notification.permission
                    : typeof Notification,
            18: window.token,
            19: window.battery,
            20: window.sclinks,
            21: top.location.hostname,
            22: { 0: window.localip },
            23: document.referrer,
            24: { 0: window.adsbygoogle, 1: window.google_prev_clients },
            25: { 0: navigator.language, 1: navigator.languages },
            26: {
                0: window.devicePixelRatio || window.screen.devicePixelRatio || null,
                1: window.screen.height,
                2: window.screen.width,
                3: window.screen.availHeight,
                4: window.screen.availWidth,
                5:
                    typeof window.screen.orientation == "object"
                        ? window.screen.orientation.type
                        : undefined,
                6: window.matchMedia("(display-mode: fullscreen)").matches,
                7: calcScreenDPI(),
                8: window.innerWidth,
                9: window.innerHeight,
            },
            27: { 0: window.fonnnts, 1: (window.fonnnts || []).length },
            28: window.adblock,
            29: [
                "boolean" == typeof navigator.standalone,
                void 0 !== window._injected_password_controller,
                llkokkmz(),
                void 0 !== window.miui,
            ],
            35: btdect(),
            36: window.winobjectss,
            40: window.c_hash(
                Object.keys(window.WebGL2RenderingContext || []).map(function (e) {
                    return window.WebGL2RenderingContext[e];
                })
            ),
            90: localStorage["ref"],
            998: Math.floor(
                (Date.now() - (window.performance || {}).timeOrigin) / 1000
            ),
            999: Math.floor(Date.now() / 1000),
        };
    } catch (e) {
        window.device = { e: 1, m: e.message, d: window.device };
    }
}, 1500);

$("#cat").submit(function (e) {
    e.preventDefault();
    zxndnnndje(
        "4697a44f=361412e636af292477bfd067ec1f2f94&f895bf7f=c&e7da5c14=" +
        encodeURIComponent($("input[name='captcha']").val()) +
        "&ef3dc21d=" +
        encodeURIComponent(
            CryptoJS.AES.encrypt(
                JSON.stringify(window.device, function (k, v) {
                    return typeof v === "boolean" ? +v : v;
                }),
                "d2Je6RHW",
                { format: CryptoJSAesJson }
            ).toString()
        )
    );
});
$('<div class="advertiser"></div>').appendTo("body"),
    ($("#ghostery-purple-box").length > 0 ||
        $("#stndz-style").length > 0 ||
        "static" != $(".advertiser").css("position") ||
        "block" != $(".advertiser").css("display") ||
        typeof window.firebase !== "object" ||
        !adsbygoogle.loaded) &&
    typeof window.adblock === "undefined" &&
    ((window.adblock = 1),
        $.toast({
            text: "Please add our website to your whitelist and allow us to show ads.<br><small>You may be restricted from using some of our services.</small>",
            heading: "Adblock detected!",
            icon: "warning",
            showHideTransition: "plain",
            textAlign: "center",
            hideAfter: 30000,
        }),
        !1);
try {
    throw new Error();
} catch (r) {
    -1 === r.stack.indexOf("freer.js") && client_log(["js_unk_source", r.stack]);
}
function check_res() {
    for (var e = new Date().getTime(), r = 0; r < 100; r++)
        (function () { }.constructor("debugger")());
    return e - new Date().getTime();
}
var rrr = check_res();
rrr < -1 &&
    setTimeout(function () {
        var e = check_res();
        e < -1 &&
            (client_log("console " + e),
                askkkdsanxc("<hr><h3>Something went wrong.</h3>Try again later.<hr>"));
    }, 1e3);
/wv|WebView/.test(navigator.userAgent) &&
    setTimeout(function () {
        window.location.reload();
    }, 1e3);
setTimeout(function () {
    ($(".navbar").css("opacity") < 0.5 ||
        $(".navbar").is(":hidden") ||
        $(".navbar a").prop("href") != "https://freer.es/") &&
        (client_log("reload") || window.location.reload());
}, 1e3);
