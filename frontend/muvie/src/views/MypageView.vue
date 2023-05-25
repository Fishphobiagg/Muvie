<template>
  <div>
    <MyProfile />
    <div class="tab">
      <ul class="tab-box">
        <li
          class="tab-li"
          ref="tabFollowing"
          :class="{ active: tab === 0 }"
          @click="clickButton(0)"
        >
          팔로잉
        </li>
        <li
          class="tab-li"
          ref="tabFollowers"
          :class="{ active: tab === 1 }"
          @click="clickButton(1)"
        >
          팔로워
        </li>
        <li
          class="tab-li"
          ref="tabLikes"
          :class="{ active: tab === 2 }"
          @click="clickButton(2)"
        >
          좋아요
        </li>
        <li
          class="tab-li"
          ref="tabPlayList"
          :class="{ active: tab === 3 }"
          @click="clickButton(3)"
        >
          재생목록
        </li>
        <div ref="line" class="line"></div>
      </ul>
      <div class="tab-container">
        <TabContainer :tab="tab" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import MyProfile from "../organisms/MyProfile.vue";
import TabContainer from "../organisms/TabContainer.vue";

export default {
  name: "MypageView",
  data() {
    return {
      tab: 0,
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
  methods: {
    clickButton(idx) {
      this.tab = idx;
      const lineElement = this.$refs.line;
      const selectedTab = this.$refs[`tab${this.tabToLabel(idx)}`];
      lineElement.style.width = `${selectedTab.offsetWidth}px`;
      lineElement.style.left = `${selectedTab.offsetLeft}px`;
    },
    tabToLabel(tab) {
      if (tab === 0) {
        return "Following";
      }
      if (tab === 1) {
        return "Followers";
      }
      if (tab === 2) {
        return "Likes";
      }
      if (tab === 3) {
        return "PlayList";
      }
      return "";
    },
  },
};
</script>

<style>
.tab {
  /* position: fixed; */
  position: relative;
  width: 100%;
  /* top: 300px; */
  /* bottom: 700px; */
  /* right: 200px; */
  overflow: hidden;
  /* background: #fff; */
  line-height: 1.5;
  font-weight: 300;
  color: #888;
  /* display: flex; */
  /* justify-content: flex-end; */
}

.tab-box {
  width: 400px;
  margin: 0px;
  display: flex;
  padding-left: 1000px;
  justify-content: space-around;
  align-items: center;
  /* border-bottom: 2px solid rgba(229, 229, 229); */
}

.tab-box li {
  width: 110px;
  list-style: none;
  font-size: 18px;
  font-weight: 600;
  color: #919191;
  background: none;
  background-color: white;
  border: none;
  padding: 15px;
  cursor: pointer;
}

.tab-box li.active {
  color: #7360ff;
}

.line {
  position: absolute;
  top: 0;
  /* left: 700; */
  width: 100px;
  height: 5px;
  background-color: #7350ff;
  border-radius: 10px;
  transition: all 0.3s ease-in-out;
  left: 1000px;
}

.tab-container {
  position: relative;
  width: 100%;
  height: 100%;
  background-color: white;
  padding-top: 10px;
}
</style>
