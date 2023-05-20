<template>
  <div>
    <SearchList 
    :item="item"
    v-for= "(item, idx) in searched_list"
    :key="idx">
    </SearchList>
  </div>
</template>

<script>

import { mapState } from "vuex";
import SearchList from '../atoms/SearchList.vue';


export default {
  name: "SearchView",
  components: {
    SearchList,
  },
  computed: {
    ...mapState({
    searched_list: (state) => state.searchStore.searchedList
    }),
    paramId() {
      return this.$route.params.userId;
    },
  },
  computed: {
    ...mapState({
        searched_list: (state) => state.searchStore.searchedList
    }),
    paramId() {
      return this.$route.params.userId;
    },
  },
  mounted() {
    console.log("마이페이지뷰의 파라미터 전달");
    console.log(this.paramId);
    if (this.paramId) {
      this.$store.dispatch("getProfile", this.paramId);
    }
  },
};
</script>


<style></style>
