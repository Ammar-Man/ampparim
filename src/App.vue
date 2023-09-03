<template>

<div>


  <h1>Bikes</h1>

 
  
  <bike-item
  
  :bikeName="fa"
  />

  <bike-item

    v-for="x in apiData"
    :bikeName="x.bikeName"
    :bikeCondition="x.bikeCondition"
    :bikePrice="x.bikePrice"
    :moreInfo="x.moreInfo"
    :bikeDate="x.createdAt"
    :_id="x._id"/>

  


  <h1>API Data:</h1>
    <ul>
      <li v-for="item in apiData" :key="item.id">{{ item.bikeName }}</li>
    </ul>
  </div>
</template>

<script>

import axios from 'axios';
const API_URL = "http://localhost:3040";
export default {
  data() {
    return {
      apiData: [], // This will store the fetched data
    };
  },
  mounted() {
    // Make an API GET request when the component is mounted
    axios.get(API_URL+"/bikes")
      .then(response => {
        // Handle the API response and update apiData

        this.apiData = response.data;
        console.log("first test",response.data )
      })
      .catch(error => {
        // Handle any errors
        console.error('Error fetching data:', error);
      });
  },
};

</script>

<style>

</style> 