// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import header1 from '@/views/component/header1'
import slider1 from '@/views/component/slider1'
import slider2 from '@/views/component/slider2'
import footer from '@/views/component/footer'
import bottom from '@/views/component/bottom'
import change from '@/views/component/change'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.min'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)
Vue.config.productionTip = false

Vue.component('app-header1', header1)
Vue.component('app-slider1', slider1)
Vue.component('app-slider2', slider2)
Vue.component('app-change', change)
Vue.component('app-bottom', bottom)
Vue.component('app-footer', footer)
Vue.prototype.$site_url = 'http://dev.paas.aioper.cn:8000'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
