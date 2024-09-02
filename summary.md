# Generator Sinusoid Binaural
 
## Overview
The Generator Sinusoid is a Django application designed to generate and visualize sine waves. This project demonstrates the integration of Django with Matplotlib to create dynamic plots that can be viewed in a web application.

## Features
- **Sine Wave Generation:** Generates a sine wave with a user-specified frequency. Optionally, it can generate a binaural sine wave.
- **Dynamic Plotting:** Uses Matplotlib to create and display the sine wave plot within the web application.
- **Audio Generation:** Generates a WAV audio file of the sine wave.
- **Binaural Option:** Allows the generation of binaural sine waves for enhanced audio effects.

## Key Files and Their Roles
- `sinusoid/urls.py`: Defines the URL patterns for the application.
- `sinusoid/views.py`: Contains the view logic to generate and display the sine wave plot and audio.
- `sinusoid/templates/index.html`: The HTML template for rendering the plot and audio.
- `generator_sinusoid/urls.py`: Includes the URL configurations for the entire project.
- `settings.py`: Main configuration settings for the Django project.

## Technical Details
- **Wave Generation:** The `generate_sine_wave` function is used to create the wave data. It generates the time series (`t`) and the corresponding wave values (`x`). If the binaural option is selected, it uses Csound to generate a binaural sine wave.
- **Plot Generation:** Matplotlib is used to create a plot of the sine wave. The plot includes labels for the x-axis (time in seconds) and the y-axis (amplitude), and a title.
- **Plot Rendering:** The plot is saved to a buffer in PNG format and encoded in base64 to be displayed as an image in the HTML template.
- **Audio Generation:** The `scipy.io.wavfile` library is used to generate a WAV audio file of the sine wave, which is then encoded in base64 to be played in the browser.

## Getting Started
To run the Sinusoid Project locally, follow these steps:

- Clone the repository:

**git clone https://github.com/MikyMikeMusic/Django.git**
**cd your-repository**


- Run the migrations:

```python manage.py migrate```

- Start the development server:
  
```ython manage.py runserver```

- Access the application: Open your web browser and navigate to `http://127.0.0.1:8000/sinusoid/`.

## Example Usage

- The application allows the user to input a frequency and optionally select a binaural option. It will generate and display a plot of the sine wave with the specified frequency. Additionally, the user will be able to listen to the generated sine wave audio
  

  
