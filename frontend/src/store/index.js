import Vue from 'vue'
import Vuex from 'vuex'
import { Note } from '../api/risks'
import {
  ADD_RISK,
  REMOVE_RISK,
  SET_RISKS
} from './mutation-types.js'

Vue.use(Vuex)

const state = {
  risks: []
}

const getters = {
  risks: state => state.risks
}

const mutations = {
  [ADD_RISK] (state, risk) {
    state.risks = [risk, ...state.risks]
  },
  [REMOVE_RISK] (state, { id }) {
    state.risks = state.risks.filter(risk => {
      return risk.id !== id
    })
  },
  [SET_RISKS] (state, { risks }) {
    state.risks = risks
  }
}

const actions = {
  createRisk ({ commit }, riskData) {
    Note.create(riskData).then(risk => {
      commit(ADD_RISK, risk)
    })
  },
  deleteRisk ({ commit }, risk) {
    Note.delete(risk).then(risk => {
      commit(REMOVE_RISK, risk)
    })
  },
  getRisks ({ commit }) {
    Note.list().then(risks => {
      commit(SET_RISKS, { risks })
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
