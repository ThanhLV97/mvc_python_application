import { createStore } from 'vuex';

import { product } from './products';
import { account } from './users';

export const store = createStore({
    modules: {
        account,
        product
    }
});
