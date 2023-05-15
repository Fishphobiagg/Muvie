<template>
  <div class="profile-item">
    <div>
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
  display: flex;
}

.profile-photo {
  width: 80px;
  height: 80px;
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
}

.follow-button {
}
</style>
