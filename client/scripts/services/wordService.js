(function () {
    'use strict';
    
    angular
        .module('app')
        .factory('WordService', WordService);
        
    WordService.$inject = ['$http', '$q'];
    
    var apiUrl = '/api/';
    
    function WordService(http, $q) {
        
        var wordSvc = this;
        
        wordSvc.words = [{"replace" : "", "with" : ""}];
        
        wordSvc.mostUsedWords = function(offset, limit) {
            var def = $q.defer();
            
            http.get(apiUrl + 'mostused', {
                params: {
                    offset: offset,
                    limit: limit
                }
            }).then(function(response) {
                def.resolve(response.data);
            });
            
            return def.promise;
        }
        
        wordSvc.numberOfWords = function() {
            var def = $q.defer();
            
            http.get(apiUrl + 'numberOfWords').then(function(response) {
                def.resolve(response.data);
            });
            
            return def.promise;
        }
        
        return wordSvc;
    };
    
})();