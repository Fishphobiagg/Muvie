<template>
  <div>
    <div class="my-profile">
      <div class="my-photo-detail">
        <img
          class="my-profile-photo"
          :src="`http://127.0.0.1:8000${profile_picture}`"
          alt=""
        />
        <i class="fas fa-camera fa-4x" v-show="editing"></i>
      </div>
      <div class="my-profile-detail">
        <div class="nick-name-detail">
          <input v-if="editing" v-model="newNickname" />
          <p v-else>{{ nickname }}</p>
          <i
            class="fas fa-pencil fa-lg"
            v-show="editing"
            @click="editNickname"
          ></i>
        </div>
        <button>취향 설정</button>
        <button @click="editProfile">프로필 편집</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "MyProfile",
  data() {
    return {
      editing: false,
      newNickname: "",
    };
  },
  computed: {
    ...mapState({
      userId: (state) => state.loginStore.userId,
      nickname: (state) => state.mypageStore.nickname,
      profile_picture: (state) => state.mypageStore.profile_picture,
    }),
  },
  methods: {
    editProfile() {
      console.log("프로필 편집");
      this.editing = !this.editing;
      console.log(this.editing);
    },
    editNickname() {
      const payload = {
        id: this.userId,
        name: this.newNickname,
        profile_picture: this.profile_picture,
      };
      this.$store.dispatch("editNickname", payload);
    },
  },
  // actions: {
  //   editNickname({ commit }) {
  //     console.log(this.newNickname);

  //     commit("updateNickname", this.newNickname);
  //     // 저장이 완료되면 editing 값을 다시 false로 설정합니다.
  //     // this.editing = false;
  //   },
  // },
  // mutations: {
  //   updateNickname(state, payload) {
  //     // eslint-disable-next-line no-param-reassign
  //     state.nickname = payload;
  //   },
};
</script>

<style>
.my-profile {
  display: flex;
  align-items: center;
  padding-left: 80px;
}

.my-photo-detail {
  position: relative;
}

.my-photo-detail i {
  position: absolute;
  top: 18px;
  right: 57px;
  opacity: 0.8;
}

.my-profile-photo {
  width: 100px;
  height: 100px;
  margin-right: 40px;
  background-color: transparent;
  border-radius: 75px;
  overflow: hidden;
  object-fit: cover;
}

.my-profile-detail p {
  font-size: 25px;
}

.my-profile-detail button {
  /* margin: 20px; */
  margin: 10px;
  padding: 10px 20px;
  background: white;
  /* 그림자 수정 필요 */
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
  text-decoration: none;
  border: none;
  cursor: pointer;
}

.my-profile-detail input {
  margin: 10px;
  padding: 10px 20px;
  background-color: transparent;
  border-bottom: 1px solid;
}

.nick-name-detail {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 230px;
  height: 85px;
}

.nick-name-detail i {
  margin-left: 15px;
}
</style>
