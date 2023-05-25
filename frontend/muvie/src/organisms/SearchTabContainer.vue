<template>
  <div class="tabvue">
    <div v-if="tab == 0">
      <SearchList
        :item="item"
        v-for="(item, idx) in searchedList"
        :key="idx"
      ></SearchList>
      <UserList
        :item="item"
        v-for="(item, idx) in userList"
        :key="idx"
      ></UserList>
    </div>
    <div v-if="tab == 1">
      <SearchList
        :item="item"
        v-for="(item, idx) in searchedList"
        :key="idx"
      ></SearchList>
    </div>
    <div v-if="tab == 2">
      <UserList
        :item="item"
        v-for="(item, idx) in userList"
        :key="idx"
      ></UserList>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import SearchList from "../atoms/SearchList.vue";
import UserList from "../atoms/UserList.vue";

export default {
  name: "SearchTab",
  components: {
    SearchList,
    UserList,
  },
  props: {
    tab: Number,
  },
  computed: {
    ...mapState({
      userId: (state) => state.loginStore.userId,
      searchedList: (state) => state.searchStore.searchedList,
      userList: (state) => state.searchStore.userList,
    }),
    paramId() {
      return this.$route.params.keyword;
    },
  },
  // watch: {
  //   paramId(keyword) {
  //     if (keyword) {
  //       console.log("워치 파라미터");
  //       this.$store.dispatch("getProfile", keyword);
  //     }
  //   },
  // },
  mounted() {
    console.log("마이페이지뷰의 파라미터 전달");
    console.log(this.paramId);
    if (this.paramId) {
      this.$store.dispatch("getSearchList", this.paramId);
      this.$store.dispatch("getUserList", this.paramId);
    }
  },
};
</script>

<style>
.tabvue {
  width: 100%;
}
</style>
