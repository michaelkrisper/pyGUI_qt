# pyGUI_qt

This project is a demonstration of a simple GUI application written in Python with PyQt5. It provides a basic ID3 tag editor for music files.

## Features

*   View and edit ID3 tags (title, artist, album, year).
*   Loads UI from either a Python module or a `.ui` file.
*   Supports internationalization.

## Requirements

*   Python 3
*   PyQt5

## Installation

1.  Clone the repository:
    ```
    git clone https://github.com/your-username/pyGUI_qt.git
    ```
2.  Install the required dependencies:
    ```
    pip install PyQt5
    ```
3.  On some Linux systems, you might need to install additional Qt libraries:
    ```
    sudo apt-get update
    sudo apt-get install -y libxcb-xinerama0 libxkbcommon-x11-0 qtwayland5
    ```

## Usage

There are two ways to run the application:

1.  **Using the pre-generated UI file:**
    ```
    python3 qt_demo.py
    ```
2.  **Loading the UI dynamically from the `.ui` file:**
    ```
    python3 qt_uic_load.py
    ```

In a headless environment, you might need to set the `QT_QPA_PLATFORM` environment variable:
```
export QT_QPA_PLATFORM=offscreen
python3 qt_demo.py
```

## Building

The `Makefile` provides helpers for managing UI files and translations.

*   To regenerate the Python UI file from the `.ui` file:
    ```
    make ui
    ```
*   To update translation files:
    ```
    make translate
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
