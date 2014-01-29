define [
  'underscore'
  'backbone'
  'cs!models/event'
], (_, Backbone, Event) ->

  class EventCollection extends Backbone.Collection
    model: Event

  return EventCollection
