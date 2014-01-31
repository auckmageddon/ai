#/*global require*/
define [
  'backbone'
  'cs!collections/article'
  'cs!collections/event'
  'cs!collections/profile'
  'cs!collections/tournament'
  'cs!views/article'
  'cs!views/event'
  'cs!views/main'
  'cs!views/navigation'
  'cs!views/profile'
  'cs!views/tournaments'
], (Backbone, Articles, Events, Profiles, Tournaments, ArticleView, EventView, MainView, NavigationView, ProfileView, TournamentView) ->

  mainView = new MainView
    el: '#main'

  articles = new Articles()
  articles.url = AI.CONFIG.articleSource

  profiles = new Profiles()
  profiles.url = AI.CONFIG.profileSource

  events = new Events()
  events.url = AI.CONFIG.eventSource

  tournaments = new Tournaments()
  tournaments.url = AI.CONFIG.tournamentSource

  articleView = new ArticleView
    collection: articles

  eventView = new EventView
    collection: events

  profileView = new ProfileView
    collection:    profiles
    steamIdSource: AI.CONFIG.steamIdSource
    profileId:     AI.CONFIG.profileId

  tournamentView = new TournamentView
    collection: tournaments

  class App extends Backbone.Router

    routes:
      'article/': 'article'
      'event/': 'event'
      'profile/': 'profile'
      'tournament/(:id/)': 'tournament'
      '*default': 'defaultRoute'

    defaultRoute: ->
      @navigate '/article/',
        trigger: true

    article: ->
      articles.fetch
        reset: true
        success: ->
          mainView.activate(articleView)

    event: () ->
      events.fetch
        reset: true
        success: ->
          mainView.activate(eventView)

    profile: ->
      profiles.fetch
        reset: true
        success: ->
          mainView.activate(profileView)

    tournament: (id) ->
      tournaments.fetch
        reset: true
        success: ->
          mainView.activate(tournamentView)
          tournamentView.activate(id)

  @app = new App()

  ready = =>
    navigationView = new NavigationView
      router: @app
      el: '#navigation'

    Backbone.history.start
      pushState: true

    return

  return {
    ready: ready
  }
