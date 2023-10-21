<template>
  <div id="app">
    <HeaderComponent />
    <div id="main-content">
      <router-view></router-view>
    </div>
    <FooterComponent />
  </div>
</template>

<script>
import FooterComponent from './components/Footer.vue';
import HeaderComponent from './components/Header.vue';

export default {
  name: 'App',
  components: {
    HeaderComponent,
    FooterComponent,
  },
};
</script>

<style>

#app {
  font-family: Arial, sans-serif;
  text-align: center;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

#main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.fancy-button {
    display: inline-block;
    font-family: bebas_neue;
    font-size: 18px;
    letter-spacing: .03em;
    text-transform: uppercase;
    color: #fff;
    position: relative;
}
.fancy-button.pop-onhover:before {
  opacity: 0;
  bottom: 10px;
}
.fancy-button span {
  display: inline-block;
  padding: 9px 30px;
  border-radius: 50em;
  position: relative;
  z-index: 2;
  will-change: transform,filter;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  -webkit-transition: all .3s ease-out;
  transition: all .3s ease-out;
  padding-top: 8px;
}
.btn-danger-gradient span,.btn-danger-gradient:before {
  /* background:#de2826; */
  /* background:-webkit-linear-gradient(left,#de2826 0%,#ea4923 80%,#ea4923 100%); */
  background: linear-gradient(to right,#de2826 0%,#ea4923 80%,#ea4923 100%);
  height: 40px
}

.btn-danger-gradient-line span,.btn-danger-gradient-line:before {
  background: #f8f8f7;
  background: -webkit-linear-gradient(left,#f8f8f7 0%,#f8f8f7 80%,#f8f8f7 100%);
  background: linear-gradient(to right,#f8f8f7 0%,#f8f8f7 80%,#f8f8f7 100%);
  border: 1px solid #b0b0b6;
  box-sizing: border-box;
  color: #414245!important
}
.fancy-button {
  display: inline-block;
  font-family: bebas_neue;
  font-size: 18px;
  letter-spacing: .03em;
  text-transform: uppercase;
  color: #fff;
  position: relative
}

.fancy-button:before {
  content: '';
  display: inline-block;
  height: 40px;
  position: absolute;
  bottom: -5px;
  left: 30px;
  right: 30px;
  z-index: -1;
  border-radius: 30em;
  -webkit-filter: blur(20px) brightness(.95);
  filter: blur(20px) brightness(.95);
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  -webkit-transition: all .3s ease-out;
  transition: all .3s ease-out
}

.fancy-button i {
  margin-top: -1px;
  margin-right: 20px;
  font-size: 1.265em;
  vertical-align: middle
}

.fancy-button span {
  display: inline-block;
  padding: 9px 30px;
  border-radius: 50em;
  position: relative;
  z-index: 2;
  will-change: transform,filter;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  -webkit-transition: all .3s ease-out;
  transition: all .3s ease-out;
  padding-top: 8px
}

.fancy-button span svg {
  margin-right: 5px
}

.fancy-button:focus,.fancy-button:active {
  color: #fff
}

.fancy-button:hover {
  color: #fff
}

.fancy-button:hover span {
  -webkit-filter: brightness(1.05) contrast(1.05);
  filter: brightness(1.05) contrast(1.05);
  -webkit-transform: scale(.95);
  transform: scale(.95)
}

.fancy-button:hover:before {
  bottom: 0;
  -webkit-filter: blur(10px) brightness(.95);
  filter: blur(10px) brightness(.95)
}

.fancy-button.pop-onhover:before {
  opacity: 0;
  bottom: 10px
}

.fancy-button.pop-onhover:hover:before {
  bottom: -7px;
  opacity: 1;
  -webkit-filter: blur(20px);
  filter: blur(20px)
}
a,a:hover,a:focus {
  color: inherit;
  text-decoration: none;
}

.fancy-button.pop-onhover:hover span {
  -webkit-transform: scale(1.04);
  transform: scale(1.04)
}

.fancy-button.pop-onhover:hover:active span {
  -webkit-filter: brightness(1) contrast(1);
  filter: brightness(1) contrast(1);
  -webkit-transform: scale(1);
  transform: scale(1);
  -webkit-transition: all .15s ease-out;
  transition: all .15s ease-out
}

.fancy-button.pop-onhover:hover:active:before {
  bottom: 0;
  -webkit-filter: blur(10px) brightness(.95);
  filter: blur(10px) brightness(.95);
  -webkit-transition: all .2s ease-out;
  transition: all .2s ease-out
}

.btn-danger-gradient-line2 {
  height:40px !important;
  background: 0 0;
  border: 0
}

.btn-danger-gradient-line2 span,.btn-danger-gradient-line2:before {
  background: 0 0;
  background: 0 0;
  background: 0 0;
  border: 1px solid #fff;
  box-sizing: border-box;
  color: #fff!important
}

.btn-danger-gradient-line span {
  padding-top: 7px!important;
  padding-bottom: 6px!important
}

.btn-danger-gradient-line2 span {
  padding-top: 7px!important;
  padding-bottom: 6px!important
}

Footer {
  margin-top: auto;
}
</style>
