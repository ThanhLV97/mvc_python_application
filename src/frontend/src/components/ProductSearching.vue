<template>
    <div>
        <div class="container">
            <div class="search-box">
                <input v-model="product" placeholder="Search">
                <button @click="searchProduct">
                    <i class="fa fa-search"></i> 
                </button>
            </div>
            <div class="dropdown">
                <FilterDropdown
                :options="filterOptions"
                @input="updateFilter"
                />
            </div>
        </div>

    </div>
</template>

<script>
import { mapActions } from 'vuex';
import FilterDropdown from './FilterDropdown';

export default {
components: {
    FilterDropdown
},

data() {
    return {
        product: '',
        category: '',
    }
},

methods: {
    ...mapActions('product', ['search', 'getCategories']),
    updateFilter(value) {
        this.category = value;
    },
    searchProduct() {
        const { product, category } = this;
        this.search({product, category})
    }
},

computed: {
    filterOptions() {
        const categories = this.getCategories()
        console.log("result 1")
        console.log(categories)
        return []
    }
}
}
</script>
<style scoped>
.dropdown {
    display: flex;
    height: 40px;
    align-items: center;
}
.container {
    display: flex;
    flex-direction: row;
    align-items: center;
    align-content: center;
    justify-content: center;

}
.search-box {
    position: relative;
    margin-right: 8px;
}

input {
    margin-top: 24px;
    margin-bottom: 24px;
    padding-left: 30px;
    height: 40px;
    width: 520px;
    border: 1px solid #caccd4;
    border-radius: 100px;
}

.fa-search {
    position: absolute;
    right: 20px;
    top: 35px;
}

</style>