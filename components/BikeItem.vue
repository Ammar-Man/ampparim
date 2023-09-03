<template>
    <div>
        <h2>{{ bikeName }}</h2>
        <img :src=bikeImg alt="" >
        <p>Kunto: {{ bikeCondition }}</p>
        <p>Hinta: <b>{{ bikePrice }} </b></p>
        <p>{{ bikeDate }}</p>
        <p>{{ createdAt }}</p>
        <p>Lisätiedot :  {{ moreInfo }}</p>
        <p>id: {{ _id }}</p>
</div>


</template>
<!-- https://www.w3schools.com/vue/img_quality.svg -->
<script>
function formatDate(inputDateString) {
  // Parse the input date string into a Date object
  const inputDate = new Date(inputDateString);

  // Get the year, month, and day components
  const year = inputDate.getFullYear();
  const month = String(inputDate.getMonth() + 1).padStart(2, "0"); // Months are 0-based
  const day = String(inputDate.getDate()).padStart(2, "0");

  // Create the formatted date string
  const formattedDateString = `${year}-${month}-${day}`;

  // Return the formatted date string
  return formattedDateString;
}

// Example usage:
const originalDateString = "2023-07-13T10:52:10.048Z";
const formattedDate = formatDate(originalDateString);
console.log(formattedDate); // Output: "2023-07-13"


export default {
    props:["bikeName","bikeImg","bikeCondition","bikePrice","bikeDate","bikeDate","createdAt","moreInfo","_id","isFavorite"],
    data() {
        return {
         
        }
    },
    methods: {
       
    }
};
</script>

<style>
img{
    width: 200px;
    height: 150px;
}
</style>  