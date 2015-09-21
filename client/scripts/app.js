var app = angular.module('app', ['ngRoute']);

// configure our routes
app.config(function($routeProvider) {
    $routeProvider

        .when('/', {
            templateUrl : 'views/home.html',
            controller  : 'HomeController',
            controllerAs : 'homeCtrl',
            resolve: {
                wordCount: ['WordService', function(wordService) {
                    return wordService.numberOfWords();                    
                }]
            }
        })
        
        .when('/result', {
            templateUrl : 'views/result.html',
            controller  : 'ResultsController',
            controllerAs : 'resultsCtrl'
        })
});