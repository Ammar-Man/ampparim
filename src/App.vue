<template>

<div>


  <h1>Bikes</h1>

 
  <div id="wrapper">


  <bike-item

    v-for="x in apiData"
    :bikeName="x.bikeName"
    :bikeImg="x.bikeImg"
    :bikeCondition="x.bikeCondition"
    :bikePrice="x.bikePrice"
    :moreInfo="x.moreInfo"
    :bikeDate="x.createdAt"
    :_id="x._id" />
</div>


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
async function getAllBikes() {
    const resp = await fetch(API_URL + '/bikes', {
        method: "GET"
    });

    if (resp.status > 201) { return showLoging(); }

    const notes = await resp.json();
    console.log("old",notes);}
    getAllBikes()



</script>

<style>
 #wrapper {
    display: flex;
    flex-wrap: wrap;
  }
  #wrapper > div {
    border: dashed black 1px;
    flex-basis: 200px;
    margin: 10px;
    padding: 10px;
    background-color: lightgreen;
  }
</style> 