/**
 * Updates the current color, distance and motor status calling
 * the corresponding methods.
 */

function updateStatus() {
    // Update current color based on Open CV

    (async () => await updateCurrentColorOpenCV())();
    // Update motor status
    //...

    // Update current color based on OpenCV
    (async () => await updateCurrentColorDistance())();
    //...

    // Update current distance
    (async () => await updateDistance())();
    //...

}

/**
 * Update the current color based on OpenCV.
 */
async function updateCurrentColorOpenCV() {
    try {
        // Request color from server
        const requestResult = await requestColorFromOpenCV()
        // Get the HTML element where the status is displayed
        const blue_open_cv = document.getElementById('blue_open_cv')
        blue_open_cv.innerHTML = requestResult.data[0]
        const purple_open_cv = document.getElementById('purple_open_cv')
        purple_open_cv.innerHTML = requestResult.data[1]
        const yellow_open_cv = document.getElementById('yellow_open_cv')
        yellow_open_cv.innerHTML = requestResult.data[2]
        const green_open_cv = document.getElementById('green_open_cv')
        green_open_cv.innerHTML = requestResult.data[3]

    } catch (e) {
        console.log('Error getting the color based on OpenCV', e)
        updateStatus('Error getting the color based on OpenCV')
    }
}

/**
 * Function to request the server to update the current
 * color based on OpenCV.
 */
function requestColorFromOpenCV() {
    try {
        // Make request to server
        return axios.get('/get_color_from_opencv')
    } catch (e) {
        console.log('Error getting the status', e)
        updateStatus('Error getting the status')

    }
}


/**
 * Function to request the server to start the motor.
 */
function requestStartMotor() {
    //...
    axios.get('/start_motor')
}


/**
 * Function to request the server to stop the motor.
 */
function requestStopMotor() {
    //...
    axios.get('/stop_motor')
}

/**
 * Update the status of the motor.
 * @param {String} status
 */
function updateMotorStatus(status) {
    // Get the HTML element where the status is displayed
    // ...
    const motorStatusElement = document.getElementById('motor_status_info');
    motorStatusElement.innerHTML = status;
}

/**
 * Update the current color based on distance sensor.
 */
async function updateDistance() {
    try {
      const requestResult = requestDistance()
    } catch (e) {
      console.log('Error getting the distance', e)
      updateStatus('Error getting the distance')
    }
  }


/**
 * Function to request the server to get the distance from
 * the rod to the ultrasonic sensor.
 */
async function requestDistance () {
    //...
    try {
      // Make request to server
      let result = await axios.get('/get_distance')
      let distance = document.getElementById("Distance")
      distance.innerText = result.data.distance
    } catch (e) {
      console.log('Error getting the distance request', e)
      updateStatus('Error getting the distance request')
    }
  }


/**
 * Update the current color based on distance sensor..
 */
async function updateCurrentColorDistance() {
    try {
      // Request color from server
      const requestResult = await requestColorFromDistance()
      // Get the HTML element where the status is displayed
      const blue_distance = document.getElementById('blue_distance')
      blue_distance.innerHTML = requestResult.data[0]
      
      const purple_distance = document.getElementById('purple_distance')
      purple_distance.innerHTML = requestResult.data[1]

      const yellow_distance = document.getElementById('yellow_distance')
      yellow_distance.innerHTML = requestResult.data[2]

      const green_distance = document.getElementById('green_distance')
      green_distance.innerHTML = requestResult.data[3]
      
    } catch (e) {
      console.log('Error getting the color based on distance', e)
      updateStatus('Error getting the color based on distance')
    }
  }


/**
 * Function to request the server to get the color based
 * on distance only.
 */
function requestColorFromDistance() {
    try {
      // Make request to server
      return axios.get('/get_color_from_distance')
    } catch (e) {
      console.log('Error getting the status', e)
      updateStatus('Error getting the status')
    }
  }

function requestMotorStatus() {
    axios.get('/motor_status')
      .then(response => {
        const status = response.data.success ? 'Motor Running' : 'Motor Stopped';
        updateMotorStatus(status);
      })
      .catch(error => {
        console.log('Error getting the motor status', error);
        updateStatus('Error getting the motor status');
      });
  }