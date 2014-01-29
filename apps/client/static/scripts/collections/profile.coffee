define [
  'underscore'
  'backbone'
  'cs!models/profile'
], (_, Backbone, Profile) ->

  class ProfileCollection extends Backbone.Collection
    model: Profile

  return ProfileCollection
