(function () {
    'use strict';
    
    angular
        .module('app')
        .factory('WordService', WordService);
        
    WordService.$inject = [];
    
    function WordService() {
        
        var wordSvc = this;
        
        wordSvc.words = [{"replace" : "", "with" : ""}];
        
        wordSvc.mostUsedWords = function(offset, limit) {
            return [{word:'word1', occurences: 42}, 
            {word:'word2', occurences: 33}, 
            {word:'word3', occurences: 32}, 
            {word:'word4', occurences: 23}, 
            {word:'word5', occurences: 16}];
        }
        
        return wordSvc;
    };
    
})();