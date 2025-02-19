# Monkeyss - Monkeypox Diagnosis System

## Overview
Monkeyss is a medical diagnosis system designed to detect monkeypox from medical images using machine learning. The system provides a web interface for users to upload images and receive automated diagnosis results.

## Key Features
- Image upload and processing
- Monkeypox detection using TensorFlow and ResNet50
- Positive/Negative classification with confidence scores
- User authentication and role-based access control
- Detailed result display interface
- Medical test history tracking

## Technology Stack
- **Backend**: Django
- **Machine Learning**: TensorFlow, Keras, ResNet50
- **Image Processing**: OpenCV, NumPy
- **Frontend**: HTML, CSS, JavaScript ,React Bootstrap,

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Monkeyss.git
   ```
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start development server:
   ```bash
   python manage.py runserver
   ```

## Usage
1. Register or login to the system
2. Upload a medical image through the diagnosis interface
3. View the diagnosis results
4. Access your test history

## Contribution
We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create a new branch for your feature
3. Submit a pull request with detailed description

## License
This project is licensed under the MIT License - see the LICENSE file for details.
