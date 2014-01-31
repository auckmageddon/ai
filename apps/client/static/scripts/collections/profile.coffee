define [
  'underscore'
  'backbone'
  'cs!models/profile'
], (_, Backbone, Profile) ->

  class ProfileCollection extends Backbone.Collection
    model: Profile

    totalsByGame: () =>
      totals = @groupBy('gameName')
      totals = _.map totals, (count, name) ->
        return {
          'label': name
          'value': count.length
        }
      totals = _.filter totals, (ele) ->
        return ele.label && ele.label != "null"

      return [{
          'key': 'Games Played'
          'values': totals
        }]

  return ProfileCollection
