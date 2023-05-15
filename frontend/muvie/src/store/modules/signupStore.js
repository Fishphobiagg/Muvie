import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/accounts/signup";

const signupStore = {
  state: {},
  mutations: {},
  actions: {
    signup(dispatch, signupObj) {
      console.log(signupObj);
      axios
        .post(BASE_URL, signupObj)
        .then((res) => {
          console.log(res.data);
          console.log("회원가입 성공!");
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};

export default signupStore;
