import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import loginStore from "./modules/loginStore";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    loginstore: loginStore,
  },
  plugins: [
    createPersistedState({
      paths: ["loginstore"],
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
