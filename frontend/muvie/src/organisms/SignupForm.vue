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
        accept="image/*"
      />
      <input type="email" v-model="email" placeholder="Email" />
      <input type="text" v-model="nickname" placeholder="Nickname" />
      <input
        type="password"
        v-model="password"
        placeholder="Password"
        autocomplete="off"
      />
      <button type="submit">Sign up</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "LoginForm",
  data() {
    return {
      email: null,
      nickname: null,
      password: null,
      profilePicture: null,
      profileUrl: null,
    };
  },
  methods: {
    fileChange(e) {
      this.profilePicture = e.target.files[0];
      const url = URL.createObjectURL(e.target.files[0]);
      this.profileUrl = url;
    },
    onSubmit() {
      const userInfo = {};
      userInfo.email = this.email;
      userInfo.password = this.password;
      userInfo.nickname = this.nickname;
      userInfo.profilePicture = this.profilePicture;
      console.log(userInfo);
      this.$store.dispatch("signup", userInfo);
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

button {
  margin: 20px;
  padding: 13px 30px;
  background: white;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
  text-decoration: none;
  border: none;
}

button:hover {
  color: white;
  background: rgba(218, 138, 114, 0.8);
  letter-spacing: 2px;
  cursor: pointer;
}

button:active {
  transform: scale(1.1);
}

.profile-image {
  width: 150px;
  height: 150px;
}
</style>
