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
    }
}

