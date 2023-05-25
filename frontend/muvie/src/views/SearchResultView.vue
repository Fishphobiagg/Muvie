<template>
  <div>
    <img src="../assets/logo.png" alt="" class="logo" @click="navigateToMain()">
    <div class="tab">
      <ul class="tab-box">
        <li
          class="tab-li"
          ref="tabAll"
          :class="{ active: tab === 0 }"
          @click="clickButton(0)"
        >
          전체
        </li>
        <li
          class="tab-li"
          ref="tabsearchedList"
          :class="{ active: tab === 1 }"
          @click="clickButton(1)"
        >
          노래
        </li>
        <li
          class="tab-li"
          ref="tabUserList"
          :class="{ active: tab === 2 }"
          @click="clickButton(2)"
        >
          유저</li>
        <div ref="line" class="line"></div>
      </ul>
      <div class="tab-container">
        <SearchTab :tab="tab" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import SearchTab from "../organisms/SearchTabContainer.vue";

export default {
  name: "SearchResultView",
  data() {
    return {
      tab: 0,
    };
  },
  components: {
    SearchTab,
  },
  computed: mapState({
    userId: (state) => state.loginStore.userId,
    searchedList: (state) => state.searchStore.searchedList,
    userList: (state) => state.searchStore.userList,
  }),
  methods: {
    navigateToMain(){
      this.$router.push({name:"MainView"})
    }
    ,
    clickButton(idx) {
      this.tab = idx;
      const lineElement = this.$refs.line;
      const selectedTab = this.$refs[`tab${this.tabToLabel(idx)}`];
      lineElement.style.width = `${selectedTab.offsetWidth}px`;
      lineElement.style.left = `${selectedTab.offsetLeft}px`;
    },
    tabToLabel(tab) {
      if (tab === 0) {
        return "All";
      }
      if (tab === 1) {
        return "searchedList";
      }
      if (tab === 2) {
        return "UserList";
      }
      return "";
    },
  },
};
</script>

<style>
.logo{
  width: 120px;
  height: 40px;
  display: flex;
  cursor: pointer;
  display: flex;
  justify-content: start;

}
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
  justify-content: space-around;
  align-items: center;
  border-bottom: 2px solid rgba(229, 229, 229);
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
}

</style>
