import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import loginStore from "./modules/loginStore";
import signupStore from "./modules/signupStore";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    loginstore: loginStore,
    signupstore: signupStore,
  },
  plugins: [
    createPersistedState({
      paths: ["loginstore", "signupstore"],
    }),
  ],
});

// export default createStore({
//   state: {},
//   getters: {},
//   mutations: {},
//   actions: {},
//   modules: {},
//   plugins: [
//     createPersistedState({
//       paths: ["loginStore"],
//     }),
//   ],
// });
