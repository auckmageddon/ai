require([
    'jquery',
    'backbone-tastypie',
    'static/js/news',
    'static/js/schedule'
], function($, Backbone, News, Schedule) {
    'use strict';

    var canLog   = typeof(console) !== 'undefined';

    // I'm a happy handy helper!
    function log(arg) {
        if (canLog) {
            console.log(arg);
        }
    }

    var Screen = function() {
        var newsView     = null,
            scheduleView = null;

		function refresh() {
            log('called');
            newsView.model.fetch();
            scheduleView.model.fetch();
            setTimeout(refresh, 10000);
		};

        function initialize() {
            newsView = new News.NewsScreenView();
            scheduleView = new Schedule.ScheduleScreenView();
            setTimeout(refresh, 10000);
        }

        return {
            initialize: initialize
        };
    };

    $(document).ready(function() {
        window.log = log;
        new Screen().initialize();
    });

});
