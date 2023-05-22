<template>
  <div>
    <div class="mainview">
      <NavBar class="navbar" @open-modal="handleModal" />
      <div class="welcome-msg">
        Hey {{ nickname || "익명의 유저" }} <br />
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
      <div @click="navigateToLogin()">로그인하기</div>
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
        localStorage.getItem("vuex") ? state.loginStore.userInfo.id : "-1",
      nickname: (state) =>
        localStorage.getItem("vuex")
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
