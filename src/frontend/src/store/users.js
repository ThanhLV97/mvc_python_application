import router from '@/router';
import { userService } from '../services/user';

const user = JSON.parse(localStorage.getItem('user'));
const state = user
    ? { status: { isLoggedIn: true }, user }
    : { status: {}, user: null };

const actions = {
    login({ dispatch, commit }, { username, password }) {
        commit('loginRequest', { username });
    
        userService.login(username, password)
            .then(
                user => {
                    commit('loginSuccess', user);
                    router.push('/');
                },
                error => {
                    commit('loginFailure', error);
                    dispatch('alert/error', error, { root: true });
                }
            );
    },
    register({ dispatch, commit }, user) {
        commit('registerRequest', user);
    
        userService.register(user)
            .then(
                user => {
                    commit('registerSuccess', user);
                    router.push('/login');
                    setTimeout(() => {
                        // display success message after route change completes
                        dispatch('alert/success', 'Registration successful', { root: true });
                    })
                },
                error => {
                    commit('registerFailure', error);
                    dispatch('alert/error', error, { root: true });
                }
            );
    },
    logout({ commit }) {
        userService.logout();
        commit('logout');
    },
};

const mutations = {
    loginRequest(state, user) {
        state.status = { isLoggingIn: true };
        state.user = user;
    },
    loginSuccess(state, user) {
        state.status = { isLoggedIn: true };
        state.user = user;
    },
    loginFailure(state) {
        state.status = { failedLoggingIn: true };
        state.user = null;
    },
    logout(state) {
        state.status = { isLogouted: true };
        state.user = null;
    },
    registerRequest(state, user) {
        state.status = { registering: true };
        state.user = user;

    },
    registerSuccess(state, user) {
        state.status = {};
        state.user = user;

    },
    registerFailure(state, error) {
        state.status = {};
        state.user = error;
    }
};

export const account = {
    namespaced: true,
    state,
    actions,
    mutations
};
