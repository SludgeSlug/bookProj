(function () {
    'use strict';
    
    angular
        .module('app')
        .controller('HomeController', HomeController);
        
    HomeController.$inject = ['$scope', '$location', 'WordService'];
    
    function HomeController(scope, location, wordService) {
        
        var homeCtrl = this;
        
        scope.words = wordService.words;
        
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
        
    };
    
})();