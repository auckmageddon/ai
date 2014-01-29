define [
  'jquery',
  'underscore',
  'backbone',
  'handlebars'
], ($, _, Backbone, Handlebars) ->
  class MainView extends Backbone.View

    activate: (view) =>
      @activeView = view
      @render()

    render: (eventName) ->
      @$el.html @activeView.render().el
      return this

  return MainView
