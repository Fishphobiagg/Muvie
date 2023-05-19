<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="onSubmit">
      <input type="email" v-model="email" placeholder="Email" />
      <input
        type="password"
        v-model="password"
        placeholder="Password"
        autocomplete="off"
      />
      <p>Forgot Password?</p>
      <button class="submit-button" type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "LoginForm",
  data() {
    return {
      email: null,
      password: null,
    };
  },
  methods: {
    onSubmit() {
      console.log(this.email);
      console.log(this.password);

      const userInfo = {};
      userInfo.email = this.email;
      userInfo.password = this.password;
      console.log(userInfo);
      this.$store.dispatch("login", userInfo);
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
</style>
