# Cat vs Dog Classifier

This project is a web application that classifies images of cats and dogs using a pre-trained MobileNetV2 model. The application allows users to upload an image, and it predicts whether the image contains a cat or a dog.

## Table of Contents
- [Cat vs Dog Classifier](#cat-vs-dog-classifier)
  - [Table of Contents](#table-of-contents)
  - [Technologies](#technologies)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Technologies
- Python
- Flask
- TensorFlow
- Keras
- HTML/CSS

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
2. Open your web browser and go to http://127.0.0.1:5000/.
3. Upload an image of a cat or a dog, and the model will classify it for you.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you'd like to contribute to the project.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.