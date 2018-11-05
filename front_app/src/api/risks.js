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
    details_test(risk) {
      return HTTP.get(`/risks/${risk}/`)
    }
}

