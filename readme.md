## Author Details
- Shakti Agrawal (shaktigrwl@gmail.com)

# Steps to Set up Python-SeleniumBDD-Project

Welcome to the Python Selenium BDD Project! This project utilizes the Selenium framework with Python to automate web test cases. Additionally, it incorporates Allure reports for comprehensive and detailed test result presentations.

## Pre-requisites:

1. **Install Python:** Ensure you have the latest version of Python installed on your system.
2. **Update System Path:** Update the system path variable to allow using Python and pip commands from the command line.
3. **Download Git:** Download and install Git for version control.
4. **Clone the Project:** Clone this project by running the command: `git clone <repository_url>`
5. **Install PyCharm:** Download and install the PyCharm IDE.
6. **Import Project:** Open PyCharm and import this project.
7. **Project Setup:** With the project loaded, you're ready to start working!

## Setting up the Project:
1. Open a terminal within the project folder.
2. Run the command: `pip install -r requirements.txt`
3. Download and update the appropriate browser drivers for Chrome, Safari, Firefox, or Edge. These drivers are necessary for Selenium to interact with the browsers. Ensure the drivers are in your system's PATH.
4. Once the requirements are installed, you're all set up!

## Running the Project:

To run the project, you have several options:

1. Run the entire suite: 
`behave -D browser=chrome -f allure_behave.formatter:AllureFormatter -o Report_Json`
2. Run a single feature file:
`behave features/online_order.feature -D browser=chrome -f allure_behave.formatter:AllureFormatter -o Report_Json`
3. Run a single scenario using its tag:
`behave features/online_order.feature --tags=Login -D browser=chrome -f allure_behave.formatter:AllureFormatter -o Report_Json`
4. Run scenarios with a specific tag across all feature files:
`behave features --tags=Login -D browser=chrome -f allure_behave.formatter:AllureFormatter -o Report_Json`


## Generating Detailed HTML Report:

To generate a comprehensive HTML report:

1. Ensure Java is installed and accessible from the command line.
2. Download the latest Allure version, extract the zip, and set the system path to the bin folder.
3. Run the following command:
`allure generate Report_Json -o Report_Html --clean`
4. Navigate to the `Report_Html` folder and find the `index.html` file.
5. If viewing the report from a server, ensure the report is supported by protocol schemes: http, data, isolated-app, chrome-extension, chrome, https, chrome-untrusted.
6. For local viewing, open a command prompt inside the `Report_Html` folder and create a simple HTTP server: `python -m http.server 8080`
7. Access the report in your browser at `http://localhost:8080`.

Enjoy the automation journey with your Python Selenium BDD project and the rich Allure reports!
