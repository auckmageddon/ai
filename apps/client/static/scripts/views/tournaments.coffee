define [
  'jquery'
  'underscore'
  'backbone'
  'handlebars'
  'cs!views/tournament'
], ($, _, Backbone, Handlebars, TournamentView) ->
  class TournamentsView extends Backbone.View
    template: Handlebars.compile '
      <div class="row">
        <ul class="side-nav large-2 columns">
          {{#each models}}
            <li><a href="/tournament/{{ attributes.id }}/">{{ attributes.name }}</a></li>
          {{/each}}
        </ul>
        <div id="tournament" class="large-10 columns">

        </div>
      </div>
    '

    activate: (id) ->
      if id
        model = @collection.get id
        subView = new TournamentView
          el: '#tournament'
          model: model
        subView.render()
        # @$el.find('#tournament').html(subView.render().el)

    render: (eventName) ->
      @$el.html(@template(@collection))
      return this

  return TournamentsView
