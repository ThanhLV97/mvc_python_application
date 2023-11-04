import ApiService from "@/services/api.service";

import {
    FETCH_PRODUCT
} from "./actions.type";

import {
    SET_PRODUCT
} from "./mutations.type";

const state = {
    products: [],
};

const getters = {
    loadProducts(state) {
        return state.products.data;
    }
};

const actions = {
    [FETCH_PRODUCT](context) {
        return new Promise(resolve => {
            ApiService.get("products")
            .then(({ data }) => {
                context.commit(SET_PRODUCT, data);
                resolve(data);
            })
        })
    }
}

const mutations = {
    [SET_PRODUCT](state, products) {
        state.products = products;
    },
}


export const product = {
    state,
    getters,
    actions,
    mutations
}
