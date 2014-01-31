define [
  'underscore'
  'backbone'
], (_, Backbone) ->
  'use strict';

  class Profile extends Backbone.Model

    inGame: () ->
      if @attributes.gameName
        return 'in-game'
      return ''

  return Profile
