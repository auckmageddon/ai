define(['backbone', 'jquery', 'underscore'], function(Backbone, $, _) {
    'use strict';

    var Tournament = Backbone.Model.extend({

    });

    var TournamentList = Backbone.Collection.extend({
        model: Tournament,
        url: '/api/v2/tournament/?format=json'
    });

    var TournamentView = Backbone.View.extend({
        tagName:  'li',
        template: _.template($('#tournament_template').html()),

        render: function(eventName) {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        }
    });

    var TournamentListView = Backbone.View.extend({
        tagName: 'ul',
        el: '#tournaments',

        events: {
            'change': 'render'
        },

        initialize: function() {
            this.model = new TournamentList();
            this.model.bind('reset', this.render, this);
            this.model.fetch();
        },

        render: function(eventName) {
            this.$el.html('');
            _.each(this.model.models, function (tournament) {
                this.$el.append(new TournamentView({model: tournament}).render().el);
            }, this);
            return this;
        }
    });

    return {
        Tournament:  Tournament,
        TournamentListView: TournamentListView
    };

});
