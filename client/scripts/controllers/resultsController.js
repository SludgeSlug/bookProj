(function () {
    'use strict';
    
    angular
        .module('app')
        .controller('ResultsController', ResultsController);
        
    ResultsController.$inject = ['$scope', 'WordService', '$http', '$q'];
    
    var apiUrl = '/api/';
    
    function ResultsController(scope, wordService, http, q) {
        var resultsCtrl = this;
        
        var quoteNumber = 0;
        
        scope.words = wordService.words;
        scope.quote = getQuote();
        
        
        resultsCtrl.getQuote = getQuote;
        
        resultsCtrl.showPrevious = function() {
            return quoteNumber > 0;
        }

        resultsCtrl.nextQuote = function() {
            quoteNumber++;
            scope.quote = getQuote();
        }
        
        resultsCtrl.previousQuote = function() {
            quoteNumber--;
            scope.quote = getQuote();
        }
        
        function getQuote() {
            
            http.get(apiUrl + 'quote', {
                params: {
                    index: quoteNumber,
                    replacementWords: JSON.stringify(wordService.words)
                }
            }).then(function(response) {
                scope.quote = response.data;    
            });
        }
    };
    
})();