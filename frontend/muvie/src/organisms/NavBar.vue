<template>
  <div class="navbar">
    <MuvieLogo />
    <div class="search-bar">
      <input
        class="input-atoms"
        v-model="inputData"
        @keydown.enter="handleSearch"
        placeholder="검색어를 입력하세요..."
      />
      <button class="search-button" @click="handleSearch">
        <i class="fas fa-search"></i>
      </button>
    </div>
    <div class="my-account">
      <p class="my-nickname">{{ nickname }}</p>
      <img
        class="my-profile-photo"
        :src="`http://127.0.0.1:8000${profile_picture}`"
        alt="내 계정"
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
      userId: (state) => state.loginStore.userId,
      nickname: (state) => state.loginStore.userInfo.nickname,
      profile_picture: (state) => state.loginStore.userInfo.profile_picture,
    }),
  },
  methods: {
    handleSearch() {
      if (this.inputData.trim() !== "") {
        this.$router.push({
          name: "SearchView",
          params: { keyword: this.inputData },
        });
        this.inputData = "";
      }
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
  border-radius: 20px; /* Make the input field round */
  border: 1px solid #ccc;
  outline: none;
}
.search-bar {
  display: flex;
  align-items: center;
  position: relative;
}
.search-button {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  background-color: transparent;
  border: none;
  outline: none;
  cursor: pointer;
  font-size: 16px;
  color: #888;
}
.search-button i {
  width: 16px;
  height: 16px;
}
.my-account {
  display: flex;
  align-items: center;
  justify-content: center;
}
.my-account img {
  width: 62px;
  height: 62px;
  margin-left: 20px;
}
.my-nickname {
  /* margin - */
}
</style>