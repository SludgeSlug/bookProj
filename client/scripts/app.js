var app = angular.module('app', ['ngRoute']);

// configure our routes
app.config(function($routeProvider) {
    $routeProvider
    
        .when('/', {
            templateUrl: 'views/home.html',
            controller : 'HomeController',
            controllerAs: 'homeCtrl',
            resolve: {
                books: ['BookService', function(bookService) {
                    return bookService.getBooks();
                }]
            }
        })

        .when('/enterwords', {
            templateUrl : 'views/enterWords.html',
            controller  : 'EnterWordsController',
            controllerAs : 'enterWordsCtrl',
            resolve: {
                wordCount: ['WordService', 'BookService', function(wordService, bookService) {
                    return wordService.numberOfWords(bookService.bookId);                    
                }]
            }
        })
        
        .when('/result', {
            templateUrl : 'views/result.html',
            controller  : 'ResultsController',
            controllerAs : 'resultsCtrl'
        })
});