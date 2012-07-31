define(['backbone-tastypie', 'jquery', 'underscore'], function(Backbone, $, _) {

    var Event = Backbone.Model.extend({

    });

    var Schedule = Backbone.Collection.extend({

    });

    var EventView = Backbone.View.extend({
        tagName:  'li',
        template: _.template($('#schedule_event_template').html()),

        render: function(eventName) {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        }
    });

    var ScheduleView = Backbone.View.extend({
        tagName: 'ol',
        el: '#schedule',

        events: {
            'change': 'render'
        },

        initialize: function() {
            this.model.bind('reset', this.render, this);
        },

        render: function(eventName) {
            this.$el.html('');
            _.each(this.model.models, function (event) {
                this.$el.append(new EventView({model: event}).render().el);
            }, this);
            return this;
        }
    });

    return {
        Schedule:  Schedule,
        ScheduleView: ScheduleView
    };

});
