<!-- eslint-disable no-restricted-syntax -->
<template>
  <div>
    <img
      src="../assets/logo3.png"
      alt="로고"
      class="logo"
      @click="navigateToMain()"
    />
    <div class="my-profile">
      <div class="my-photo-detail">
        <img
          class="my-profile-photo"
          :src="`http://127.0.0.1:8000${profile_picture}`"
          alt="프로필 사진"
        />
        <!-- <i class="fas fa-camera fa-4x" v-show="editing" @click="editPhoto"></i> -->
        <!-- 이미지 파일 업로드 버튼 -->
        <i
          class="fas fa-camera fa-4x"
          v-show="editing"
          @click="handleUploadClick"
        ></i>

        <!-- 이미지 파일 선택을 위한 input 요소 -->
        <input
          type="file"
          ref="fileInput"
          style="display: none"
          @change="handleFileChange"
        />
      </div>
      <div class="my-profile-detail">
        <div class="nick-name-detail">
          <input class="nick-name-input" v-if="editing" v-model="newNickname" />
          <p class="my-profile-detail-nickname" v-else>{{ nickname }}</p>
          <i
            class="fas fa-pencil fa-lg"
            v-show="editing"
            @click="editNickname"
          ></i>
        </div>
        <!-- 내 프로필 메뉴 -->
        <div class="my-profile" v-if="me">
          <div class="follow_info">
            <span class="count"
              >{{ followers_count }}
              <p class="follow_tag">팔로워</p>
            </span>
            <span class="count"
              >{{ following_count }}
              <p class="follow_tag">팔로잉</p>
            </span>
            <button class="profile-button" @click="handleModal">
              취향 설정
            </button>
            <button class="profile-button" @click="editProfile">
              프로필 편집
            </button>
          </div>
        </div>
        <!-- 상대 프로필 메뉴 -->
        <div class="other-profile" v-else>
          <div class="follow_info">
            <span class="count"
              >{{ followers_count }}
              <p class="follow_tag">팔로워</p>
            </span>
            <span class="count"
              >{{ following_count }}
              <p class="follow_tag">팔로잉</p>
            </span>
            <button class="profile-button">
              {{ isFollowing() ? "팔로잉" : "팔로우" }}
            </button>
          </div>
        </div>
        <ModalAtom :isModalOpen="isModalOpen">
          <h2>음악 취향</h2>
          <PreferSelect @close-modal="closeModal" />
        </ModalAtom>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapState, mapMutations } from "vuex";
import ModalAtom from "../atoms/ModalAtom.vue";
import PreferSelect from "./PreferSelect.vue";

export default {
  name: "MyProfile",
  data() {
    return {
      me: true,
      editing: false,
      newNickname: "",
      formData: null,
      isModalOpen: false,
    };
  },
  components: {
    ModalAtom,
    PreferSelect,
  },
  // created() {
  //   console.log(this.userId, this.paramId);
  //   // eslint-disable-next-line eqeqeq
  //   console.log(this.userId == this.paramId);
  //   // eslint-disable-next-line eqeqeq
  // },
  watch: {
    paramId(newParamId) {
      // eslint-disable-next-line eqeqeq
      this.me = this.userId == newParamId;
      console.log(`이 유저는 내가 ${this.me}`);
    },
  },
  mounted: {},
  computed: {
    ...mapState({
      userId: (state) => state.loginStore.userId,
      nickname: (state) => state.mypageStore.nickname,
      following: (state) => state.mypageStore.following,
      profile_picture: (state) => state.mypageStore.profile_picture,
      followers_count: (state) => state.mypageStore.followers_count,
      following_count: (state) => state.mypageStore.following_count,
    }),
    paramId() {
      return this.$route.params.userId;
    },
  },
  methods: {
    navigateToMain() {
      this.$router.push({ name: "MainView" });
    },
    ...mapMutations(["updatePhoto"]),
    isFollowing() {
      console.log(this.following);
      console.log("프로필 버튼 조건문");
      return this.following.some((item) => item.id === this.paramId);
    },
    editProfile() {
      console.log("프로필 편집");
      this.editing = !this.editing;
      console.log(this.editing);
    },
    editNickname() {
      const payload = {
        id: this.userId,
        name: this.newNickname,
        // profile_picture: this.profile_picture,
      };
      this.$store.dispatch("editNickname", payload);
      this.editing = !this.editing;
    },
    handleUploadClick() {
      // 이미지 파일 선택을 위해 input 요소 클릭
      this.$refs.fileInput.click();
    },
    handleFileChange(event) {
      // 파일 선택 이벤트 처리
      const file = event.target.files[0];
      console.log("프로필 파일 변경 요청 들어감");

      this.formData = new FormData();
      this.formData.append("id", this.userId); // id 추가
      this.formData.append("profile_picture", file);

      console.log(this.formData);
      console.log(this.userId);

      axios
        .patch(
          `http://127.0.0.1:8000/accounts/edit/${this.userId}/`,
          this.formData
        )
        .then((res) => {
          console.log(res);
          console.log("프로필사진 변경 성공");
          this.updatePhoto(file);
        });
      this.editing = !this.editing;
    },
    handleModal() {
      console.log("모달 오픈");
      this.$store.dispatch("getPreference");
      this.isModalOpen = true;
    },
    closeModal() {
      console.log("모달 닫기");
      this.isModalOpen = false;
    },
  },
};
</script>

<style>
.logo {
  width: 120px;
  height: 40px;
  margin-left: 30px;
  cursor: pointer;
  display: flex;
  justify-content: start;
  top: 30;
}
.follow_info {
  display: flex;
  flex-direction: row;
}

.follow_tag {
  font-size: 15px;
  margin-top: 3px;
  font-weight: normal;
}

.count {
  font-size: 20px;
  margin: 10px;
  font-weight: 600;
}

.my-profile {
  display: flex;
  align-items: center;
  padding-left: 80px;
}

.my-profile i {
  cursor: pointer;
}

.my-photo-detail {
  position: relative;
}

.my-photo-detail i {
  position: absolute;
  top: 18px;
  right: 57px;
  opacity: 0.8;
}

.my-profile-photo {
  width: 100px;
  height: 100px;
  margin-right: 40px;
  background-color: transparent;
  border-radius: 75px;
  overflow: hidden;
  object-fit: cover;
}

.my-profile-detail-nickname {
  font-size: 25px;
}

.my-profile-detail button {
  /* margin: 20px; */
  margin: 10px;
  height: 50px;

  padding: 10px 20px;
  background: white;
  /* 그림자 수정 필요 */
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.1);
  border-radius: 50px;
  text-decoration: none;
  border: none;
  cursor: pointer;
}

.nick-name-input {
  margin: 10px;
  padding: 10px 20px;
  background-color: transparent;
  border-bottom: 1px solid;
}

.nick-name-detail {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 230px;
  height: 85px;
}

.nick-name-detail i {
  margin-left: 15px;
}
</style>
