import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import loginStore from "./modules/loginStore";
import signupStore from "./modules/signupStore";
import mypageStore from "./modules/mypageStore";
import mainStore from "./modules/mainStore";
import searchStore from "./modules/searchStore";
import preferenceStore from "./modules/preferenceStore";
import playerStore from "./modules/playerStore";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    loginStore,
    signupStore,
    mypageStore,
    mainStore,
    searchStore,
    preferenceStore,
    playerStore,
  },
  plugins: [createPersistedState({ paths: ["loginStore", "playerStore"] })],
});
