<template>
  <div class="profile-item">
    <div class="user-detail">
      <img
        class="profile-photo"
        :src="`http://127.0.0.1:8000${fwg.profile_picture}`"
        alt="프로필 사진"
      />
      <span class="user-name" @click="navigateToProfile(fwg.id)">{{
        fwg.nickname
      }}</span>
    </div>
    <button
      class="follow-button"
      @click="followAction(fwg)"
      :class="{ following: fwg.is_followed }"
    >
      {{ fwg.is_followed ? "팔로잉" : "팔로우" }}
    </button>
  </div>
</template>

<script>
export default {
  name: "FollowList",
  data() {
    return {
      buttonMsg: "팔로잉",
    };
  },
  methods: {
    navigateToProfile(userId) {
      this.$router.push({ name: "Profile", params: { userId } });
    },
    followAction(fwg) {
      if (fwg.is_followed) {
        // 이미 팔로잉 중인 경우의 동작
        this.$store.dispatch("unfollow", fwg.id);
      } else {
        // 팔로우할 경우의 동작
        this.$store.dispatch("follow", fwg.id);
      }
    },
  },
  props: {
    fwg: Object,
  },
};
</script>

<style>
.profile-item {
  width: 1000px;
  height: 80px;
  margin: 5px auto;
  padding: 10px 60px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.user-detail {
  height: 80px;
  display: flex;
  align-items: center;
}

.profile-photo {
  width: 66px;
  height: 66px;
  background-color: white;
  border-radius: 75px;
  overflow: hidden;
  object-fit: cover;
}

.user-name {
  text-decoration: none;
  border: none;
  /* background-color: transparent; */
  margin: 0 15px 0 40px;
  font-size: 25px;
  line-height: 80px;
  cursor: pointer;
  display: inline-block;
  vertical-align: middle;
}

.follow-button {
  height: 40px;
  width: 80px;
  font-size: 15px;
  border: none;
  border-radius: 9px;
  cursor: pointer;
  background-color: blue;
  color: white;
}

.following {
  background-color: lightgray !important;
  color: black !important;
}
</style>
