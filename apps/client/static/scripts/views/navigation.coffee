define [
  'jquery',
  'underscore',
  'backbone',
  'handlebars'
], ($, _, Backbone, Handlebars) ->
  class NavigationView extends Backbone.View

    # events:
    #   'hover a[href="/article/"]':    'article'
    #   'hover a[href="/event/"]':      'event'
    #   'hover a[href="/tournament/"]': 'tournament'

  return NavigationView
