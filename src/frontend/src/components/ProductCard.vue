// ProductCard.vue

<template>
  <div class="product-card">
    <img :src="product.image" :alt="product.name">
    
    <h4>{{ product.name }}</h4>
    
    <p>{{ product.description }}</p>
    
    <div class="product-info">
      <p>Price: ${{ product.price }}</p> 
      
      <p>
        <span 
          v-for="n in 5"
          :key="n"
          class="fas fa-star"
          :class="{ checked: n <= product.rating }"
        ></span>
      </p>
      
      <p>
        <i class="fas fa-truck"></i>
        Free Shipping
      </p>
      
      <p>
        {{ product.stock > 0 ? "In Stock" : "Out of Stock" }}  
      </p>
    </div>
    
    <button 
      class="button"
      @click="addToCart"
      :disabled="product.stock <= 0"
    >
      Add to Cart
    </button>
  </div>
</template>

<script>
export default {
  props: ['product'],
  
  methods: {
    addToCart() {
      this.$emit('add-to-cart', this.product)
    }
  }
}
</script>

<style scoped>
/* Card styles */  
</style>
