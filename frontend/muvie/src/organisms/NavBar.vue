<template>
  <div class="navbar">
    <img src="../assets/logo.png" alt="로고" class="logo" />
    <div class="search-bar">
      <div class="search-input">
        <button class="search-button" @click="handleSearch">
          <i class="fas fa-search"></i>
        </button>
        <input
          class="input-atoms"
          v-model="inputData"
          @keydown.enter="handleSearch"
          @input="changeInput"
          placeholder="음악과 사용자를 검색해보세요"
        />
      </div>
      <div class="search-bar-line"></div>
    </div>
    <div class="my-account">
      <p class="my-nickname">{{ nickname || "익명의 유저" }}</p>
      <img
        class="my-profile-photo"
        :src="`http://127.0.0.1:8000${profile_picture || '/users/default.gif'}`"
        alt="내 계정"
        @click="handleModal"
      />
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "NavBar",
  data() {
    return {
      inputData: "",
    };
  },
  computed: {
    ...mapState({
      userId: (state) =>
        localStorage.getItem("vuex") ? state.loginStore.userId : -1,
      nickname: (state) =>
        localStorage.getItem("vuex")
          ? state.loginStore.userInfo.nickname
          : "익명의 유저",
      profile_picture: (state) =>
        localStorage.getItem("vuex")
          ? state.loginStore.userInfo.profile_picture
          : "/users/default.gif",
    }),
  },
  methods: {
    changeInput(e) {
      this.inputData = e.target.value;
      console.log(this.inputData);
    },
    handleSearch() {
      if (this.inputData.trim() !== "") {
        this.$router.push({
          name: "SearchResultView",
          params: { keyword: this.inputData },
        });
        this.inputData = "";
      }
    },
    handleModal() {
      console.log("프사 클릭");
      this.$emit("open-modal");
    },
    navigateToMain() {
      console.log("로고 클릭");
      this.$router.push({ name: "MainView" });
    },
  },
};
</script>

<style>
.logo {
  width: 120px;
  height: 40px;
  margin-left: 30px;
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.search-bar {
  position: relative;
}

.search-input {
  display: flex;
  align-items: center;
}

.input-atoms {
  margin: 10px 0 10px 10px;
  padding: 5px;
  background-color: transparent;
  border: none;
  outline: none;
}

.input-atoms::placeholder {
  color: gray;
}

.search-button {
  background-color: transparent;
  border: none;
  outline: none;
  cursor: pointer;
  font-size: 16px;
  color: #888;
  margin-right: 10px;
  margin-left: 10px;
}

.search-button i {
  width: 16px;
  height: 16px;
}

.search-bar-line {
  height: 1px;
  background-color: #ccc;
  margin-top: -10px;
}

.my-account {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 10px;
}

.my-account img {
  width: 62px;
  height: 62px;
  margin-left: 20px;
  margin-top: 15px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
}

.my-profile-photo {
  width: 62px;
  height: 62px;
  margin-left: 20px;
  z-index: 300;
}
</style>
