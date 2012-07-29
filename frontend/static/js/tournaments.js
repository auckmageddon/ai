define(['backbone', 'jquery', 'underscore'], function(Backbone, $, _) {

    var Tournament = Backbone.Model.extend({

    });

    var TournamentList = Backbone.Collection.extend({

    });

    var ServerView = Backbone.View.extend({
        tagName:  'li',
        template: _.template('<%= title %>'),

        render: function(eventName) {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        }
    });

    var TournamentListView = Backbone.View.extend({
        tagName: 'ul',
        el: '#tournments',

        events: {
            'change': 'render'
        },

        initialize: function() {
            this.model.bind('reset', this.render, this);
        },

        render: function(eventName) {
            _.each(this.model.models, function (tournament) {
                this.$el.append(new TournamentView({model: tournament}).render().el);
            }, this);
            return this;
        }
    });

    return {
        Tournament:  Tournament,
        TournamentView: TournamentView
    }

});