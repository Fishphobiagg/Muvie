<template>
  <div>
    <div class="mainview">
      <NavBar class="navbar" @open-modal="handleModal" />
      <div class="welcome-msg">
        Hey {{ nickname }} <br />
        Welcome Back!
      </div>
      <!-- <CircleCarousel :components="components" /> -->
      <div v-if="components">
        <CarouselView :components="components" />
      </div>
      <div v-if="users">
        <UsersView :users="users" />
      </div>
      <div v-if="likes">
        <LikesView :likes="likes" />
      </div>
    </div>
    <ModalAtom class="profile-modal" :isModalOpen="isModal1Open">
      <ul>
        <li @click="navigateToProfile(userId)">마이페이지</li>
        <li @click="logout">로그아웃</li>
      </ul>
    </ModalAtom>
    <ModalAtom class="login-request" :isModalOpen="isModal2Open">
      <div>로그인하기</div>
      <div>회원가입하기</div>
    </ModalAtom>
  </div>
</template>

<script>
import { mapState } from "vuex";
import NavBar from "../organisms/NavBar.vue";
// import CircleCarousel from "../organisms/CircleCarousel.vue";
import CarouselView from "../organisms/CarouselView.vue";
import UsersView from "../organisms/UsersView.vue";
import LikesView from "../organisms/LikesView.vue";
import ModalAtom from "../atoms/ModalAtom.vue";

export default {
  name: "MainView",
  data() {
    return {
      isModal1Open: false,
      isModal2Open: false,
      localStorageValue: false,
    };
  },
  components: {
    NavBar,
    // CircleCarousel,
    CarouselView,
    UsersView,
    LikesView,
    ModalAtom,
  },
  methods: {
    handleLocalStorageChange(value) {
      console.log("로컬스토리지 감시");
      if (!value) {
        this.isModal2Open = true;
      } else {
        this.isModal2Open = false;
      }
      console.log(this.isModal2Open);
    },
    handleModal() {
      console.log("부모 컴포넌트에서 모달 오픈");
      this.isModal1Open = !this.isModal1Open;
      console.log(this.isModal1Open);
    },
    navigateToProfile(userId) {
      this.$router.push({ name: "Profile", params: { userId } });
    },
    logout() {
      localStorage.removeItem("vuex");
      this.localStorageValueExists();
    },
    localStorageValueExists() {
      console.log("로컬스토리지 있니?");
      console.log(localStorage.getItem("vuex"));
      console.log(localStorage.getItem("vuex") != null);
      this.localStorageValue =
        // eslint-disable-next-line eqeqeq
        localStorage.getItem("vuex") != null &&
        // eslint-disable-next-line eqeqeq
        localStorage.getItem("vuex") != undefined;
    },
  },
  watch: {
    localStorageValue: {
      immediate: true,
      handler: "handleLocalStorageChange",
    },
  },
  computed: {
    ...mapState({
      userId: (state) =>
        localStorage.getItem("vuex") ? state.loginStore.userInfo.id : "-1",
      nickname: (state) =>
        localStorage.getItem("vuex")
          ? state.loginStore.userInfo.nickname
          : "유저",
      components: (state) =>
        localStorage.getItem("vuex")
          ? state.mainStore.componentsRecommends
          : [],
      users: (state) =>
        localStorage.getItem("vuex") ? state.mainStore.userRecommends : [],
      likes: (state) =>
        localStorage.getItem("vuex") ? state.mainStore.likeRecommends : [],
    }),
  },
  created() {
    if (localStorage.getItem("vuex")) {
      this.$store.dispatch("getComponentsRecommends");
      this.$store.dispatch("getUserRecommends");
      this.$store.dispatch("getLikeRecommends");
    }
  },
  mounted() {
    this.localStorageValueExists();
  },
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

.navbar {
  position: relative;
}

.profile-modal {
  background-color: transparent;
}

.profile-modal .modal-content {
  position: fixed;
  border: 1px solid gray;
  border-radius: 5px;
  top: 150px;
  right: 50px;
  width: 150px;
  min-height: 30px;
  padding: 5px;
  padding: 5px;
}

.profile-modal .modal-content > ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.profile-modal .modal-content > ul > li {
  text-align: center;
  margin: 10px;
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
</style>
