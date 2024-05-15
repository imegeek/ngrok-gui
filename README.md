# ngrok-gui

ngrok-gui is a Python-based graphical user interface for ngrok, making it easier to create secure tunnels.

## Features

- **User-friendly interface**: Simple and intuitive GUI to create ngrok tunnels.
- **Multi-platform support**: Works on Windows, macOS, and Linux.
- **Easy setup**: Quick and straightforward installation process.

## Prerequisites

- Python 3.x
- ngrok account and API key
- Tkinter library for the GUI (usually included with Python installations)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/imegeek/ngrok-gui
    cd ngrok-gui
    ```

2. **Install the required Python libraries:**

    ```sh
    pip install psutil
    ```

3. **Download ngrok and place it in your PATH:**

    - Download ngrok from [ngrok.com](https://ngrok.com/download)
    - Extract it and place the executable in a directory included in your system's PATH

## Configuration

1. **Set your ngrok authtoken:**

    - Obtain your ngrok authtoken from the [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken).
    - Run the following command to authenticate ngrok with your account:

      ```sh
      ngrok authtoken <your-authtoken>
      ```

## Usage

1. **Run the application:**

    ```sh
    python main.py
    ```

2. **Using the GUI:**

    - Open the application.
	- Choose http/tcp protocols.
    - Enter the port number you want to expose.
    - Click on the "Create Tunnel" button to create a tunnel.
    - The GUI will display the public URL generated by ngrok.

## Screenshots

<div align="center">
<img src="https://github.com/imegeek/ngrok-gui/assets/63346676/3cdd25ae-26cb-440b-8abe-34955cb783be" alt="ngrok-gui screenshot">
</div>

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/imegeek/ngrok-gui/blob/master/LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of ngrok for creating such a useful tool.
