import { Component } from '@angular/core';

@Component({
	moduleId:module.id,
  	selector: 'home',
  	templateUrl: 'home.component.html'
})
export class HomeComponent { 
    private books;
    //var config = require('./../../../scriptures/reference/book-of-mormon.json');
    private test;

    constructor(){
        this.books=['New Testament', 'Old Testament', 'Book of Mormon', 'Doctrine and Covenants', 'Pearl of Great Price'];
        this.booksJSON=[];
        
        $http.get('./../../../scriptures/reference/book-of-mormon.json').success(function(data) {
           this.test = data;
        });


        /*$.getJSON('/scriptures/reference/book-of-mormon.json', function(data) { 
            test=data;
        }).done(function(){
            console.log(test.length());
        }).fail(function() {
            console.log('getJSON request failed!');
        }); */
        console.log(this.test.length());
        //this.jbtText="blah blah blah blah :p";
        //this.jbtBtnText="Contact";
        //this.jbtBtnUrl="/contact";
    }
}
