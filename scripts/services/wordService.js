(function () {
    'use strict';
    
    angular
        .module('app')
        .factory('WordService', WordService);
        
    WordService.$inject = [];
    
    function WordService() {
        
        var wordSvc = this;
        
        wordSvc.words = [{"replace" : "", "with" : ""}];
        
        return wordSvc;
    };
    
})();