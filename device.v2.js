const Device = class {
    static getDevice() {
        return {
            0: "Europe/Dublin",
            1: 0,
            2: { 0: true, 1: true, 2: true, 3: true, 4: true },
            3: [this.randint(154243263, 354243263), this.randint(100, 300)],
            4: { 0: 25, 1: 1, 2: 19 },
            5: this.randint(50, 100),
            6: false,
            7: 2,
            8: false,
            10: "MacIntel",
            11: 8,
            12: 8,
            13: {
                render: "ANGLE (Apple, Apple M2, OpenGL 4.1)",
                vendor: "Google Inc. (Apple)",
                p: this.randint(1000, 6000),
                id: this.randhex(16),
            },
            15: { 0: true, 1: true },
            16: [this.randint(11715, 16715), this.randint(107064317542, 147064317542)],
            17: "denied",
            19: { isc: false, lvl: 40, ct: null, dct: 8400 },
            20: [],
            21: "freer.es",
            22: { 0: `${this.uuid()}.local` },
            23: "",
            24: { 0: [{}] },
            25: { 0: "en", 1: ["en", "fr-FR", "es-ES", "es", "fr", "en-US", "am", "de"] },
            26: {
                0: 2,
                1: 956,
                2: 1470,
                3: 845,
                4: 1470,
                5: "landscape-primary",
                6: false,
                7: 192,
                8: 385,
                9: 766,
            },
            27: { 0: ["Baskerville"], 1: 1 },
            28: 1,
            29: [false, false, false, false],
            35: false,
            36: [
                "queryLocalFonts",
                "define",
                "returnCommentSymbol",
                "savedChPos",
                "returnedSuggestion",
                "suggestionsStatus",
                "docLang",
                "suggestionDisplayed",
                "isReturningSuggestion",
                "acceptTab",
                "acceptSuggestion",
                "displayGrey",
                "updateSuggestionStatus",
                "formatCode",
                "insert",
            ],
            40: this.randint(4110500686, 4310500686),
            998: 4,
            999: Math.floor(Date.now() / 1000),
        }
    }

    static randhex = size       => [...Array(size)].map(() => Math.floor(Math.random() * 16).toString(16)).join('')
    static randint = (min, max) => Math.floor(Math.random() * (Math.floor(max) - Math.ceil(min) + 1)) + Math.ceil(min);
    static uuid    = ()         => 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
        return v.toString(16);
    });
};

console.log(Device.getDevice());