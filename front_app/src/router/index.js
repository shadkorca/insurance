import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import risks from '@/components/RiskPage'
import policies from '@/components/PolicyPage'
import risk_fields from '@/components/RiskFields'
import risk_details from '@/components/RiskDetailsPage'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'policies',
      component: policies,
      props: true
    },
    {
      path: '/risks_detail',
      name: 'risks',
      component: risks,
      props: true
    },
    {
      path: '/risk_details',
      name: 'risk_details',
      component: risk_details,
      props: true
    }

  ]
})