import ApiService from "@/services/api.service";
import JwtService from "@/services/jwt.service";

import {
  CHECK_AUTH,
  LOGIN,
  LOGOUT,
  REGISTER,
  UPDATE_USER
} from "./actions.type";

import {
  PURGE_AUTH,
  SET_AUTH,
  SET_ERROR,
  SET_USER
} from "./mutations.type";

const state = {
  errors: null,
  user: {},
  isAuthenticated: !!JwtService.getToken()
};

const getters = {
  currentUser(state) {
    return state.user;
  },
  isAuthenticated(state) {
    return state.isAuthenticated;
  }
};

const actions = {
  [LOGIN](context, credentials) {
    return new Promise(resolve => {
      ApiService.post("auth/login", credentials)
        .then(( { data }) => {
          context.commit(SET_AUTH, data.access_token);
          resolve(data);
        })
        .catch(({ response }) => {
          context.commit(SET_ERROR, response.json());
        });
    });
  },
  [LOGOUT](context) {
    context.commit(PURGE_AUTH);
  },
  [REGISTER](context, credentials) {
    return new Promise((resolve, reject) => {
      ApiService.post("users", { credentials })
        .then(({ data }) => {
          context.commit(SET_AUTH, data.user);
          resolve(data);
        })
        .catch(({ response }) => {
          context.commit(SET_ERROR, response.data.errors);
          reject(response);
        });
    });
  },
  [CHECK_AUTH](context) {
    if (JwtService.getToken()) {
      ApiService.setHeader();
      ApiService.get('users', 'me')
        .then(({ data }) => {
          context.commit(SET_USER, data);
        })
        .catch(({ response }) => {
          context.commit(SET_ERROR, response.data.errors);
        });
    } else {
      context.commit(PURGE_AUTH);
    }
  },
  [UPDATE_USER](context, payload) {
    const { email, username, password, image, bio } = payload;
    const user = {
      email,
      username,
      bio,
      image
    };
    if (password) {
      user.password = password;
    }

    return ApiService.put("user", user).then(({ data }) => {
      context.commit(SET_AUTH, data.user);
      return data;
    });
  }
};

const mutations = {
  [SET_ERROR](state, error) {
    state.errors = error;
  },
  [SET_AUTH](state, access_token) {
    state.isAuthenticated = true;
    state.errors = {};
    JwtService.saveToken(access_token);
  },
  [SET_USER](state, user) {
    state.user = user;
    state.isAuthenticated = true;
  },
  [PURGE_AUTH](state) {
    state.isAuthenticated = false;
    state.user = {};
    state.errors = {};
    JwtService.destroyToken();
  }
};

export const user = {
  state,
  actions,
  mutations,
  getters
};
