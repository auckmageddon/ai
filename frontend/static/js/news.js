define(['backbone-tastypie', 'jquery', 'underscore'], function(Backbone, $, _) {

    var Entry = Backbone.Model.extend({

    });

    var News = Backbone.Collection.extend({
        model: Entry,
        url: 'http://localhost:8000/api/v1/entry/?format=json'
    });

    var EntryView = Backbone.View.extend({
        tagName:  'li',
        template: _.template($('#news_entry_template').html()),

        render: function(eventName) {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        }
    });

    var NewsView = Backbone.View.extend({
        tagName: 'ul',
        id: 'news',

        events: {
            'change': 'render'
        },

        initialize: function() {
            this.model = new News();
            this.model.bind('reset', this.render, this);
            this.model.fetch();
        },

        render: function(eventName) {
            this.$el.html('');
            _.each(this.model.models, function (entry) {
                this.$el.append(new EntryView({model: entry}).render().el);
            }, this);
            return this;
        }
    });

    return {
        Entry: Entry,
        News:  News,
        NewsView: NewsView
    };

});
