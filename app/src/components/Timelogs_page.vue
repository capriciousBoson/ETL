<template>
  <div>
    
    <a class="btn btn-primary" href="/reports" role="button">show reports</a>
    
  </div>
    <div>
      <Table />
    </div>
  </template>
  
  <script>
  import Table from './timelogs_table.vue';
  export default {
    name: 'Timelogs_page',
    components: {
      Table
    }
  };
  </script>