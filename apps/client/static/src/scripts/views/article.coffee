define [
  'jquery'
  'underscore'
  'backbone'
  'handlebars'
], ($, _, Backbone, Handlebars) ->
  class ArticleView extends Backbone.View
    template: Handlebars.compile "
      {{#each models}}
        <div>
            <p>{{ attributes.content }}</p>
        </div>
      {{/each}}
    "

    render: (eventName) ->
      console.log @collection
      @$el.html(@template(@collection))
      return this

  return ArticleView
