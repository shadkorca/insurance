import { HTTP } from './common'

export const Field = {
    listFields(id) {
        return HTTP.get(`/risks/fields/${id}/`).then(response => {
            return response.data
        })
    },
    addField(risk_id, config) {
        return HTTP.post(`/risks/fields/${risk_id}/`, config).then(response => {
            return response.data
        })
    },
    delField(risk_id, field_id) {
        return HTTP.delete(`/risks/fields/${risk_id}/${field_id}`)
    },

    listPoliciesFields(id) {
        return HTTP.get(`/policies/fields/${id}/`).then(response => {
            return response.data
        })
    },
    updateFieldValue(risk_id, field_id, config) {
        return HTTP.patch(`/policies/fields/${risk_id}/${field_id}`, config).then(response => {
            return response.data
        })
    }
};

