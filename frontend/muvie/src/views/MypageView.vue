<template>
  <div>
    <MyProfile />
    <div class="tab">
      <ul class="tab-bar">
        <li @click="tab = 0">팔로잉</li>
        <li @click="tab = 1">팔로워</li>
        <li @click="tab = 2">좋아요</li>
      </ul>
    </div>

    <div class="tab-container">
      <TabContainer :tab="tab" />
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import MyProfile from "../organisms/MyProfile";
import TabContainer from "../organisms/TabContainer";

export default {
  name: "MypageView",
  data() {
    return {
      tab: 1,
      profilePhoto: null,
    };
  },
  components: {
    TabContainer,
    MyProfile,
  },
  computed: mapState({
    userId: (state) => state.loginStore.userId,
    followers: (state) => state.mypageStore.followers,
    following: (state) => state.mypageStore.following,
  }),
  // created() {
  //   console.log("마이페이지뷰");
  //   if (this.userId) {
  //     this.$store.dispatch("getProfile", this.userId);
  //   }
  // },
};
</script>

<style>
.tab {
  /* width: 400px; */
  position: fixed;
  bottom: 700px;
  right: 200px;
  /* padding-top: 30px; */
  overflow: hidden;
  background: #fff;
  line-height: 1.5;
  font-weight: 300;
  color: #888;
}

.tab-bar {
  display: table;
  /* position: relative; */
  /* overflow: hidden; */
  margin: 0 auto;
  padding: 0;
}

.tab-bar li {
  list-style: none;
  font-size: 22px;
  color: black;
  /* padding: 10px; */
  margin: 0px 40px;
  padding: 25px 20px 10px 20px;
  float: left;
  line-height: 38px;
  overflow: hidden;
  /* padding: 0; */
  position: relative;
}

.tab-container {
  width: 100vh;
  height: 700px;
}
</style>
