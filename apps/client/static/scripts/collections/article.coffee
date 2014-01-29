define [
  'underscore'
  'backbone'
  'cs!models/article'
], (_, Backbone, Article) ->

  class ArticleCollection extends Backbone.Collection
    model: Article

  return ArticleCollection
