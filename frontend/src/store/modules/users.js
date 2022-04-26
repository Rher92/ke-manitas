import axios from 'axios';

const state = {
  user: null,
};

const getters = {
  isAuthenticated: state => !!state.user,
  stateUser: state => state.user,
};

const headers = {'Access-Control-Allow-Origin': '*'}

const actions = {
  async register({dispatch}, form) {
    await axios.post('register', form, headers);
    let UserForm = new FormData();
    UserForm.append('username', form.username);
    UserForm.append('password', form.password);
    await dispatch('logIn', UserForm);
  },

  async logIn({commit}, user) {
    let userLogin = await axios.post('api/users/login/', user, headers);
    await commit('setUserToken', userLogin.data);
  },

  async deleteUser(_, id) {
    await axios.delete(`user/${id}`);
  },

  async logOut({commit}) {
    let user = null;
    commit('logout', user);
  },

  async VehicleWorkdayToUser({commit}, vehicle_workday) {
    await commit('setVehicleWorkdayToUser', vehicle_workday);
  },
};

const mutations = {
  setUserToken(state, user) {
    state.user = user;
  },
  logout(state, user){
    state.user = user;
  },
  setVehicleWorkdayToUser(state, vehicle_workday){
    state.user.vehicle_workday = vehicle_workday.vehicle_workday;
},
};

export default {
  state,
  getters,
  actions,
  mutations
};
