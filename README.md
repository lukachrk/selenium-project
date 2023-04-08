<a name="readme-top"></a>
[![python](https://img.shields.io/badge/python-3.11.2-blue.svg)](https://www.python.org/downloads/) 
[![selenium](https://img.shields.io/badge/selenium-v4.8.2-green.svg)](https://pypi.org/project/selenium/)
[![status](https://img.shields.io/badge/status-stable-green.svg)](https://github.com/lukachrk/selenium-project)



## About The Project
![terminal gif](https://user-images.githubusercontent.com/47860959/230725808-5da2f151-12ce-48c1-a872-2a6ae45c8482.gif)

Selenium e2e testing automation project for talent acqusition website "awork.ge"

## Backstory
This is a personal project that I've been working on since I began learning QA theory and manual testing at CommSchool. The main objective of this project is to automate the test cases I've been writing and testing manually throughout the semester and improve my automation testing skills. To achieve this goal, I selected the awork platform as my testing ground, as I use it occasionally and wanted to practice finding and reproducing bugs.

To accomplish the automation, I used several technologies, including Python and Selenium for web automation. I also utilized Rich, a library for customizing the console, to enhance the user experience.

Overall, this project has been a valuable learning experience for me, allowing me to apply the concepts I've learned in a practical setting and develop my automation testing abilities.


## Getting Started
To get a local copy up and running follow these steps.

### Prerequisites
* Python v3.10+
* Chrome browser v:111+
* Chrome webdriver v:111.0.5563.64 (included in repo)

### Installation
 
1. clone the repository
   ```sh
   git clone https://github.com/lukachrk/selenium-project
   ```
2. navigate into main folder using `cd selenium-project`

3. Create new virtual python environment
   ```sh
   python3 -m venv venv
   ```
4. Activate virtual python environment
   ```sh
   venv/bin/activate
   ```
5. Install all the libraries mentioned in requirements.txt 
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Usage
open up cmd, type: `python main.py` and provide suite number to
run one of the test suites. to test authetication or profile page 
elements, you need to provide your credentials to authorize on 
the websiter



## Roadmap

- [ ] Add test cases for the main page components
- [x] Add test cases for the profile page components
- [x] Add the ability to automatically detect chrome webdriver
- [x] Add reusable test data for different modules
- [x] Add reusable test data for different modules
- [x] Add test cases for registration
- [ ] create test suite for smoke testing
- [ ] Add test suite for regression testing


<p align="right"><a href="#readme-top">back to top</a></p>
