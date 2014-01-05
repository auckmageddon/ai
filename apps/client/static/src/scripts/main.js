/*
 * Shim -- the main app is CoffeeScript, but we need something that'll load
 * that in our browser.  This file handles that.
 */
/*global require*/
(function() {
  'use strict';
  require.config({
    shim: {
      backbone: {
        deps: [
          'underscore',
          'jquery'
        ],
        exports: 'Backbone'
      },
      handlebars: {
        exports: 'Handlebars'
      },
      jquery: {
        exports: '$'
      },
      underscore: {
        exports: '_'
      }
    },
    paths: {
      backbone: '../bower_components/backbone/backbone',
      foundation: '../bower_components/foundation/js/foundation',
      handlebars: '../bower_components/handlebars/handlebars',
      jquery: '../bower_components/jquery/jquery',
      modernizr: '../bower_components/modernizr/modernizr',
      underscore: '../bower_components/underscore/underscore'
    },
    packages: [
      {
        name: 'cs',
        location: '../bower_components/require-cs',
        main: 'cs'
      },
      {
        name: 'coffee-script',
        location: '../bower_components/coffee-script',
        main: 'index'
      }
    ]
  });

  require(['jquery', 'cs!app'], function($, app) {
    // $() executes on DOMContentLoaded
    $(function() {
      app.init();
    });
  });

}).call(this);
