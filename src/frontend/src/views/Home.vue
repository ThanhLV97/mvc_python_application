<!-- Home.vue -->
<template>
    <main>
      <ProductSearching/>
      <section class="hero">
        <div class="hero-content">
          <img src="https://www.z2u.com/static/platform/img/index/big-show-pic02.webp" alt="" width="100%" height="auto">
          <div class="text-wrap">
            <span class="text-1">Get Started For World Developing</span>
            <br>
            <span class="text-2">YOU NEED TO START ENJOYING WORLD!</span>
            <p class="text-3">First, solve the problem. Then, write the code.</p>
            <br>
            <a href="/register" class="aa fancy-button pop-onhover btn-danger-gradient"
              style="margin-right: 15px; width: 215px;">
              <span style="width: 100%">Register</span>
            </a>
            <button class="fancy-button pop-onhover btn-danger-gradient-line2" style="margin-left: 15px; width: 215px;">
              <span style="width: 100%" class="text-nowrap">How It Works?</span>
            </button>
          </div>
        </div>
      </section>
      <section class="features">
        <div class="feature">
          <i class="fas fa-cogs"></i>
          <h2>Powerful Services</h2>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
        <div class="feature">
          <i class="fas fa-users"></i>
          <h2>Expert Team</h2>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
        <div class="feature">
          <i class="fas fa-lightbulb"></i>
          <h2>Innovative Solutions</h2>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        </div>
      </section>
      <section>
        <div class="products">
          <ProductCard class="products-card"
            v-for="product in products"
            :key="product.id"
            :product="product"
            @add-to-cart="addToCart" 
          />
        </div>
      </section>
    </main>
</template>

<script>
import ProductCard from '@/components/ProductCard.vue';
import ProductSearching from '@/components/ProductSearching.vue';

export default {
  name: 'HomePage',
  components: {
    ProductSearching,
    ProductCard
  },
  data() {
    return {
      // TODO @Thanhlv - fetch data from backend
      products: [
        {
          price: 12,
          stock: 5,
          description: 23,
          name: 'product_1',
          image: 'https://img.icons8.com/ios/100/image--v1.png'
        },
        {
          price: 12,
          stock: 5,
          description: 23,
          name: 'product_1',
          image: 'https://img.icons8.com/ios/100/image--v1.png'
        }
      ]
    }
  }
};
</script>

<style scoped>
  
  .products {
    display: flex;
    flex-wrap: wrap;
  }
  .product-card {
    margin: 5px;
  }

  /* Styles for hot-game-box-list-card */
  .hot-game-box-list-card .more-btn {
    background: #fb7600;
    color: var(--color-1);
    font-size: 14px;
    width: 140px;
    height: 32px;
    line-height: 32px;
    text-align: center;
    display: inline-block;
    border-radius: 5px;
    margin-left: auto;
    margin-right: auto;
  }
  
  /* Reset default styles for certain elements */
  ul, li, ol, h1, h2, h3, h4, h5, h6, dd, dt, p {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  a {
    color: #2780E3;
    text-decoration: none;
  }
  .hot-game-box-list-card .game-info-list li a {
    color: #fff;
    text-decoration: none;
  }
  .hot-game-box-list-card .game-info-list li span {
    float: right;
    padding: 0 6px;
    border: 1px solid #fff;
    border-radius: 30px;
    font-size: 14px;
    display: inline-block;
  }
  .hot-game-box-list-card .game-info-list li {
    justify-content: space-between;
    align-items: center;
    padding-top: 15px;
    display: list-item;
    padding-bottom: 15px;
    list-style-type: none;
    font-size: 14px;
    color: #fff;
    border-top: 1px solid rgba(255,242,179,.3);
  }
  /* Styles for hot-game-box-list-card */
  .hot-game-box-list-card .game-info-list {
    margin: 15px 0 0;
    padding: 0;
    font-size: 14px;
  }
  
  .hot-game-box-list-card .title-top {
    text-align: right;
    font-family: var(--font-family-1);
    font-size: 24px;
    color: #fff;
  }
  
  .hot-game-box-list-card .icon-top {
    position: absolute;
    width: 70px;
    height: 70px;
    border-radius: 5px;
    left: 15px;
    top: -30px;
    z-index: 2;
    border: 1px solid #ffd557;
    box-shadow: 10px 10px 30px #fc9700;
    overflow: hidden;
  }
  .hot-game-box-list-card {
    align-items: center;
    border-radius: 5px;
    background-size: 100%;
    padding: 15px 15px 22px;
    position: relative;
  }
  
  /* Styles for background cards */
  .background-card-1 {
    background: #fec200 url(https://www.z2u.com/static/platform/img/index/hot-game-bg-1.webp) no-repeat;
    background-size: 100%;
    border-radius: 5px;
    padding: 15px 15px 22px;
    position: relative;
  }
  
  .background-card-2 {
    background: #8846ff url(https://www.z2u.com/static/platform/img/index/hot-game-bg-2.png) no-repeat;
    background-size: 100%;
    border-radius: 5px;
    padding: 15px 15px 22px;
    position: relative;
  }
  
  .background-card-3 {
    background: #1d244b url(https://www.z2u.com/static/platform/img/index/hot-game-bg-3.png) no-repeat;
    background-size: 100%;
    border-radius: 5px;
    padding: 15px 15px 22px;
    position: relative;
  }
  
  .background-card-4 {
    background: #0397ff url(https://www.z2u.com/static/platform/img/index/hot-game-bg-4.png) no-repeat;
    background-size: 100%;
    border-radius: 5px;
    padding: 15px 15px 22px;
    position: relative;
  }
  
  /* Additional styles */
  .margin_top30 {
    margin-top: 30px;
  }
  
  .main .popular_game .title {
    font-size: 42px;
    font-weight: 700;
    color: var(--color-2);
    padding: 40px 0 10px;
    font-family: var(--font-family-1);
  }
  
  .text-center {
    text-align: center;
  }
  
  .container {
    margin-right: auto;
    margin-left: auto;
    padding-left: 15px;
    padding-right: 15px;
  }
  .hero-content {
    position: relative;
  }
  .hero-content img {
    width: 100%;
    height: 390px;
    filter: brightness(60%);
    max-width: 100%;
  }
  
  .hero-content .text-wrap {
    transform: translate(-50%, -50%);
    white-space: normal !important;
    width: 1363px;
    position: absolute;
    left: 50%;
    top: 50%;
    text-align: center;
    color: var(--color-1);
    padding-top: 40px;
    padding-bottom: 30px;
    box-sizing: border-box;
    font-family: var(--font-family-1);
  }
  .hero-content .text-wrap .text-1 {
    font-size: 55px;
    display: inline-block;
    border-bottom: 2px solid #de3726
  }
  
  .hero-content .text-wrap .text-2 {
    white-space: nowrap;
    font-size: 70px;
    display: inline-block
  }
  
  .hero-content .text-wrap .text-3 {
    font-family: Arial;
    font-size: 16px;
    margin-bottom: 30px
  }
  
  .hero {
    background-color: var(--background-color-1);
  }
  
  .hero h1 {
    font-size: 40px;
    margin-bottom: 20px;
  }
  
  .hero p {
    font-size: 18px;
    margin-bottom: 40px;
  }
  
  .features {
    display: flex;
    justify-content: center;
    margin-top: 40px;
  }
  
  .feature {
    max-width: 300px;
    padding: 20px;
    text-align: center;
  }
  
  .feature i {
    font-size: 40px;
    margin-bottom: 20px;
  }
  
  .feature h2 {
    font-size: 24px;
    margin-bottom: 10px;
  }
  
  .feature p {
    font-size: 16px;
    color: var(--color-3);
  }
  </style>
