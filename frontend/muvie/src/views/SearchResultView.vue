<template>
  <div>
    <img src="../assets/logo.png" alt="" class="logo" @click="navigateToMain()">
    <div class="tab">
      <div class="search-bar">
        <div class="search-input">
          <button class="search-button" @click="handleSearch">
            <i class="fas fa-search"></i>
          </button>
          <input
            class="input-atoms"
            v-model="inputData"
            @keydown.enter="handleSearch"
            placeholder="음악과 사용자를 검색해보세요"
          />
        </div>
        <div class="search-bar-line"></div>
      </div>

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
          유저
        </li>
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
      inputData: "",
    };
  },
  components: {
    SearchTab,
  },
  computed: mapState({
    userId: (state) => state.loginStore.userId,
    searchedList: (state) => state.searchStore.searchedList,
    userList: (state) => state.searchStore.userList,
    keyword() {
      return this.$route.params.keyword;
    },
  }),
  created() {
    if (this.keyword) {
      console.log("키워드 있어");
      console.log(this.keyword);
      this.inputData = this.keyword; // inputData에 파라미터 값을 할당
    }
  },
  methods: {
    handleSearch() {
      if (this.inputData.trim() !== "") {
        this.$router.push({
          name: "SearchResultView",
          params: { keyword: this.inputData },
        });
        this.inputData = "";
      }
    },
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
  position: relative;
  width: 100%;
  overflow: hidden;
  line-height: 1.5;
  font-weight: 300;
}

.search-bar {
  width: 50%;
  margin: 50px auto;
}

.tab-box {
  width: 400px;
  margin: 20px 0 20px 0;
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.tab-box li {
  width: 110px;
  list-style: none;
  font-size: 18px;
  font-weight: 600;
  color: #919191;
  background-color: #fff;
  border: none;
  padding: 13px;
  margin: 5px;
  cursor: pointer;
  border-radius: 40px;
}

.tab-box li.active {
  color: #fff;
  background-color: #7a56e8;
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
