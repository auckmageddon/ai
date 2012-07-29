require([
    'backbone',
    'news', 
    'servers', 
    'tournaments', 
    'schedule'
],
[
    Backbone,
    News,
    Servers,
    Tournaments,
    Schedule
], function() {

    var currentlyDisplayed = null;

    var AppRouter = Backbone.Router.extend({
        routes: {
            'news': 'displayNews',
            'servers': 'displayServers',
            'tournaments': 'displayTournaments',
            'schedule': 'displaySchedule'
        },

        displayNews: function() {},
        displayServers: function() {},
        displayTournaments: function() {},
        displaySchedule: function() {}
    });

    var appRouter = new AppRouter;

    Backbone.history.start();

});