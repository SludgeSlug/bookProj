(function () {
    'use strict';
    
    angular
        .module('app')
        .controller('HomeController', HomeController);
        
    HomeController.$inject = ['$location', 'books', '$scope', 'BookService'];
    
    var apiUrl = '/api/';
    
    function HomeController(location, books, scope, bookService) {
        
        var homeCtrl = this;
        
        homeCtrl.books = books;
        scope.selectedBook = 0;
        
        homeCtrl.select = function() {
            bookService.bookId = scope.selectedBook;
            location.path('/enterwords'); 
        }
        
    };
    
})();