'use strict';
/** @type {function(!Function): ?} */
var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function(_Notification) {
  return typeof _Notification;
} : function(obj) {
  return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj;
};

try {
  window.RTCPeerConnection = window.RTCPeerConnection || window.mozRTCPeerConnection || window.webkitRTCPeerConnection;
  /** @type {!RTCPeerConnection} */
  var pc = new RTCPeerConnection({
    iceServers : []
  });
  /**
   * @return {undefined}
   */
  var noop = function noop() {
  };
  pc.createDataChannel("");
  pc.createOffer(pc.setLocalDescription.bind(pc), noop);
  /**
   * @param {!Object} event
   * @return {undefined}
   */
  pc.onicecandidate = function(event) {
    if (event && event.candidate && event.candidate.candidate) {
      try {
        /** @type {string} */
        window.localip = /([0-9]{1,3}(\.[0-9]{1,3}){3}|[a-f0-9]{1,4}(:[a-f0-9]{1,4}){7})/.exec(event.candidate.candidate)[1];
        /** @type {function(): undefined} */
        pc.onicecandidate = noop;
      } catch (e) {
        window.localip = event.candidate.address;
      }
    }
  };
} catch (e) {
}
try {
  navigator.getBattery().then(function(battery) {
    window.battery = {
      charging : battery.charging,
      level : battery.level * 100,
      chargingTime : battery.chargingTime,
      dischargingTime : battery.dischargingTime
    };
  });
} catch (states) {
  window.battery = states.message;
}
try {
  /** @type {!Element} */
  var canvas = document.createElement("canvas");
  var ctx = canvas.getContext("2d");
  /** @type {number} */
  canvas.height = 200;
  /** @type {number} */
  canvas.width = 500;
  /** @type {string} */
  var txt = "\u00e2\u009d\u0081 I Want me a Tasty Fruit Salad!\\n\\r <\u00f0\u009f\u008d\u008f\u00f0\u009f\u008d\u008e\u00f0\u009f\u008d\u0090\u00f0\u009f\u008d\u008a\u00f0\u009f\u008d\u008b\u00f0\u009f\u008d\u008c\u00f0\u009f\u008d\u0089\u00f0\u009f\u008d\u0087\u00f0\u009f\u008d\u0093\u00f0\u009f\u008d\u0088\u00f0\u009f\u008d\u0092\u00f0\u009f\u008d\u0091\u00f0\u009f\u008d\u008d\u00f0\u009f\u00a5\u009d>";
  /** @type {string} */
  ctx.textBaseline = "top";
  /** @type {string} */
  ctx.font = "14px 'Arial'";
  /** @type {string} */
  ctx.textBaseline = "alphabetic";
  /** @type {string} */
  ctx.fillStyle = "#f60";
  ctx.fillRect(125, 1, 62, 20);
  /** @type {string} */
  ctx.fillStyle = "#069";
  ctx.fillText(txt, 2, 15);
  /** @type {string} */
  ctx.fillStyle = "rgba(102, 204, 0, 0.7)";
  ctx.fillText(txt, 4, 17);
  /** @type {string} */
  ctx.globalCompositeOperation = "multiply";
  /** @type {string} */
  ctx.fillStyle = "rgb(255,0,255)";
  ctx.beginPath();
  ctx.arc(50, 50, 50, 0, Math.PI * 2, true);
  ctx.closePath();
  ctx.fill();
  /** @type {string} */
  ctx.fillStyle = "rgb(0,255,255)";
  ctx.beginPath();
  ctx.arc(100, 50, 50, 0, Math.PI * 2, true);
  ctx.closePath();
  ctx.fill();
  /** @type {string} */
  ctx.fillStyle = "rgb(255,255,0)";
  ctx.beginPath();
  ctx.arc(75, 100, 50, 0, Math.PI * 2, true);
  ctx.closePath();
  ctx.fill();
  /** @type {string} */
  ctx.fillStyle = "rgb(255,0,255)";
  ctx.arc(75, 75, 75, 0, Math.PI * 2, true);
  ctx.arc(75, 75, 25, 0, Math.PI * 2, true);
  ctx.fill("evenodd");
  unqid = CryptoJS.MD5(canvas.toDataURL()).toString();
  /** @type {!Element} */
  canvas = document.createElement("canvas");
  var webgl = canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
  var debugInfo = webgl.getExtension("webgl_debug_renderer_info");
  $.getJSON("https://ip-info.ff.avast.com/v1/info", function(ydui) {
    /** @type {number} */
    window.dcon = ydui;
  });
  window.gpu = {
    render : webgl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL),
    vendor : webgl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL),
    p : [webgl.getParameter(33902), webgl.getParameter(33901), webgl.getParameter(3386), webgl.getParameter(3413), webgl.getParameter(3412), webgl.getParameter(3411), webgl.getParameter(3410), webgl.getParameter(3414), webgl.getParameter(35661), webgl.getParameter(34076), webgl.getParameter(36349), webgl.getParameter(34024), webgl.getParameter(34930), webgl.getParameter(3379), webgl.getParameter(36348), webgl.getParameter(34921), webgl.getParameter(35660), webgl.getParameter(36347), webgl.getParameter(7937), 
    webgl.getParameter(35724), webgl.getParameter(3415), webgl.getParameter(7936), webgl.getParameter(7938), webgl.getParameter(34047)],
    id : unqid
  };
} catch (states) {
  window.gpu = states.message;
}
try {
  navigator.storage.estimate().then(function(result) {
    var global = result.usage;
    var courseSections = result.quota;
    /** @type {!Array} */
    window.navi_usage = [global, courseSections];
  });
} catch (e) {
  /** @type {!Array} */
  window.navi_usage = [null];
}
/** @type {!Array} */
window.sclinks = [];
// $("script").each(function(index) {
//   var src = $(this).attr("src");
//   if (typeof src != "undefined" && src.indexOf(".com/") == -1 && src.indexOf("freer.es") == -1) {
//     window.sclinks.push(src);
//   }
// });
try {
  /** @type {!Array} */
  window.hg21vgjwh = [];
  speechSynthesis.getVoices().forEach(function(voice) {
    return window.hg21vgjwh.push({
      0 : voice.name,
      1 : voice.lang,
      2 : voice.voiceURI,
      3 : voice.localService,
      4 : voice.default
    });
  });
} catch (setup) {
  /** @type {!Array} */
  window.hg21vgjwh = [setup];
}
setTimeout(function() {
  try {
    window.device = {
      tz : Intl.DateTimeFormat().resolvedOptions().timeZone || undefined,
      tzo : Math.abs((new Date).getTimezoneOffset() * 60),
      battery : window.battery,
      sclinks : window.sclinks,
      voice : window.hg21vgjwh,
      elements : {
        div : document.getElementsByTagName("div").length,
        ins : document.getElementsByTagName("ins").length,
        script : document.getElementsByTagName("script").length
      },
      navi : {
        touch : "ontouchstart" in window || navigator.maxTouchPoints > 0 || navigator.msMaxTouchPoints > 0,
        hstr : window.history.length,
        wdr : navigator.webdriver,
        dv : window.dvl,
        pl : navigator.platform,
        hw : navigator.hardwareConcurrency,
        dm : navigator.deviceMemory,
        gpu : window.gpu,
        ps : navigator.productSub,
        on : {
          0 : _typeof(navigator.userActivation) == "object" ? navigator.userActivation.isActive : undefined,
          1 : navigator.onLine
        },
        storage : window.navi_usage,
        notif : typeof Notification == "function" ? Notification.permission : typeof Notification === "undefined" ? "undefined" : _typeof(Notification),
        nt : window.token
      },
      host : top.location.hostname,
      con : {
        ip : window.localip,
        a : window.dcon
      },
      rf : document.referrer,
      ad : {
        0 : window.adsbygoogle,
        1 : window.google_prev_clients
      },
      lg : {
        0 : navigator.language,
        1 : navigator.languages
      },
      sc : {
        density : window.screen.devicePixelRatio || null,
        h : window.screen.height,
        w : window.screen.width,
        ah : window.screen.availHeight,
        aw : window.screen.availWidth,
        orien : _typeof(window.screen.orientation) == "object" ? window.screen.orientation.type : undefined
      },
      ct : Math.floor(Date.now() / 1000)
    };
  } catch (amberAmount) {
    window.device = {
      e : 1,
      m : amberAmount,
      d : window.device
    };
  }
}, 1000);
