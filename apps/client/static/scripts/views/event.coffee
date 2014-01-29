define [
  'jquery'
  'underscore'
  'backbone'
  'handlebars'
  'moment'
], ($, _, Backbone, Handlebars, moment) ->

  Handlebars.registerHelper 'moment', (date, format) ->
    return moment(date).format(format)

  class EventView extends Backbone.View


    template: Handlebars.compile '
      {{#each models}}
        <div class="event row">
          <div class="timestamp large-4 columns">{{ moment attributes.happeningAt "dddd, HH:mm" }}</div>
          <div class="details large-8 columns">{{ attributes.name }}</div>
        </div>
      {{/each}}
    '

    render: (eventName) ->
      @$el.html @template @collection
      return this

  return EventView
