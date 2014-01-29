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
      markdown: {
        exports: 'markdown'
      },
      handlebars: {
        exports: 'Handlebars'
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
      markdown: '../bower_components/markdown/lib/markdown',
      moment: '../bower_components/momentjs/moment',
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

  require(['backbone', 'jquery', 'cs!app'], function(Backbone, $, app) {

    $(function() {
      app.ready();

      // prevent links from triggering navigation to the server
      // adapted from http://stackoverflow.com/questions/16966321/how-to-properly-use-html5-pushstate-in-backbone-js
      // it'd be nice to find a better solution
      $(document).on('click', 'a', function(e){
        var href = $(this).prop('href'),
            root = location.protocol+'//'+location.host+'/';

        if (root === href.slice(0, root.length)){
          e.preventDefault();
          Backbone.history.navigate(href.slice(root.length), true);
        }
      });
    });
  });
}).call(this);
