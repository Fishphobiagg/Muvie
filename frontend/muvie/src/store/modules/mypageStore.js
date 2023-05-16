import axios from "axios";

const mypageStore = {
  state: {
    followers: null,
    following: null,
  },
  mutations: {},
  // computed: mapState({
  //   userId: (state) => state.loginStore.userId,
  // }),
  actions: {
    getProfile(_, id) {
      const BASE_URL = `http://127.0.0.1:8000/accounts/${id}/profile`;
      console.log(axios.defaults);

      axios
        .get(BASE_URL)
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => console.log(err));
      console.log(BASE_URL);
    },
  },
  mounted() {
    console.log(this.userId);
    this.getProfile();
  },
};

export default mypageStore;
