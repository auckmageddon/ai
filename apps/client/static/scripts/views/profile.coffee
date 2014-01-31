define [
  'jquery'
  'underscore'
  'backbone'
  'd3'
  'nvd3'
  'handlebars'
  'cs!models/profile'
], ($, _, Backbone, d3, nv, Handlebars, Profile) ->

  _renderProfile = Handlebars.compile  '
      <div class="profile row">
        <div class="columns large-2">
          <img src="{{ attributes.avatarUrl }}" class="{{ inGame }}"></img>
        </div>
        <div class="large-10 columns">
          <h4>{{ attributes.username }}</h4>
          <p>
          {{#if inGame}}
            {{#if attributes.gameIp}}
              Currently playing <a href="steam://connect/{{ attributes.gameIp }}">{{ attributes.gameName}}</a>
            {{else}}
              Currently playing <a href="steam://run/{{ attributes.gameId }}">{{ attributes.gameName}}</a>
            {{/if}}
          {{else}}
            &nbsp;
          {{/if}}
          </p>
        </div>
      </div>
    '

  _renderAddProfile = Handlebars.compile '
      <h2>Add Account</h2>
      {{#if this}}
        {{renderProfile this}}
        <form action="#" id="confirm-profile" class="clearfix">
          <input id="no" class="right button secondary" type="button" value="This Isn\'t Me">
          <input id="yes" class="right button success" type="submit" value="Confirm">
        </form>
      {{else}}
        <form action="#" id="add-profile">
          <div class="row">
            <div class="small-6 columns">
              <label for="steam-id" class="right inline">http://steamcommunity.com/id/</label>
            </div>
            <div class="small-6 columns">
              <input id="steam-id" type="text" name="steam-id">
            </div>
          </div>
          <input type="submit" class="button success right" value="Validate">
        </form>
      {{/if}}
    '

  Handlebars.registerHelper 'renderProfile', (profile) ->
    return new Handlebars.SafeString _renderProfile profile


  Handlebars.registerHelper 'renderAddProfile', (conditionalProfile) ->
    return new Handlebars.SafeString _renderAddProfile conditionalProfile


  class ProfileView extends Backbone.View
    template: Handlebars.compile '
      <div class="row">
        <div id="chart"><svg></svg></div>
      </div>
      <div class="row">
        <div id="add-steam-account" class="clearfix">
          {{#unless profileId}}
            {{renderAddProfile conditionalProfile}}
          {{/unless}}
        </div>
        <div id="players">
        <h2>Players</h2>
        {{#each profiles.models}}
          {{renderProfile this}}
        {{/each}}
        </div>
      </div>
    '


    initialize: (config) ->
      @steamIdSource = config.steamIdSource
      @conditionalProfile = null
      @profileId = config.profileId
      @listenTo @collection, 'sync', @render


    events:
      'submit form#add-profile':         'onGetProfile'
      'submit form#confirm-profile':     'onAcceptProfile'
      'click #no':      'onDeclineProfile'


    onGetProfile: (e) =>
      e.preventDefault()
      form = $(e.target)
      name = form.find('input[name="steam-id"]').val()
      $.getJSON(@steamIdSource, {'name': name})
        .done(@onReceiveProfile)
        .fail(() -> alert('Failed to find a profile with that URL'))


    onReceiveProfile: (data, status) =>
      @conditionalProfile = new Profile data
      @render()


    onAcceptProfile: (e) =>
      e.preventDefault()
      @profileId = @conditionalProfile.attributes.steamId
      @collection.create {steamId: @conditionalProfile.attributes.steamId}, {wait: true}
      @conditionalProfile = null
      @render()


    onDeclineProfile: (e) =>
      e.preventDefault()
      @conditionalProfile = null
      @render()
      @$el.find('input[name="steam-id"]').focus()
      return


    render: (eventName) =>
      @$el.html(@template(
        profiles: @collection
        conditionalProfile: @conditionalProfile
        profileId: @profileId
      ))

      nv.addGraph () =>
        chart = nv.models.multiBarHorizontalChart()
          .margin({top: 30, right: 20, bottom: 50, left: 175})
          .x((d) -> d.label)
          .y((d) -> d.value)
          # .staggerLabels(true)
          .tooltips(false)
          .showLegend(false)
          .showControls(false)
          .showValues(true)

        d3.select(@$el.find('#chart svg')[0])
          .datum(@collection.totalsByGame())
          .transition()
          .duration(500)
          .call(chart)

        nv.utils.windowResize chart.update

        return chart

      return this


  return ProfileView
