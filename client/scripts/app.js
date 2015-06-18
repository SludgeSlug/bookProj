var app = angular.module('app', ['ngRoute']);

// configure our routes
app.config(function($routeProvider) {
    $routeProvider

        .when('/', {
            templateUrl : 'views/home.html',
            controller  : 'HomeController',
            controllerAs : 'homeCtrl'
        })
        
        .when('/result', {
            templateUrl : 'views/result.html',
            controller  : 'ResultsController',
            controllerAs : 'resultsCtrl'
        })
});