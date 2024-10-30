# Cat vs Dog Classifier

This project is a web application that classifies images of cats and dogs using a pre-trained MobileNetV2 model. The application allows users to upload an image, and it predicts whether the image contains a cat or a dog.

![Upload Interface](https://pub-819e757aa3dd4d2d9806e0b097a9e4bb.r2.dev/1.png)
*Image Upload Interface: Users can easily upload their images for classification*

![Classification Result](https://pub-819e757aa3dd4d2d9806e0b097a9e4bb.r2.dev/2.png)
*Classification Result: The application displays the prediction result with confidence score*

## Table of Contents
- [Cat vs Dog Classifier](#cat-vs-dog-classifier)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies](#technologies)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Features
- Simple and intuitive web interface
- Real-time image classification
- Support for various image formats
- Confidence score display
- Pre-trained MobileNetV2 model for accurate predictions
- Responsive design for both desktop and mobile devices

## Technologies
- Python
- Flask
- TensorFlow
- Keras
- HTML/CSS
- MobileNetV2 (pre-trained model)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/elhaddajiotmane/CatDog-Classifier.git
cd CatDog-Classifier
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python app.py
```

2. Open your web browser and go to http://127.0.0.1:5000/

3. Use the application:
   - Click the "Choose File" button to select an image
   - Upload an image of a cat or a dog
   - Wait for the model to process the image
   - View the classification result and confidence score

## Contributing

Contributions are welcome! To contribute to this project:

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

Please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Created by [elhaddajiotmane](https://github.com/elhaddajiotmane)  
Connect with me on [LinkedIn](https://linkedin.com/in/elhaddaji-otmane/)
