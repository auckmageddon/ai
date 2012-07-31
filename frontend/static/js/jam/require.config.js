var jam = {
    "packages": [
        {
            "name": "bootstrap",
            "location": "js/jam/bootstrap"
        },
        {
            "name": "less",
            "location": "jam/less",
            "main": "./lib/index.js"
        },
        {
            "name": "underscore",
            "location": "js/jam/underscore",
            "main": "underscore.js"
        },
        {
            "name": "jquery",
            "location": "js/jam/jquery",
            "main": "jquery.js"
        },
        {
            "name": "backbone",
            "location": "js/jam/backbone",
            "main": "backbone.js"
        },
        {
            "name": "backbone-tastypie",
            "location": "js/jam/backbone-tastypie",
            "main": "backbone-tastypie.js"
        }
    ],
    "version": "0.1.14",
    "shim": {}
};

if (typeof require !== "undefined" && require.config) {
    require.config({packages: jam.packages, shim: jam.shim});
}
else {
    var require = {packages: jam.packages, shim: jam.shim};
}

if (typeof exports !== "undefined" && typeof module !== "undefined") {
    module.exports = jam;
}