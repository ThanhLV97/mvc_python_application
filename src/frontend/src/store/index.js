import { createStore } from 'vuex';

import { account } from './users';

export const store = createStore({
    modules: {
        account
    }
});
