(function () {
    'use strict';
    
    angular
        .module('app')
        .controller('ResultsController', ResultsController);
        
    ResultsController.$inject = ['$scope', 'WordService'];
    
    function ResultsController(scope, wordService) {
        
        var resultsCtrl = this;
        
        scope.words = wordService.words;
    };
    
})();