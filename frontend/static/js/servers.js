define(['backbone-tastypie', 'jquery', 'underscore'], function(Backbone, $, _) {
    'use strict';

    var Server = Backbone.Model.extend({

    });

    var ServerList = Backbone.Collection.extend({

    });

    var ServerView = Backbone.View.extend({
        tagName:  'li',
        template: _.template('<%= title %>'),

        render: function(eventName) {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        }
    });

    var ServerListView = Backbone.View.extend({
        tagName: 'ul',
        el: '#servers',

        events: {
            'change': 'render'
        },

        initialize: function() {
            this.model.bind('reset', this.render, this);
        },

        render: function(eventName) {
            this.$el.html('');
            _.each(this.model.models, function (server) {
                this.$el.append(new ServerView({model: server}).render().el);
            }, this);
            return this;
        }
    });

    return {
        Server:  Server,
        ServerListView: ServerListView
    };

});
