define(['backbone-tastypie', 'jquery', 'underscore'], function(Backbone, $, _) {

    var Event = Backbone.Model.extend({

    });

    var Schedule = Backbone.Collection.extend({
        model: Event,
        url: '/api/v1/event/?format=json',

        next_event: function() {
            log(this.models);
            var now = Date.now();
            var upcoming = _.filter(this.models, function(anEvent) {
                return now < anEvent['happening_at'];
            });
            log(upcoming);

            return upcoming[0];
        }
    });

    var EventView = Backbone.View.extend({
        tagName:  'li',
        template: _.template($('#schedule_event_template').html()),

        render: function(eventName) {
            this.$el.html(this.template(this.model.toJSON()));
            return this;
        }
    });

    var EventScreenView = Backbone.View.extend({
        tagName: 'div',
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
            this.model = new Schedule();
            this.model.bind('reset', this.render, this);
            this.model.fetch();
        },

        render: function(eventName) {
            this.$el.html('');
            _.each(this.model.models, function (event) {
                this.$el.append(new EventView({model: event}).render().el);
            }, this);
            return this;
        }
    });

    var ScheduleScreenView = Backbone.View.extend({
        el: '#next_event',

        initialize: function() {
            this.model = new Schedule();
            this.model.bind('reset', this.render, this);
            this.model.fetch();
        },

        render: function(eventName) {
            this.$el.html(''); // should make this transition it out first
            var next_event = this.model.next_event();
            if (typeof(next_event) !== 'undefined' && next_event != null)
                this.$el.html(new EventScreenView({model: next_event}).render().el);
            else
                this.$el.html('<h2>NEK MINNU--oh shit it\'s over???</h2>');
        }
    });

    return {
        Schedule:  Schedule,
        ScheduleView: ScheduleView,
        ScheduleScreenView: ScheduleScreenView
    };

});
