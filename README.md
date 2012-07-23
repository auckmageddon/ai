ai
==
auckmageddon intranet project

setup
-----

    virtualenv env --no-site-packages
    env/bin/activate
    pip install -r requirements.txt

Other Stuff
-----------
We're using the following support projects:

 * Twitter Bootstrap (for CSS)
 * LESS (required by Bootstrap)
 * HTML5BP (basic HTML5 template)
 * require.js (for managing the Javascript stuff)
 * jQuery
 * modernizr
 * Backbone.js (?)
 * underscore.js

Most of these files can be found collected, and ready for use as AMD
modules for require.js in static-src.

In order to use the LESS compiler and require.js from the commandline,
it's probably a good idea to install node.js.

It's also probably a good idea to grab grunt (http://gruntjs.com/) and
jam (http://jamjs.org/) (both can be installed via node's npm),
because they'll eventually be used - just not yet.

(I wish yeoman.io had been released already).
