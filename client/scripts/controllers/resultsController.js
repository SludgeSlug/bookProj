(function () {
    'use strict';
    
    angular
        .module('app')
        .controller('ResultsController', ResultsController);
        
    ResultsController.$inject = ['$scope', 'WordService', '$http'];
    
    function ResultsController(scope, wordService, http) {
        
        var resultsCtrl = this;
        
        scope.words = wordService.words;
        
        resultsCtrl.download = function() {
            
            var request = http({
                method: 'post',
                url: 'https://sludgeslug.pythonanywhere.com/api/book/',
                data: wordService.words
            });
            
            request.success(function(data, status, headers, config) {
    			
    		});
    		request.error(function(data, status, headers, config) {
    			alert( "failure message: " + JSON.stringify({data: data}));
    		});	
        }
    };
    
})();