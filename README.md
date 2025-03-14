# DishVision AI 🍽️

An AI-powered application that analyzes food images to identify dishes, list ingredients, and provide step-by-step recipes.

## Features 🌟

- Upload images or capture them using your camera
- AI-powered dish detection
- Detailed ingredient lists with quantities
- Step-by-step cooking instructions
- Modern and intuitive user interface
- Robust error handling and logging

## Project Structure 📁

```
DishVision/
├── src/
│   ├── components/      # UI components
│   ├── services/        # Model and business logic
│   ├── utils/          # Utility functions and logging
│   ├── config/         # Configuration files
│   └── app.py          # Secondary entry point
├── logs/               # Application logs
├── tests/             # Test files
├── main.py            # Main entry point
└── requirements.txt    # Project dependencies
```

## Setup 🚀

1. Clone the repository:
```bash
git clone <repository-url>
cd DishVision
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Get your API key:
- Visit [Google AI Studio](https://aistudio.google.com/)
- Sign in and generate your API key

## Running the Application 🏃‍♂️

1. Make sure you're in the project root directory

2. Run the Streamlit app:
```bash
streamlit run main.py
```

3. Open your browser and go to the URL shown in the terminal (usually http://localhost:8501)

4. Enter your Google AI Studio API key in the sidebar

5. Start analyzing dishes! 🎉

## 📸 Screenshot
![DishVision AI Screenshot](screenshots/img.png)  

## Contributing 🤝

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details. 