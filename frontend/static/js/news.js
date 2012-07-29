define(['backbone', 'jquery', 'underscore'], function(Backbone, $, _) {

    var Entry = Backbone.Model.extend({

    });

    var News = Backbone.Collection.extend({

    });

    var EntryView = Backbone.View.extend({
        tagName:  'li',
        template: _.template('<%= title %>'),

        render: function(eventName) {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        }
    });

    var NewsView = Backbone.View.extend({
        tagName: 'ul',
        el: '#news',

        events: {
            'change': 'render'
        },

        initialize: function() {
            this.model.bind('reset', this.render, this);
        },

        render: function(eventName) {
            _.each(this.model.models, function (entry) {
                this.$el.append(new EntryView({model: entry}).render().el);
            }, this);
            return this;
        }
    });

    return {
        News:  News,
        NewsView: NewsView
    }

});