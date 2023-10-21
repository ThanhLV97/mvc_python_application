<template>
    <v-combobox class="my-combobox"
    v-model="select"
    :items="options"
    label="Category Filtering"
    multiple
    chips
  ></v-combobox>
  </template>
  
  <script>
  export default {
    props: ['options'],
    data() {
      return {
        selected: [],
      }
    },

    methods: {
      remove(item) {
        this.selected = this.selected.filter(i => i !== item)
      }
    }
  } 
  </script>
<style scoped>
.v-combobox {
    height: 40px;
    width: 240px;
}

.v-combobox-input {
    height: 40px;
}
.v-input__control {
    height: 40px;
}
.my-combobox .v-menu {
  width: 100%;
}

/* Chips */  
.my-combobox .v-chip {
  height: 24px;
}

.my-combobox .v-label {
    line-height: 40px;
  }

</style>
