<!-- eslint-disable no-restricted-syntax -->
<template>
  <div>
    <div class="my-profile">
      <div class="my-photo-detail">
        <img
          class="my-profile-photo"
          :src="`http://127.0.0.1:8000${profile_picture}`"
          alt=""
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
          <input v-if="editing" v-model="newNickname" />
          <p v-else>{{ nickname }}</p>
          <i
            class="fas fa-pencil fa-lg"
            v-show="editing"
            @click="editNickname"
          ></i>
        </div>
        <button>취향 설정</button>
        <button @click="editProfile">프로필 편집</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "MyProfile",
  data() {
    return {
      editing: false,
      newNickname: "",
      formData: null,
    };
  },
  computed: {
    ...mapState({
      userId: (state) => state.loginStore.userId,
      nickname: (state) => state.mypageStore.nickname,
      profile_picture: (state) => state.mypageStore.profile_picture,
    }),
  },
  methods: {
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

      this.formData = new FormData();
      this.formData.append("id", this.nickname); // id 추가
      this.formData.append("profile_picture", file);

      console.log(this.formData);
      this.$store.dispatch("editPhoto", this.formData);
      this.editing = !this.editing;
    },
  },
};
</script>

<style>
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

.my-profile-detail p {
  font-size: 25px;
}

.my-profile-detail button {
  /* margin: 20px; */
  margin: 10px;
  padding: 10px 20px;
  background: white;
  /* 그림자 수정 필요 */
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
  text-decoration: none;
  border: none;
  cursor: pointer;
}

.my-profile-detail input {
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
