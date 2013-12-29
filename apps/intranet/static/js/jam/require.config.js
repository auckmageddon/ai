var jam = {
    "packages": [
        {
            "name": "bootstrap",
            "location": "static/js/jam/bootstrap"
        },
        {
            "name": "less",
            "location": "static/js/jam/less",
            "main": "./lib/index.js"
        },
        {
            "name": "underscore",
            "location": "static/js/jam/underscore",
            "main": "underscore.js"
        },
        {
            "name": "jquery",
            "location": "static/js/jam/jquery",
            "main": "jquery.js"
        },
        {
            "name": "backbone",
            "location": "static/js/jam/backbone",
            "main": "backbone.js"
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
