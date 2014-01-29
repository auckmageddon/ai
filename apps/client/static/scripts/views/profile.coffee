define [
  'jquery',
  'underscore',
  'backbone',
  'handlebars'
], ($, _, Backbone, Handlebars) ->
  class ProfileView extends Backbone.View
    template: Handlebars.compile '
      <div class="large-6 columns">
        Stats here
      </div>
      <div class="large-6 columns">
        <div id="add-steam-account">
          {{#if conditionalProfile}}
            Is {{ conditionalProfile.username }} you?
            <a href="#" id="yes">yes</a>
            <a href="#" id="no">no</a>
          {{else}}
          Enter your Steam URL here:
          <form action="{{ steamIdSource }}">
            http://steamcommunity.com/id/
            <input name="steam-id">
            <input type="submit" id="derp">
          </form>
          {{/if}}
        </div>
        {{#each profiles.models}}
          <div>
            <img src="{{ attributes.avatarUrl }}"></img>
            {{ attributes.username }}
          </div>
        {{/each}}
      </div>

    '

    initialize: (config) ->
      @steamIdSource = config.steamIdSource
      @conditionalProfile = null
      @listenTo @collection, 'sync', @render


    events:
      'submit form':    'onGetProfile'
      'click #yes':     'onAcceptProfile'
      'click #no':      'onDeclineProfile'


    onGetProfile: (e) =>
      e.preventDefault()
      form = $(e.target)
      name = form.find('input[name="steam-id"]').val()
      $.get(@steamIdSource, {'name': name}, @onReceiveProfile, 'json')


    onReceiveProfile: (data, status) =>
      @conditionalProfile = data
      @render()


    onAcceptProfile: (e) =>
      e.preventDefault()
      @collection.create {steamId: @conditionalProfile.steamId}, {wait: true}
      @conditionalProfile = null
      @render()


    onDeclineProfile: (e) =>
      @conditionalProfile = null
      @render()
      @$el.find('input[name="steam-id"]').focus()
      return


    render: (eventName) =>
      @$el.html(@template(
        profiles: @collection
        steamIdSource: @steamIdSource
        conditionalProfile: @conditionalProfile
      ))
      return this

  return ProfileView
