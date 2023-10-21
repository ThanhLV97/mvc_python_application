import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import 'typeface-bebas-neue';
import { createApp } from 'vue';
import App from './App.vue';
import './assets/reset.css';
import './assets/variables.css';
import router from './router';
import { store } from './store/index';

const app = createApp(App);
app.use(router);
app.use(store)
app.mount('#app');
