import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000/accounts/signup";

const signupStore = {
  state: {},
  mutations: {},
  actions: {
    signup(_, signupObj) {
      console.log(signupObj);
      const config = {
        headers: {
          "Content-Type": "multipart/form-data", // 파일 업로드를 위한 헤더 설정
        },
      };

      axios
        .post(BASE_URL, signupObj, config)
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
