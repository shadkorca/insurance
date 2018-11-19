import Vue from 'vue'
import Vuex from 'vuex'
import { Risk } from '../api/risks'
import { Policy } from '../api/policies'
import { Field } from "../api/fields"
import { ADD_RISK, REMOVE_RISK, LIST_RISKS,
    ADD_POLICY, REMOVE_POLICY, LIST_POLICIES,
    ADD_FIELD, REMOVE_FIELD, LIST_FIELDS
} from './mutation-types.js'

Vue.use(Vuex)

const state = {
    risks: [],
    policies: [],
    fields: []
}


const getters = {
    risks(state) {
        return state.risks
    },
    policies(state) {
        return state.policies
    },
    fields(state) {
        return state.fields
    }
}

const mutations = {
    [ADD_RISK] (state, risk) {
        state.risks.push(risk)
    },
    [REMOVE_RISK] (state, del_risk) {
        state.risks = state.risks.filter(risk => {
            return risk.id !== del_risk.id
        })
    },
    [LIST_RISKS] (state, { risks }) {
        state.risks = risks
    },

    [ADD_POLICY] (state, policy) {
        state.policies.push(policy)
    },
    [REMOVE_POLICY] (state, del_pol) {
        state.policies = state.policies.filter(policy => {
            return policy.id !== del_pol.id
        })
    },
    [LIST_POLICIES] (state, { policies }) {
        state.policies = policies
    },

    [ADD_FIELD] (state, field) {
        state.fields.push(field)
    },
    [REMOVE_FIELD] (state, del_field_id) {
        state.fields = state.fields.filter(field => {
            return field.id !== del_field_id
        })
    },
    [LIST_FIELDS] (state, { fields }) {
        state.fields = fields
    }
}

const actions = {
    createRisk ({ commit }, riskData) {
        Risk.create(riskData).then(risk => {
            commit(ADD_RISK, risk)
        })
    },
    deleteRisk ({ commit }, del_risk) {
        Risk.delete(del_risk).then(risk => {
            commit(REMOVE_RISK, del_risk)
        })
    },
    getRisks ({ commit }) {
        Risk.list().then(risks => {
            commit(LIST_RISKS, { risks })
        })
    },

    createPolicy ({ commit }, policyData) {
        Policy.createPolicy(policyData).then(policy => {
            commit(ADD_POLICY, policy)
        })
    },
    deletePolicy ({ commit }, del_policy) {
        Policy.deletePolicy(del_policy).then(policy => {
            commit(REMOVE_POLICY, del_policy)
        })
    },
    getPolicies ({ commit }) {
        Policy.listPolicies().then(policies => {
            commit(LIST_POLICIES, { policies })
        })
    },

    createField ({ commit }, fieldData) {
        let field_id = fieldData[0]['id']
        let config = fieldData[1]
        Field.addField(field_id, config).then(field => {
            commit(ADD_FIELD, field)
        })
    },
    deleteField ({ commit }, data) {
        let risk_id = data[0]
        let field_id = data[1]
        Field.delField(risk_id, field_id).then(field => {
            commit(REMOVE_FIELD, field_id)
        })
    },
    getFields ({ commit }, risk_id) {
        Field.listFields(risk_id).then(fields => {
            commit(LIST_FIELDS, { fields })
        })
    }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
