// // Wait for the DOM to be ready
// document.addEventListener('DOMContentLoaded', function() {

//   var searchBox = document.getElementById('search-box');
//   var searchButton = document.getElementById('search-button');
//   // var resultsContainer = document.getElementById('results-container'); // Assuming you have a container for displaying results

//   // Add a click event listener to the search button
//   searchButton.addEventListener('click', async function() { // Mark the function as async

//     // Get the value from the search box
//     var searchTerm = searchBox.value;

//     // Make an API request to the Python backend
//     const response = await fetch(`/click?query=${searchTerm}`); // Fix the template literal
//     const data = await response.json();

//     // Make an API request to the Flask backend
//   fetch("/search", {
//     method: "POST",
//     headers: {
//         "Content-Type": "application/x-www-form-urlencoded",
//     },
//     body: sequence=${encodeURIComponent(sequence)},
// })
// .then(response => response.json())
// .then(data => {
//     // Process and display the API response on your webpage
//     const resultsContainer = document.getElementById("results-container");
//     resultsContainer.innerHTML = JSON.stringify(data, null, 2);
// })
// .catch(error => console.error("API request error:", error));
// }


//     // Process and display the API response on your webpage
//     resultsContainer.innerHTML = JSON.stringify(data, null, 2);

    

//     // Do something with the search term (e.g., display it)
//     alert('You searched for: ' + searchTerm);

//     // You can also perform an AJAX request to fetch data based on the search term
//     // For simplicity, we're just showing an alert in this example
//   });
// });
/*document.addEventListener('DOMContentLoaded', function() {
  var searchBox = document.getElementById('search-box');
  var searchButton = document.getElementById('search-button');
  var resultsContainer = document.getElementById('results-container'); // Assuming you have a container for displaying results

  // Add a click event listener to the search button
  searchButton.addEventListener('click', async function() { // Mark the function as async
    // Get the value from the search box
    var searchTerm = searchBox.value;

    // Sending a variable from JavaScript to Python

// $.ajax({
//   type: "POST",
//   url: "/receive_data", // This endpoint will be handled by your Flask app
//   data: JSON.stringify(searchTerm),
//   contentType: "application/json",
//   success: function(response) {
//     console.log("Response from Python:", response);
//     // Handle the response from Python here
//   },
//   error: function(error) {
//     console.error("Error:", error);
//   }
// });

    // try {
    //   // Make an API request to the Python backend
    //   const response = await fetch(`/click?query=${searchTerm}`); // Fix the template literal

    //   if (!response.ok) {
    //     throw new Error('Network response was not ok');
    //   }

      // const data = await response.json();

      // // Process and display the API response on your webpage
      // resultsContainer.innerHTML = JSON.stringify(data, null, 2);

      // // Do something with the search term (e.g., display it)
      // alert('You searched for: ' + searchTerm);

      // You can also perform an AJAX request to fetch data based on the search term
      // For simplicity, we're just showing an alert in this example
    // } catch (error) {
    //   console.error('API request error:', error);
    // }
  });
});

  

*/
           