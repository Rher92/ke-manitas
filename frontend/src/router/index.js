import Vue from 'vue';
import VueRouter from 'vue-router';

import store from '@/store';

import Dashboard from '@/views/Dashboard';
import Home from '@/views/Home.vue';
import Login from '@/views/Login';
import Profile from '@/views/Profile';
import Register from '@/views/Register';
import LoginVehicle from '@/views/LoginVehicle';
import LogoutVehicle from '@/views/LogoutVehicle';
import ListVehicleWorkdays from '@/views/ListVehicleWorkdays';
import RetrieveVehicleWorkdays from '@/views/RetrieveVehicleWorkdays';
import ListLentsUsers from '@/views/ListLentsUsers';
import RetrieveLentUser from '@/views/RetrieveLentUser';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: "Home",
    component: Home,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/login-vehicle',
    name: 'LoginVehicle',
    component: LoginVehicle,
  },
  {
    path: '/logout-vehicle',
    name: 'LogoutVehicle',
    component: LogoutVehicle,
  },
  {
    path: '/list-vehicle-workdays',
    name: 'ListVehicleWorkdays',
    component: ListVehicleWorkdays,
  },
  {
    path: '/retrieve-vehicle-workdays/:id',
    name: 'RetrieveVehicleWorkdays',
    component: RetrieveVehicleWorkdays,
    props: true
  },
  {
    path: '/list-lents-users',
    name: 'ListLentsUsers',
    component: ListLentsUsers,
  },
  {
    path: '/retrieve-lent-users/:id',
    name: 'RetrieveLentUser',
    component: RetrieveLentUser,
    props: true
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {requiresAuth: true},
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {requiresAuth: true},
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/login');
  } else {
    next();
  }
});

export default router;
