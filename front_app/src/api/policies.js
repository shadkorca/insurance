import { HTTP } from './common'

export const Policy = {
    listPolicies () {
        return HTTP.get('/policies/').then(response => {
          return response.data
        })
    },
    createPolicy(config) {
        return HTTP.post('/policies/', config).then(response => {
          return response.data
        })
    },
    deletePolicy(policy) {
      return HTTP.delete(`/policies/${policy.id}/`)
    }
}
