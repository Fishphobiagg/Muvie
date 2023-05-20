<template>
  <div class="mainview">
    <NavBar />
    <div class="welcome-msg">
      Hey {{ nickname }} <br />
      Welcome Back!
    </div>
    <!-- <CircleCarousel :components="components" /> -->
    <CarouselView :components="components" />
  </div>
</template>

<script>
import { mapState } from "vuex";
import NavBar from "../organisms/NavBar.vue";
// import CircleCarousel from "../organisms/CircleCarousel.vue";
import CarouselView from "../organisms/CarouselView.vue";

export default {
  name: "MainView",
  data() {
    return {};
  },
  components: {
    NavBar,
    // CircleCarousel,
    CarouselView,
  },
  computed: {
    ...mapState({
      nickname: (state) => state.loginStore.userInfo.nickname,
      components: (state) => state.mainStore.componentsRecommends,
      users: (state) => state.mainStore.userRecommends,
      likes: (state) => state.mainStore.likeRecommends,
    }),
  },
  created() {
    this.$store.dispatch("getComponentsRecommends");
    this.$store.dispatch("getUserRecommends");
    this.$store.dispatch("getLikeRecommends");
  },
  methods: {},
};
</script>

<style>
.mainview {
  background: #fff;
}
.welcome-msg {
  width: 500px;
  height: 200px;
  font-size: 70px;
  margin-top: 100px;
  margin-left: 80px;
  opacity: 0.7;
  text-align: left;
}
</style>
