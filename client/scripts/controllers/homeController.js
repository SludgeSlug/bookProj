(function () {
    'use strict';
    
    angular
        .module('app')
        .controller('HomeController', HomeController);
        
    HomeController.$inject = ['$scope', '$location', 'WordService'];
    
    function HomeController(scope, location, wordService) {
        
        var homeCtrl = this;
        
        var mostUsedOffset = 0;
        var mostUsedLimit = 5;
        
        scope.words = wordService.words;
        
        getMostUsedWords();
        
        function getMostUsedWords() {
            wordService.mostUsedWords(mostUsedOffset, mostUsedLimit)
                .then(function(response) {
                    scope.mostUsedWords = response;    
                });
        }
        
        homeCtrl.addNewWord = function() {
            scope.words.push(
                {"replace" : "", "with" : ""}
                );
        };
        
        homeCtrl.deleteRow = function(index) {
            scope.words.splice(index, 1);
        };
        
        homeCtrl.showDelete = function() {
            return scope.words.length > 1;
        };
        
        homeCtrl.generate = function() {
            location.path('/result');    
        };
        
        homeCtrl.previous = function() {
            mostUsedOffset = mostUsedOffset - 5;
            getMostUsedWords();
        }
        
        homeCtrl.next = function() {
            mostUsedOffset = mostUsedOffset + 5;
            getMostUsedWords();
        }
        
        homeCtrl.showPrevious = function() {
            return mostUsedOffset > 0;
        }
        
        homeCtrl.showNext = function() {
            return true;
        }
        
    };
    
})();