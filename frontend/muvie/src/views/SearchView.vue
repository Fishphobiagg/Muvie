<template>
  <div>
    <SearchList 
    :fwg="item"
    v-for= "(item, idx) in keyword"
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
  props: {
    tab: Number,
  },
  computed: {
    ...mapState({
    searched_list: (state) => state.searchStore.searchedList
    }),
    paramId() {
      return this.$route.params.userId;
    },
  },
  watch: {
    paramId(newId) {
      if (newId) {
        console.log("워치 파라미터");
        this.$store.dispatch("getProfile", newId);
      }
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
