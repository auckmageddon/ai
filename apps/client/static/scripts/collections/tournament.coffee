define [
  'underscore'
  'backbone'
  'cs!models/event'
], (_, Backbone, Tournament) ->

  class TournamentCollection extends Backbone.Collection
    model: Tournament

  return TournamentCollection
