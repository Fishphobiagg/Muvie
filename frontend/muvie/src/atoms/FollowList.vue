<template>
  <div class="profile-item">
    <div class="user-detail">
      <div class="profile-photo"></div>
      <span class="user-name">하니</span>
    </div>
    <button class="follow-button">{{ buttonMsg }}</button>
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
};
</script>

<style>
.profile-item {
  width: 1000px;
  height: 80px;
  margin: 0 auto;
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
  width: 77px;
  height: 77px;
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
  display: inline-block; /* 추가 */
  vertical-align: middle; /* 추가 */
}

.follow-button {
  height: 40px;
  width: 80px;
  font-size: 15px;
  border: none;
  border-radius: 9px;
  cursor: pointer;
}
</style>
