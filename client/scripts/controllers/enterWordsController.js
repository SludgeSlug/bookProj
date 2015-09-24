(function () {
    'use strict';
    
    angular
        .module('app')
        .controller('EnterWordsController', EnterWordsController);
        
    EnterWordsController.$inject = ['$scope', '$location', 'WordService', 
        'wordCount', 'BookService', 'bookTitle'];
    
    function EnterWordsController(scope, location, wordService, 
        wordCount, bookService, bookTitle) {
        
        var enterWordsCtrl = this;
        
        var mostUsedOffset = 0;
        var mostUsedLimit = 5;
        
        scope.words = wordService.words;
        scope.bookTitle = bookTitle;
        scope.showMostUsedWords = false;
        
        var numberOfWords = parseInt(wordCount);
        
        getMostUsedWords();
        
        function getMostUsedWords() {
            wordService.mostUsedWords(mostUsedOffset, mostUsedLimit, bookService.bookId)
                .then(function(response) {
                    scope.mostUsedWords = response;    
                });
        };
        
        enterWordsCtrl.toggleMuWords = function() {
            scope.showMostUsedWords = !scope.showMostUsedWords;
        }
        
        enterWordsCtrl.addNewWord = function() {
            scope.words.push(
                {"replace" : "", "with" : ""}
                );
        };
        
        enterWordsCtrl.deleteRow = function(index) {
            scope.words.splice(index, 1);
        };
        
        enterWordsCtrl.showDelete = function() {
            return scope.words.length > 1;
        };
        
        enterWordsCtrl.generate = function() {
            location.path('/result');    
        };
        
        enterWordsCtrl.previous = function() {
            mostUsedOffset = mostUsedOffset - 5;
            getMostUsedWords();
        };
        
        enterWordsCtrl.next = function() {
            mostUsedOffset = mostUsedOffset + 5;
            getMostUsedWords();
        };
        
        enterWordsCtrl.addMostUsedWord = function(word) {
            if(scope.words.length === 1 &&
                scope.words[0].replace === "") {
                
                scope.words = [{"replace" : word, "with": ""}];     
            } else {
                scope.words.push(
                {"replace" : word, "with" : ""});
            }
        };
        
        enterWordsCtrl.wordAdded = function(word) {
            for(var i in scope.words) {
                if(scope.words[i].replace === word) {
                    return false;
                }
            }
            return true;
        };
        
        enterWordsCtrl.showPrevious = function() {
            return mostUsedOffset > 0;
        };
        
        enterWordsCtrl.showNext = function() {
            return mostUsedOffset < numberOfWords;
        };
        
    };
    
})();