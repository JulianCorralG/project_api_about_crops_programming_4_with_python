# project_api_about_crops_programming_4_with_python
Project Description:
This Python project provides a streamlined interface for querying and analyzing agricultural data. It leverages the Socrata API to retrieve agricultural data based on user-defined parameters such as department, municipality, and crop type. The retrieved data is then cleaned, and key edaphic variables, including pH, phosphorus, and potassium, are analyzed to calculate medians. The project consists of three modules: main, ui_section, and api_section, each serving a specific purpose in the data retrieval and analysis process.

# Agriculture Data Analysis

Welcome to the Agriculture Data Analysis project! This Python-based tool simplifies the process of querying and analyzing agricultural data. It connects to the Socrata API to fetch agricultural data based on user-specified parameters, such as department, municipality, and crop type. The retrieved data is then cleaned and used to calculate medians for essential edaphic variables like pH, phosphorus, and potassium.

## Table of Contents
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Modules](#modules)

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.x
- Socrata API key (if querying a different dataset)

### Installation

1. Clone this repository to your local machine using:
https://github.com/JulianCorralG/project_api_about_crops_programming_4_with_python.git

3. Navigate to the project directory:
cd project_api_about_crops_programming_4_with_python


### Usage

1. Run the main script to start the data analysis tool:
python main_section/main.py


2. Follow the prompts to enter your query parameters (department, municipality, crop type, and limit).

3. View the cleaned data and computed medians for edaphic variables.

## Modules

- `main_section/main.py`: The main entry point of the application.
- `ui_section/ui.py`: Handles user input and presentation.
- `api_section/api.py`: Manages data retrieval from the Socrata API and data manipulation.


   
