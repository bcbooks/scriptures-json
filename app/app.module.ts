import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import {AppComponent} from './app.component';
import {NavbarComponent} from './components/navbar/navbar.component';
import {JumbotronComponent} from './components/jumbotron/jumbotron.component';
import {SearchComponent} from './components/pages/search.component';
import {HomeComponent} from './components/pages/home.component';
import {ContactComponent} from './components/pages/contact.component';

import {routing} from './app.routing';

@NgModule({
  imports:      [ BrowserModule, routing ],
  declarations: [ AppComponent,
  				  NavbarComponent,
  				  JumbotronComponent,
  				  SearchComponent,
  				  HomeComponent,
                  ContactComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
