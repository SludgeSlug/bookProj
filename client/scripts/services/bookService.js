(function () {
    'use strict';
    
    angular
        .module('app')
        .factory('BookService', BookService);
        
    BookService.$inject = ['$http', '$q'];
    
    var apiUrl = '/api/';
    
    function BookService(http, $q) {
        
        var bookSvc = this;
        
        bookSvc.bookId = 1;
        
        bookSvc.getBooks = function() {
            var def = $q.defer();
            
            http.get(apiUrl + 'books').then(function(response) {
                def.resolve(response.data);
            });
            
            return def.promise;
        }
        
        bookSvc.getBookTitle = function() {
            var def = $q.defer();
            
            http.get(apiUrl + 'bookTitle', {
                params: {
                    bookId: bookSvc.bookId
                }
            }).then(function(response) {
                def.resolve(response.data);
            });
            
            return def.promise;
        }

        return bookSvc;
    };
    
})();