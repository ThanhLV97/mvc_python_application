<template>
  <div class="container-fluid">
    <div class="row justify-content-center align-items-center p-3">
      <div class="col-md-6 d-flex justify-content-center align-items-center">
        <div class="register-group w-100">
          <h1>Sign Up</h1>
          <p class="login-link">Already have an account? <a href="/login">Login here</a></p>
          <div class="form-group">
            <form @submit.prevent="handleSubmit">
              <div class="input-group">
                <label for="username">Username</label>
                <div class="input-container">
                  <i class="icon fas fa-user"></i>
                  <input type="text" id="username" v-model="user.username" v-validate="'required'" placeholder="Enter your username">
                </div>
              </div>
              <div class="input-group">
                <label for="email">Email</label>
                <div class="input-container">
                  <i class="icon fas fa-envelope"></i>
                  <input type="email" id="email" v-model="user.email" v-validate="'required|email'" placeholder="Enter your email">
                </div>
              </div>
              
              <div class="input-group">
                <label for="password">Password</label>
                <div class="input-container">
                  <i class="icon fas fa-lock"></i>
                  <input type="password" id="password" v-model="user.password" v-validate="'required'" placeholder="Enter your password">
                </div>
              </div>
              
              <div class="input-group">
                <label class="remember-label">
                  <input type="checkbox" id="remember" v-model="rememberMe" class="checkbox"/>
                  <span class="checkbox-custom"></span>
                  Remember Me
                </label>
              </div>
              
              <button type="submit" :disabled="status.registering" >Register</button>
            </form>
          </div>
        </div>
        <!-- Error Popup -->
        <div v-if="error" class="popup">
          <p>{{ errorMessage }}</p>
          <button @click="hideErrorPopup">Close</button>
        </div>
      </div>
      <div class="col-md-6 d-none d-md-block">
        <img :src="imagePath" alt="Image" class="image"/>
      </div>
    </div>

  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex';
export default {
    data () {
        return {
            user: {
                username: '',
                email: '',
                password: ''
            },
            submitted: false
        }
    },
    computed: {
        ...mapState('account', ['status']),
        imagePath() {
          return require('@/assets/register.png');
        }
    },
    methods: {
        ...mapActions('account', ['register']),
        handleSubmit() {
          this.submitted = true;
          this.register(this.user);
        }
    }
};
</script>
<style scoped>
@media (max-width: 768px) {
  /* Adjust the height for smaller screens */
  .register-group {
    height: 480px;
    .col-md-6.d-flex.justify-content-center.align-items-center {
      justify-content: space-around;
      padding: 0 20px;
      box-sizing: border-box;
    }
  }
}
.register-group {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 788px;
    height: 784px;
    background-color: #fff;
    border-radius: 10px;
}
.form-group {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.row {
  background-color: #D2D2D2;
}
.remember-label {
  display: flex;
  align-items: center;
  width: 247px;
}

.checkbox {
  display: none; /* Hide the default checkbox */
}

.checkbox-custom {
  display: inline-block;
  width: 14px;
  height: 14px;
  border: 1px solid #000000;
  border-radius: 4px;
  background-color: #fff;
  margin-right: 5px;
}

.checkbox:checked + .checkbox-custom {
  background-color: #007bff;  /* Color when checkbox is checked */
}

.image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.main {
  display: flex;
  flex-direction: row;
  flex: 1;
  background-color: #0056b3;
}

.left {
  flex: 1;
  background-color: #ffff;
  text-align: center;
}

.right {
  flex: 1;
  height: auto;
  width: auto;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #007bff;
}

p {
    margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

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

.input-group {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 20px;

}

label {
  margin-bottom: 5px;
}

input {
  padding: 5px;
  border-radius: 6px;
  border-width: 1px;
  height: 28px;
  border-color: #D2D2D2;
  width: 247px;
}

button {
  width: 247px;
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 30px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

/* Popup Styles */
.popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  padding: 20px;
  border: 1px solid #ccc;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  z-index: 9999;
}

.popup p {
  margin-bottom: 10px;
}

.popup button {
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.popup button:hover {
  background-color: #0056b3;
}
</style>
