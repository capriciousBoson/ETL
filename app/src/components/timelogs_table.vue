<template>
  <div class="container">
    <table class="table table-striped">
      <thead class="thead-dark">
        <tr>
          <th>No.</th>
          <th>Team</th>
          <th>Username</th>
          <th>Job Number</th>
          <th>Booking Codes</th>
          <th>Booking Date</th>
          <th>Time Tracked</th>
          <th>Task Estimate</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in slicedItems" :key="item.id">
          <td>{{ (currentPage - 1) * itemsPerPage + index + 1 }}</td>
          <td>{{ item.team }}</td>
          <td>{{ item.username }}</td>
          <td>{{ item.job_number }}</td>
          <td>{{ item.booking_codes }}</td>
          <td>{{ item.booking_date }}</td>
          <td>{{ item.time_tracked }}</td>
          <td>{{ item.task_estimate }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="pagination centered">
    <button class="btn btn-success" :disabled="currentPage === 1" @click="previousPage">Previous</button>
    <span style="margin-left: 50px;">Page {{ currentPage }} of {{ pageCount }}</span>
    <button class="btn btn-success" style="margin-left: 50px;" :disabled="currentPage === pageCount"
      @click="nextPage">Next</button>
  </div>
</template>
  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      currentPage: 1, //stores the current page number
      itemsPerPage: 10,
      items: []
    }
  },
  computed: {
    //a computed property that returns the 
    //sliced array of items based on the current page 
    // and items per page
    slicedItems() {
      const start = (this.currentPage - 1) * this.itemsPerPage
      const end = start + this.itemsPerPage
      return this.items.slice(start, end)
    },
    pageCount() {
      return Math.ceil(this.items.length / this.itemsPerPage)
    }
  },
  methods: {
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--
      }
    },
    nextPage() {
      if (this.currentPage < this.pageCount) {
        this.currentPage++
      }
    }

  },
  created() {

    axios.get('http://localhost:8000/timelogs/api/')
      .then(response => {
        this.items = response.data;
      })
      .catch(error => {
        console.log(error);
      });
    window.addEventListener('keydown', this.handleKeyDown)
  },
  beforeUnmount() {
    window.removeEventListener("keydown", this.handleKeyDown);
  },


};
</script>

<style scoped>
.centered {
  display: flex;
  justify-content: center;
}
</style>
