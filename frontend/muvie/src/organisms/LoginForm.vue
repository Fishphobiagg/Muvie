<template>
  <div>
    <h2>Login</h2>
    <label for=""><input type="email" placeholder="Email" /></label>
    <label for=""><input type="password" placeholder="Password" /></label>
    <p>Forget Password?</p>
    <button>Login</button>
  </div>
</template>

<script>
export default {
  name: "LoginForm",
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
</style>
