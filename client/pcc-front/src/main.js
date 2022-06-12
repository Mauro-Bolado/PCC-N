import { createApp } from 'vue'
import App from './App.vue'
import Vue from 'vue'
import axios from 'axios'

Vue.prototype.$http = axios

app = new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})

createApp(App).mount('#app')
