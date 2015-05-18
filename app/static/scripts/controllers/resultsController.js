(function () {
    'use strict';
    
    angular
        .module('app')
        .controller('ResultsController', ResultsController);
        
    ResultsController.$inject = ['$scope', 'WordService', '$http', '$q'];
    
    function ResultsController(scope, wordService, http, q) {
        
        var resultsCtrl = this;
        
        scope.words = wordService.words;
        
        resultsCtrl.download = function() {
            var defer = q.defer();
            
            var request = http({
                method: 'get',
                url: 'https://spinbook-sludgeslug.c9.io/api/book/',
                data: wordService.words
            });
            
            request.success(function(data, status, headers, config) {
                alert('success');
    			defer.resolve(data);
    		});
    		request.error(function(data, status, headers, config) {
    			scope.error = data;
    		});
    		
    		return defer.promise;
        }
    };
    
})();