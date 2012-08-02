define(['backbone-tastypie', 'jquery', 'underscore'], function(Backbone, $, _) {
    'use strict';

    var Server = Backbone.Model.extend({

    });

    var ServerList = Backbone.Collection.extend({
        model: Server,
        url: '/api/v1/server/?format=json'
    });

    var ServerView = Backbone.View.extend({
        tagName:  'li',
        template: _.template($('#server_template').html()),

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
            this.model = new ServerList();
            this.model.bind('reset', this.render, this);
            this.model.fetch();
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
