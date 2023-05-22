<template>
  <div class="navbar">
    <MuvieLogo />
    <input
      class="input-atoms"
      v-model="inputData"
      @keydown.enter="handleSearch"
    />
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
import MuvieLogo from "../atoms/MuvieLogo.vue";

export default {
  name: "NavBar",
  data() {
    return {
      inputData: "",
    };
  },
  components: {
    MuvieLogo,
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
    handleSearch() {
      if (this.inputData.trim() !== "") {
        this.$router.push({
          name: "SearchView",
          params: { query: this.inputData },
        });
        this.inputData = "";
      }
    },
    handleModal() {
      console.log("프사 클릭");
      this.$emit("open-modal");
    },
  },
};
</script>

<style>
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.input-atoms {
  margin: 10px;
  padding: 5px;
  background-color: transparent;
  border-bottom: 1px solid;
  outline: none;
}
.my-account {
  display: flex;
  align-items: center;
  justify-content: center;
}
.my-profile-photo {
  width: 62px;
  height: 62px;
  margin-left: 20px;
  z-index: 400;
}
</style>
