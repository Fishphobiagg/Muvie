<template>
  <div>
    <h2>Signup</h2>
    <form @submit.prevent="onSubmit">
      <div
        class="profile-image"
        :style="`background-image:url(${profileUrl})`"
      ></div>
      <label for="file" class="input-circle"></label>
      <input
        @change="fileChange"
        type="file"
        id="file"
        class="inputFile"
        accept=".gif, .jpg, .png"
      />
      <input type="email" v-model="email" placeholder="Email" />
      <input type="text" v-model="nickname" placeholder="Nickname" />
      <input
        type="password"
        v-model="password"
        placeholder="Password"
        autocomplete="off"
      />
      <button class="submit-button" type="submit">Sign up</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "SignupForm",
  data() {
    return {
      email: null,
      nickname: null,
      password: null,
      profilePicture: null,
      profileUrl: null,
      formData: null,
    };
  },
  methods: {
    fileChange(e) {
      this.profilePicture = e.target.files[0];

      // 프론트 화면 출력을 위한 가공
      const url = URL.createObjectURL(e.target.files[0]);
      this.profileUrl = url;
      console.log(this.profileUrl);
    },
    onSubmit() {
      // 모달 오픈 이벤트 상위 SignupView로 전달
      this.$emit("open-modal");
      if (this.profilePicture == null) {
        this.formData = new FormData();
        this.formData.append("email", this.email);
        this.formData.append("password", this.password);
        this.formData.append("nickname", this.nickname);
      } else {
        this.formData = new FormData();
        this.formData.append("email", this.email);
        this.formData.append("password", this.password);
        this.formData.append("nickname", this.nickname);
        this.formData.append("profile_picture", this.profilePicture);
      }
      console.log(this.formData);
      this.$store.dispatch("signup", this.formData);
    },
  },
};
</script>

<style>
input {
  width: 300px;
  height: 40px;
  border: none;
  margin: 5px;
  padding-left: 10px;
}

input::placeholder {
  color: rgba(218, 138, 114, 0.8);
  margin-left: 5px;
}

.submit-button {
  margin: 20px;
  padding: 13px 30px;
  background: white;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
  text-decoration: none;
  border: none;
}

.submit-button:hover {
  color: white;
  background: rgba(218, 138, 114, 0.8);
  letter-spacing: 2px;
  cursor: pointer;
}

.submit-button:active {
  transform: scale(1.1);
}

.profile-image {
  width: 150px;
  height: 150px;
  background-size: cover;
  background-position: center;
}
</style>
