<template>
  
  <div>
    <Header />
    <router-view></router-view>
    <Footer />
  </div>
  <div>
  
  </div>
</template>

<script>
//import Table from './components/timelogs_table.vue';
import Header from './components/Header_global.vue';
import Footer from './components/Footer_global.vue';

export default {
  components: {
    Header,
    Footer
  }
}
</script>
