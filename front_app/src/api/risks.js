import { HTTP } from './common'

export const Risk = {
    create (config) {
        return HTTP.post('/risks/', config).then(response => {
            return response.data
        })
    },
    delete (risk) {
        return HTTP.delete(`/risks/${risk.id}/`)
    },
    list () {
        return HTTP.get('/risks/').then(response => {
            return response.data
        })
    },
    details(risk) {
        return HTTP.get(`/risks/${risk.id}/`)
    },
    details_test(id) {
        return HTTP.get(`/risks/fields/${id}/`)
    },
    addField(risk_id, config) {
        return HTTP.post(`/risks/fields/${risk_id}`, config).then(response => {
            console.log('response', response.data)
            return response.data
        })
    },
    delField(risk_id, field_id) {
        return HTTP.delete(`/risks/fields/${risk_id}/${field_id}`)
    }
}

