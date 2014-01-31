/**
* Build profile for a standalone django-require module, packaged with almond.js.
*
* This supports all the normal configuration available to a r.js build profile. The only gotchas are:
*
* - 'baseUrl' will be overidden by django-require during the build process.
* - 'name' will be overidden by django-require during the build process.
* - 'include' will be overidden by django-require during the build process.
* - 'out' will be overidden by django-require during the build process.
*/
({
  wrap: false,
  optimize: 'uglify2', // uglify2
  preserveLicenseComments: true,
  shim: {
    backbone: {
      deps: [
        'underscore',
        'jquery'
      ],
      exports: 'Backbone'
    },
    d3: {
      exports: 'd3'
    },
    handlebars: {
      exports: 'Handlebars'
    },
    jquery: {
      exports: '$'
    },
    nvd3: {
      exports: 'nv',
      deps: ['d3']
    },
    underscore: {
      exports: '_'
    }
  },
  stubModules: [
  	'cs'
  ],
  exclude: [
    'coffee-script'
  ],
  paths: {
    backbone: '../bower_components/backbone/backbone',
    d3: '../bower_components/d3/d3',
    foundation: '../bower_components/foundation/js/foundation',
    handlebars: '../bower_components/handlebars/handlebars',
    jquery: '../bower_components/jquery/jquery',
    modernizr: '../bower_components/modernizr/modernizr',
    moment: '../bower_components/momentjs/moment',
    nvd3: '../bower_components/nvd3/nv.d3',
    underscore: '../bower_components/underscore/underscore',
    'cs': '../bower_components/require-cs/cs',
    'coffee-script': '../bower_components/coffee-script/index'
  }

})
