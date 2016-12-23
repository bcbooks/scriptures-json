"use strict";
var router_1 = require("@angular/router");
var home_component_1 = require("./components/pages/home.component");
var search_component_1 = require("./components/pages/search.component");
var contact_component_1 = require("./components/pages/contact.component");
var appRoutes = [
    {
        path: '',
        component: home_component_1.HomeComponent
    },
    {
        path: 'search',
        component: search_component_1.SearchComponent
    },
    {
        path: 'contact',
        component: contact_component_1.ContactComponent
    }
];
exports.routing = router_1.RouterModule.forRoot(appRoutes);
//# sourceMappingURL=app.routing.js.map