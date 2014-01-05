define [
  'jquery'
  'underscore'
  'backbone'
  'templates'
], ($, _, Backbone, JST) ->
  class IndexView extends Backbone.View
    template: JST['app/scripts/templates/index.hbs']