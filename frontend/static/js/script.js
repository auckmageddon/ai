require([
    'jquery',
    'backbone-tastypie',
    'static/js/news',
    'static/js/servers',
    'static/js/tournaments',
    'static/js/schedule'
], function($, Backbone, News, Servers, Tournaments, Schedule) {
    'use strict';

    var $content = null,
        canLog   = typeof(console) !== 'undefined';

    // I'm a happy handy helper!
    function log(arg) {
        if (canLog) {
            console.log(arg);
        }
    }

    var AppRouter = Backbone.Router.extend({
        newsView:        null,
        serversView:     null,
        tournamentsView: null,
        scheduleView:    null,


        routes: {
            'news':        'displayNews',
            'servers':     'displayServers',
            'tournaments': 'displayTournaments',
            'schedule':    'displaySchedule'
        },

		// the following are all dummies and incomplete...
		// I'm trying to follow https://github.com/ccoenraets/backbone-directory/blob/master/web/js/main.js
        displayNews: function() {
            this.changeView('newsView', News.NewsView);
		},

        displayServers: function() {
            this.changeView('serversView', Servers.ServerListView);
		},

        displayTournaments: function() {
            this.changeView('tournamentsView', Tournaments.TournamentListView);
		},

        displaySchedule: function() {
            this.changeView('scheduleView', Schedule.ScheduleView);
		},

        changeView: function(cachedReference, ViewLoader, model) {
            // this is kind of nasty, but whatever.
            log(this[cachedReference]);
            if (typeof(this[cachedReference]) === 'undefined' || this[cachedReference] === null) {
                this[cachedReference] = new ViewLoader();
            }

            $content.html(this[cachedReference].render().el);
        }
    });

    $(document).ready(function() {
        window.log = log;
        $content = $('#content');
        new AppRouter();
        Backbone.history.start();
    });

});
