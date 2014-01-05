#/*global require*/
define [
  'backbone',
  'cs!collections/article'
  'cs!views/article'
], (Backbone, Articles, ArticleView) ->

  init = ->
    articles = new Articles
    articles.url = AI.CONFIG.articles

    view = new ArticleView
      collection: articles
      el: '#main'

    articles.fetch
      reset: true
      success: ->
        view.render()

    Backbone.history.start()
    return

  return {
    init: init
  }
