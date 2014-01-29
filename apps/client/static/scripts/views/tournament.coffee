define [
  'jquery'
  'underscore'
  'backbone'
  'handlebars'
], ($, _, Backbone) ->
  class TournamentView extends Backbone.View
    template: Handlebars.compile '
      <iframe src="{{ attributes.challongeUrl }}" width="100%" height="500" frameborder="0" scrolling="auto" allowtransparency="true"></iframe>
    '

    render: (eventName) ->
      @$el.html(@template(@model))
      return this

  return TournamentView
