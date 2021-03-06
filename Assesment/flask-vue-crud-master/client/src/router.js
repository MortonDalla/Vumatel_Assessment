import Vue from 'vue';
import Router from 'vue-router';
import installations from './components/installations.vue';
import Ping from './components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'installations',
      component: installations,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
