<template>
  <div class="navbar">
    <MuvieLogo />
    <input class="input-atoms" v-model="inputData" />
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
.my-account img {
  width: 62px;
  height: 62px;
  margin-left: 20px;
}
.my-nickname {
  /* margin - */
}
</style>
