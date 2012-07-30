require([
    'jquery',
    'backbone',
    'js/news', 
    'js/servers', 
    'js/tournaments', 
    'js/schedule'
], function($, Backbone, News, Servers, Tournaments, Schedule) {

    var $content = $("#content");

    var AppRouter = Backbone.Router.extend({
        routes: {
            'news':        'displayNews',
            'servers':     'displayServers',
            'tournaments': 'displayTournaments',
            'schedule':    'displaySchedule'
        },

		// the following are all dummies and incomplete...
		// I'm trying to follow https://github.com/ccoenraets/backbone-directory/blob/master/web/js/main.js
        displayNews: function() {
            var entryOne = new News.Entry({title: "test"}),
                entryTwo = new News.Entry({title: "test2"}),
                news     = new News.News([entryOne, entryTwo]);

            console.log(new News.NewsView({model: news}).render());

			$('#content').html(new News.NewsView({model: news}).render().el);

            console.log('rendered');
		},
        displayServers: function() {
			$content.html(new ServersView().render());
		},
        displayTournaments: function() {
			$content.html(new TournamentsView().render());
		},
        displaySchedule: function() {
			$content.html(new ScheduleView().render());
		}
    });

    window.appRouter = new AppRouter();

    Backbone.history.start();

    $('#loadNews').on('click', function() {
        appRouter.navigate('news', {'trigger': true});
    });

});
