import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import 'typeface-bebas-neue';
import { createApp } from 'vue';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import 'vuetify/styles';
import App from './App.vue';
import './assets/reset.css';
import './assets/variables.css';
import router from './router';
import { store } from './store/index';

const vuetify = createVuetify({
    components,
    directives,
})

const app = createApp(App);
app.use(router);
app.use(store)
app.use(vuetify)
app.mount('#app');
