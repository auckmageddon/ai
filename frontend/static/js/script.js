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

    function refresh(appRouter) {
        var views = [appRouter.newsView, appRouter.serversView, appRouter.tournamentsView, appRouter.scheduleView];

        for (var viewIdx in views) {
            var view = views[viewIdx];
            if (view != null) {
                view.model.fetch();
            }
        }

        setTimeout(function() {
            refresh(appRouter);
        }, 30000);
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
            'schedule':    'displaySchedule',
            '*path':       'displayNews' 
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
            if (typeof(this[cachedReference]) === 'undefined' || this[cachedReference] === null) {
                this[cachedReference] = new ViewLoader();
                this[cachedReference].render();
            }

            this[cachedReference].model.fetch();
            $content.children().removeClass('show').addClass('hidden');
            this[cachedReference].$el.removeClass('hidden').addClass('show');
        }
    });

    $(document).ready(function() {
        window.log = log;
        $content = $('#content');
        var appRouter = new AppRouter();
        Backbone.history.start();
        refresh(appRouter);

        Cufon.set('fontFamily', 'earth');
        Cufon.replace('.navbar .brand');
    });

});
