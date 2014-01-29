define [
  'backbone'
  'handlebars'
  'jquery'
  'markdown'
  'underscore'
], (Backbone, Handlebars, $, Markdown, _) ->
  class ArticleView extends Backbone.View
    Handlebars.registerHelper 'markdown', (content) ->
      rendered = Markdown.toHTML content
      return new Handlebars.SafeString(rendered)

    template: Handlebars.compile '
      {{#each models}}
        <article class="row">
            <h1>{{ attributes.title }}</h1>
            <div class="content">
              {{ markdown attributes.content }}
            </div>
        </article>
      {{/each}}
    '

    render: (eventName) ->
      @$el.html(@template(@collection))
      return this

  return ArticleView
