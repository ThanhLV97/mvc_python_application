import router from '@/router';
import { productServices } from '../services/products';

const products = JSON.parse(localStorage.getItem('products'));
const state = products
    ? { products: products }
    : { products: null};

const actions = {
    search({ dispatch, commit }, { product, category }) {
    
        productServices.search(product, category)
            .then(
                products => {
                    commit('userProduct', products);
                    router.push('/');
                },
                error => {
                    commit('userProduct', error);
                    dispatch('alert/error', error, { root: true });
                }
            );
    },
    getCategories({ dispatch, commit }) {
    
        productServices.getCategories()
            .then(
                products => {
                    commit('userProduct', products);
                    router.push('/');
                },
                error => {
                    commit('userProduct', error);
                    dispatch('alert/error', error, { root: true });
                }
            );
    }
};



const mutations = {
    userProduct(state, products) {
        state.products = products;
    },
};

export const product = {
    namespaced: true,
    state,
    actions,
    mutations
};
