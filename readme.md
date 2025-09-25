# Mine Planning Software

Mine Planning Software is a desktop application designed to help mining engineers and planners manage, analyze, and visualize mining data efficiently. Built with Python and PyQt5, it provides a user-friendly interface for importing data and planning mining operations.

## Features

- **Home Page Dashboard:** Clean and intuitive welcome screen.
- **Data Import:** Easily import mining data files into the application.
- **Automatic Data Storage:** Imported files are saved in the `data` folder for easy access.
- **Menu Navigation:** Simple menu bar for importing data and exiting the application.
- **Extensible Design:** Modular code structure for easy feature expansion.

## Getting Started

### Prerequisites

- Python 3.7+
- [PyQt5](https://pypi.org/project/PyQt5/)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Shyam1289/mine-planning-software.git
   cd mine-planning-software
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application

```sh
python src/main.py
```

## Project Structure

```
MinePlanningSoftware/
├── data/                # Imported data files
├── src/
│   ├── main.py          # Main application script
│   └── homepage.py      # Home page UI module
├── .gitignore
├── readme.md
└── requirements.txt
```

## Usage

- Launch the application.
- Use the **File > Import Data** menu to select and import your mining data files.
- Imported files are automatically saved in the `data` folder.
- The home page displays the status of your imported data.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Screenshots

![Home Page](docs/homepage_screenshot.png)
*Home page dashboard*

---

**Developed by Shyam Sunder**