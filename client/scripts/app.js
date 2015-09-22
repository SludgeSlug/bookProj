var app = angular.module('app', ['ngRoute']);

// configure our routes
app.config(function($routeProvider) {
    $routeProvider

        .when('/', {
            templateUrl : 'views/enterWords.html',
            controller  : 'EnterWordsController',
            controllerAs : 'enterWordsCtrl',
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