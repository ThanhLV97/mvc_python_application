<template>
  <div class="container-fluid">
    <div class="row justify-content-center align-items-center p-3">
      <div class="col-md-6 d-none d-md-block">
        <div class="logo-wellcome">
          <img :src="loginImagePath" alt="Image" class="img-fluid"/>
        </div>
      </div>
      <div class="col-md-6 d-flex justify-content-center align-items-center">
        <div class="login-group w-100">
          <div class="wellcome-group">
            <div class="login-slogan">
              <p>Wellcome to</p>
              <h3>AI4U Shop</h3>
            </div>
          </div>
          <div class="form-group">
            <form @submit.prevent="handleSubmit">
              <div class="input-group">
                <label for="username">Email</label>
                <div class="input-container">
                  <i class="icon fas fa-envelope"></i>
                  <input type="text" id="username" v-model="username" placeholder="Enter your email">
                </div>
              </div>
              <div class="input-group">
                <label for="password">Password</label>
                <div class="input-container">
                  <i class="icon fas fa-lock"></i>
                  <input type="password" id="password" v-model="password" placeholder="Enter your password">
                </div>
              </div>
              <button type="submit">Login</button>
            </form>
            <div class="redirect-to-signup">
              <p class="login-link">Don't have an account? <a href="/register">Sign up</a></p>
            </div>
        </div> 
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import '@fortawesome/fontawesome-free/css/all.css';
import { mapActions, mapState } from 'vuex';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';

export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  computed: {
    ...mapState('user', ['status']),
    logoImagePath() {
      return require('@/assets/logo.png');
    },
    loginImagePath() {
      return require('@/assets/login.png');
    }
  },
  created () {
      this.logout();
  },
  methods: {
      ...mapActions('account', ['login', 'logout']),
      handleSubmit () {
          this.submitted = true;
          const { username, password } = this;
          if (username && password) {
              this.login({ username, password })
          }
      }
  }
};
</script>

<style scoped>
/* Add your login page styles here */

.input-container {
  position: relative;
}

.input-container input {
  padding-left: 2.5rem; /* Adjust this value as needed */
}

.input-container .icon {
  position: absolute;
  top: 50%;
  left: 0.75rem; /* Adjust this value as needed */
  transform: translateY(-50%);
  pointer-events: none;
}

img {
  width: 640.14px;
  height: 639.43px;
}
.row {
  background-color: #D2D2D2;
}
.login-group {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 788px;
  height: 784px;
  background-color: #fff;
  border-radius: 10px;
}
@media (max-width: 768px) {
  /* Adjust the height for smaller screens */
  .login-group {
    height: 480px;
    .col-md-6.d-flex.justify-content-center.align-items-center {
      justify-content: space-around;
      padding: 0 20px;
      box-sizing: border-box;
    }
  }
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}
.login-slogan {
  margin-bottom: 52px;

}
.login-slogan h3 {
  color: #0056b3;

}

.form-group {
  display: flex;
  flex-direction: column;
  align-items: center;
}
form {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px;
  .input-group {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-bottom: 20px;
  }
}
label {
  margin-bottom: 10.33px;

}
input {
  padding: 5px;
  border-radius: 4px !important;
  border-width: 1px;
  height: 36px;
  border-color: #D2D2D2;
  width: 212px;
}

button {
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 8.8px;
  cursor: pointer;
  width: 212px;
  margin-bottom: 20px;
}

button:hover {
  background-color: #0056b3;
}
</style>

