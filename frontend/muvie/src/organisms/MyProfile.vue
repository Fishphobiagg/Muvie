<template>
  <div>
    <div class="my-profile">
      <img
        class="my-profile-photo"
        :src="`http://127.0.0.1:8000${profile_picture}`"
        alt=""
      />
      <div class="my-profile-detail">
        <p>{{ nickname }}</p>
        <button>취향 설정</button>
        <button>프로필 편집</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "MyProfile",
  computed: mapState({
    userId: (state) => state.mypageStore.userId,
    nickname: (state) => state.mypageStore.nickname,
    profile_picture: (state) => state.mypageStore.profile_picture,
  }),
};
</script>

<style>
.my-profile {
  display: flex;
  align-items: center;
  padding-left: 80px;
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
}
</style>
