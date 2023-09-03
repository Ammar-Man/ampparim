<template>
    <div class="bike-item">
        <div class="side">  <img :src="bikeImg " alt="Bike Image" ></div>
      
<div class="main">
    <h2>{{ bikeName }}</h2>
    <p>Kunto: {{ bikeCondition }}</p>
    <p>Hinta: <b>{{ bikePrice }} </b></p>
    <p>{{ bikeDate }}</p>

    <p>{{ createdAt }}</p>
    <p>Lisätiedot  {{ moreInfo }}</p>
    <p>id: {{ _id }}</p>
</div>

</div>

</template>

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
    data() {
        return {
            name: 'Apples',
            bikeCondition: 'Hyvä',
            bikeDate: '',
            bikeImg: 'https://images.tori.fi/api/v1/imagestori/images/4971449856.jpg?rule=medium_660',
            bikeName: 'Trek Roscoe 8 XL maastopyörä',
            bikePrice: '990',
            createdAt: formatDate('2023-07-13T10:52:10.048Z'),
            moreInfo: 'Myynnissä hyväkuntoinen trek roscoe 8 vm.2019. Runkokoko XL',
            _id: '132112'
        }
    }
};
</script>

<style>
.bike-item {
  display: flex; 
  align-items: center; 
  color: #8a6d3b;
    background-color: #fcf8e3;
    border-color: #faebcc;
    margin-bottom: 20px;
    border: 1px solid transparent;
    border-radius: 4px;
}
.side {
  flex: 10%;
  padding: 20px;
}

/* Main column */
.main {
  flex: 70%;
}


img {
  width: 200px;
  height: 150px;
  padding: 4px;
    line-height: 1.42857143;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 4px;
    -webkit-transition: all .2s ease-in-out;
    -o-transition: all .2s ease-in-out;
    transition: all .2s ease-in-out;
    display: inline-block;
    max-width: 100%;
    height: auto;
}
</style>  