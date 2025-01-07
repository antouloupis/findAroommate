function cleanURL(event) {
    event.preventDefault();  // Prevent default form submission
    
    const filterForm = event.target;  // Get the form element from the event
    const formData = new FormData(filterForm);
    const params = new URLSearchParams();
    
    // Iterate over form data and add only the non-empty entries to params
    for (let [key, value] of formData.entries()) {
        if (value) {
            params.append(key, value);
        }
    }
    
    // Construct the cleaned URL
    const cleanedURL = `${filterForm.action.split('?')[0]}?${params.toString()}`;
    
    // Redirect with the cleaned parameters
    window.location.href = cleanedURL;
}

function validateRoommates(input) {
    restrictToNumbers(input);
    let value = parseInt(input.value, 10);

    if (value < 1) {
        input.value = 1; // Set to minimum
    } else if (value > 10) {
        input.value = 10; // Set to maximum
    }
}

function validateBathrooms(input) {
    restrictToNumbers(input);
    let value = parseInt(input.value, 10);

    if (value < 1) {
        input.value = 1; // Set to minimum
    } else if (value > 10) {
        input.value = 10; // Set to maximum
    }
}

function validateSize(input) {
    restrictToNumbers(input);
    let value = parseInt(input.value, 10);

    if (value < 15) {
        input.value = 15; // Set to minimum
    } else if (value > 500) {
        input.value = 500; // Set to maximum
    }
}

function validatePrice() {
    const minInput = document.getElementById("id_price_min");
    const maxInput = document.getElementById("id_price_max");

    // Get values as integers or default to null
    let minPrice = minInput.value === "" ? null : parseInt(minInput.value, 10);
    let maxPrice = maxInput.value === "" ? null : parseInt(maxInput.value, 10);

    // If only min price is filled
    if (minPrice !== null && maxPrice === null) {
        if (minPrice < 15) {
            minInput.value = 15; // Set to minimum allowed value
        } else if (minPrice > 4998) {
            minInput.value = 4999;
        }
    }

    // If only max price is filled
    if (minPrice === null && maxPrice !== null) {
        if (maxPrice > 5000) {
            maxInput.value = 5000; // Set to maximum allowed value
        } else if (maxPrice < 15){
            maxInput.value = 15;
        }
    }

    // If both min and max prices are filled
    if (minPrice !== null && maxPrice !== null) {
        if (minPrice < 15) {
            minInput.value = 15; // Set min price to minimum allowed value
            minPrice = 15;
        }

        if (maxPrice > 5000) {
            maxInput.value = 5000; // Set max price to maximum allowed value
            maxPrice = 5000;
        } else if (maxPrice < 16) {
            maxInput.value = 16;
            maxPrice = 16;
        }

        if (minPrice >= maxPrice) {
            if (maxPrice < 16) {
                maxInput.value = 16;
                maxPrice = 16;
            }
            minInput.value = maxPrice - 1; // Adjust min to be 1 less than max
        }
    }
}

function validateFloor() {
    const minInput = document.getElementById("id_floor_min");
    const maxInput = document.getElementById("id_floor_max");

    let minFloor = minInput.value === "" ? null : parseInt(minInput.value, 10);
    let maxFloor = maxInput.value === "" ? null : parseInt(maxInput.value, 10);

    // If only min price is filled
    if (minFloor !== null && maxFloor === null) {
        if (minFloor < -2) {
            minInput.value = -2; // Set to minimum allowed value
        } else if (minFloor > 15) {
            minInput.value = 15;
        }
    }

    // If only max price is filled
    if (minFloor === null && maxFloor !== null) {
        if (maxFloor > 15) {
            maxInput.value = 15; // Set to maximum allowed value
        } else if (maxFloor < -2){
            maxInput.value = -2;
        }
    }

    // If both min and max prices are filled
    if (minFloor !== null && maxFloor !== null) {
        if (minFloor < -2) {
            minInput.value = -2; // Set min price to minimum allowed value
            minFloor = -2;
        }

        if (maxFloor > 15) {
            maxInput.value = 15; // Set max price to maximum allowed value
            maxFloor = 15;
        }

        if (minFloor >= maxFloor) {
            if (maxFloor < -1) {
                maxInput.value = -1;
                maxFloor = -1;
            }
            minInput.value = maxFloor - 1; // Adjust min to be 1 less than max
        }
    }
}

function restrictToNumbers(input) {
    // Replace non-numeric characters except "-" for negative values
    input.value = input.value.replace(/[^0-9\-]/g, "");

    // Ensure only one "-" is allowed and it must be at the start
    if (input.value.indexOf("-") > 0) {
        input.value = input.value.replace("-", "");
    }
}
    

