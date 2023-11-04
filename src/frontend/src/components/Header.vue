<!-- Header.vue -->
<template>
  <header>
    <nav>
      <router-link to="/" class="logo">1MT Interview</router-link>
      <div class="nav-links">
        <router-link v-if="!access_token" to="/register">
          <i class="fas fa-user-plus"></i> Register
        </router-link>
        <router-link v-if="!access_token" to="/login">
          <i class="fas fa-sign-in-alt"></i> Login
        </router-link>
        <router-link v-else to="/login">
          <i class="fas fa-sign-out-alt"></i> Logout
        </router-link>
      </div>
    </nav>
  </header> 
</template>

<script>
import '@fortawesome/fontawesome-free/css/all.css';
import vClickOutside from 'v-click-outside';

import { mapState } from 'vuex';

export default {
  name: 'HeaderComponent',
  directives: {
      clickOutside: vClickOutside.directive
  },
  data() {
    return {
      active: false,
    }
  },
  computed: {
    // TODO @thanhlv
    ...mapState('user', ['access_token']),
  },

};
</script>

<style scoped>
.profile {
  display: flex; 
  align-items: center;
  cursor: pointer;
  position: relative;
}
.profile-pulldown {
  position: absolute;
  z-index: 1000;
  background-color: #ffffff;
  right: 0;
  top: 32.5px;
  text-align: left;
}
.account-menu {
  padding-left: 20px;
}
header {
  background-color: #333;
  color: #fff;
  height: 40px;
  align-items: center;
}

nav {
  display: flex;
  justify-content: space-between;
  height: 40px;
  align-items: center;
}

.logo {
  color: #fff;
  font-size: 24px;
  text-decoration: none;
}

.nav-links {
  color: #f5f5f5;
  margin-right: 20px;
}

nav a {
  color: #fff;
  text-decoration: none;
  margin-left: 20px;
}

nav a:hover {
  color: #ccc;
}
</style>
