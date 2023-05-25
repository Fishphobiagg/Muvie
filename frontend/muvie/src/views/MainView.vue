<template>
  <div>
    <div class="mainview">
      <NavBar class="navbar" @open-modal="handleModal" />
      <div class="one-view">
        <div class="welcome-msg">
          {{ nickname || "익명의 유저" }} 님을 위한 <br />오늘의 음악
        </div>
        <!-- <CircleCarousel :components="components" /> -->
        <div class="full-height-container first">
          <transition name="slide">
            <div class="full-height-scroll">
              <CarouselView :components="components" />
            </div>
          </transition>
        </div>
      </div>
      <div class="full-height-container">
        <transition name="slide">
          <div class="full-height-scroll">
            <UsersView :users="users" />
          </div>
        </transition>
      </div>
      <div class="full-height-container">
        <transition name="slide">
          <div class="full-height-scroll">
            <LikesView :likes="likes" />
          </div>
        </transition>
      </div>
    </div>
    <ModalAtom class="profile-modal" :isModalOpen="isModal1Open">
      <ul>
        <li @click="navigateToProfile(userId)">마이페이지</li>
        <li @click="logout">로그아웃</li>
      </ul>
    </ModalAtom>
    <ModalAtom class="login-request" :isModalOpen="isModal2Open">
      <div></div>
      <img class="modal-logo" src="../assets/logo2.png" alt="" />
      <h2 class="explanation">
        당신의 영화를 듣고, <br />좋아하고, <br />즐겨보세요
      </h2>
      <p>로그인하면 더 많은 음악을 만나실 수 있습니다!</p>
      <div class="option-container">
        <div @click="navigateToLogin()" class="option">로그인</div>
        <div @click="navigateToSignup()" class="option">회원가입</div>
      </div>
    </ModalAtom>
    <YoutubePlayer />
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
import YoutubePlayer from "../organisms/YoutubePlayer.vue";

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
    YoutubePlayer,
  },
  methods: {
    handleModal() {
      console.log("부모 컴포넌트에서 모달 오픈");
      this.isModal1Open = !this.isModal1Open;
      console.log(this.isModal1Open);
    },
    navigateToProfile(userId) {
      this.$router.push({ name: "Profile", params: { userId } });
    },
    navigateToLogin() {
      this.$router.push({ name: "Login" });
    },
    navigateToSignup() {
      this.$router.push({ name: "Signup" });
    },
    logout() {
      const vuexData = JSON.parse(localStorage.getItem("vuex"));
      if (vuexData && vuexData.loginStore) {
        delete vuexData.loginStore;
        localStorage.setItem("vuex", JSON.stringify(vuexData));
      }
      this.localStorageValueExists();
    },
    localStorageValueExists() {
      console.log("로컬스토리지 있니?");
      const vuexData = JSON.parse(localStorage.getItem("vuex"));
      console.log(vuexData.loginStore);
      this.localStorageValue = vuexData.loginStore;
    },
    handleLocalStorageChange(value) {
      console.log("있으면 감시");
      if (!value) {
        this.isModal2Open = true;
      } else {
        this.isModal2Open = false;
      }
      console.log(this.isModal2Open);
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
        localStorage.getItem("vuex") && state.loginStore.userInfo
          ? state.loginStore.userInfo.id
          : "-1",
      nickname: (state) =>
        localStorage.getItem("vuex") && state.loginStore.userInfo
          ? state.loginStore.userInfo.nickname
          : "익명의 유저",
      components: (state) =>
        localStorage.getItem("vuex")
          ? state.mainStore.componentsRecommends
          : [
              {
                title: "American Beauty",
                artist: "Thomas Newman",
                album: "American Beauty (Soundtrack)",
                poster:
                  "https://i.scdn.co/image/ab67616d0000b273e0deac21921480ebcb0ecae0",
                "like count": 0,
              },
              {
                title: "Sally's Song",
                artist: "Catherine O'Hara",
                album: "Nightmare Before Christmas Special Edition",
                poster:
                  "https://i.scdn.co/image/ab67616d0000b27347cc5d86f3528b233f2b78ff",
                "like count": 0,
              },
              {
                title: "Abraham's Daughter",
                artist: "Arcade Fire",
                album: "The Hunger Games: Songs From District 12 And Beyond",
                poster:
                  "https://i.scdn.co/image/ab67616d0000b273d29a5d713277b0b3d517507b",
                "like count": 0,
              },
              {
                title: "Wheel of Fortune",
                artist: "Hans Zimmer",
                album:
                  "Pirates Of The Caribbean - Dead Man's Chest Original Soundtrack (English Version)",
                poster:
                  "https://i.scdn.co/image/ab67616d0000b273d80f11f52191d80b84e80221",
                "like count": 0,
              },
              {
                title:
                  'Noble Maiden Fair (A Mhaighdean Bhan Uasal) - From "Brave"/Soundtrack',
                artist: "Emma Thompson",
                album: "Brave",
                poster:
                  "https://i.scdn.co/image/ab67616d0000b2738ce48a7507eab97d87c70687",
                "like count": 0,
              },
            ],
      users: (state) =>
        localStorage.getItem("vuex")
          ? state.mainStore.userRecommends
          : [
              {
                id: 54,
                email: "minji20@example.com",
                nickname: "민지20",
                profile_picture: "users/default.gif",
              },
              {
                id: 36,
                email: "minji1@example.com",
                nickname: "민지1",
                profile_picture: "/users/default.gif",
              },
              {
                id: 43,
                email: "minji8@example.com",
                nickname: "민지8",
                profile_picture: "/users/default.gif",
              },
              {
                id: 50,
                email: "minji16@example.com",
                nickname: "민지16",
                profile_picture: "/users/default.gif",
              },
              {
                id: 51,
                email: "minji17@example.com",
                nickname: "민지17",
                profile_picture: "/users/default.gif",
              },
            ],
      likes: (state) =>
        localStorage.getItem("vuex")
          ? state.mainStore.likeRecommends
          : [
              {
                id: 28344,
                title: "Only Way",
                artist: "Danny Elfman",
                album_cover:
                  "https://i.scdn.co/image/ab67616d0000b2731eba7c491721451464a322a7",
                like_count: 2,
              },
              {
                id: 30000,
                title: "Ba Do Bleep",
                artist: "The Minions",
                album_cover:
                  "https://i.scdn.co/image/ab67616d0000b2737d15f4754a70b55dac6cd56e",
                like_count: 3,
              },
              {
                id: 34000,
                title: "The House of Belonging",
                artist: "Junkie XL",
                album_cover:
                  "https://i.scdn.co/image/ab67616d0000b27311eb862950737980343df57d",
                like_count: 3,
              },
              {
                id: 24344,
                title: "Colette Shows Him Le Ropes",
                artist: "Michael Giacchino",
                album_cover:
                  "https://i.scdn.co/image/ab67616d0000b273da96ceef85aba33d1e68b773",
                like_count: 1,
              },
              {
                id: 25252,
                title: "I'm Goblin",
                artist: "Hans Zimmer",
                album_cover:
                  "https://i.scdn.co/image/ab67616d0000b273aedd0ee1a89b21cd9da5c9b3",
                like_count: 1,
              },
            ],
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
.explanation {
  margin-right: 50px;
  margin-left: 50px;
}

.option-container {
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.modal-logo {
  margin-right: 2px;
  margin-bottom: 20px;
}

.option-container {
  height: 250px;
}

.option {
  margin-top: 20px;
  padding: 10px;
  color: white;
  border: 2px solid white;
  border-radius: 10px;
  background: rgb(123, 86, 232);

  font-size: 20px;
  cursor: pointer;
}

.option:hover {
  margin-top: 20px;
  padding: 10px;
  color: white;
  border: 2px solid white;
  border-radius: 10px;
  background: rgb(123, 86, 232, 0.8);

  font-size: 20px;
  cursor: pointer;
}

.mainview {
  background: #eef3f7;
  /* height: 50vh; */
  overflow-y: auto;
}

.first {
  position: absolute;
  top: 0.5;
  right: 0;
  width: 100%;
  height: 100%;
  z-index: 3;
  background-color: transparent;
}

.full-height-scroll {
  flex: 1;
  overflow-y: auto;
  /* padding: 20px; */
}

.one-view {
  width: 100vw;
  height: 100vh;
}

.welcome-msg {
  width: 600px;
  height: 200px;
  font-size: 60px;
  margin-top: 50px;
  margin-left: 80px;
  text-align: left;
  opacity: 0.9;
  /* z-index: -2; */
  background-color: transparent;
}

.navbar {
  position: relative;
}

.profile-modal {
  background-color: transparent;
}

.profile-modal .modal-content {
  position: fixed;
  border-radius: 5px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  top: 90px;
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
.login-request {
  display: flex;
}
.login-request .modal-content {
  width: 400px;
  min-height: 580px;
  justify-content: center;
}
</style>
