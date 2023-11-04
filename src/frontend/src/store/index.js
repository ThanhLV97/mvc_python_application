import { createStore } from 'vuex';

import { user } from './auth.module';
import { product } from './product.module';

export const store = createStore({
    modules: {
        user,
        product
    }
});

