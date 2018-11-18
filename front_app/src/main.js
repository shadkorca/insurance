import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

new Vue({
    render: h => h(App),
    router,
    store
}).$mount('#app')

// Vue.http.options.credentials = true;
//
// Vue.http.options.xhr = {
//   withCredentials: true
// }
// Vue.http.options.emulateJSON = true
// Vue.http.options.emulateHTTP = true
// Vue.http.options.crossOrigin = true
//
// Vue.http.headers.common['Access-Control-Allow-Origin'] = '*'
// Vue.http.headers.common['Content-Type'] = 'application/x-www-form-urlencoded'
// Vue.http.headers.common['Accept'] = 'application/json, text/plain, */*'
// Vue.http.headers.common['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, Authorization, Access-Control-Allow-Origin'
