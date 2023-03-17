<a name="readme-top"></a>
[![python](https://img.shields.io/badge/python-3.11.2-blue.svg)](https://www.python.org/downloads/) 
[![selenium](https://img.shields.io/badge/selenium-v4.8.2-green.svg)](https://pypi.org/project/selenium/)
[![status](https://img.shields.io/badge/status-stable-green.svg)](https://github.com/lukachrk/selenium-project)



## About The Project
selenium gui automatization project for automating manual test cases for awork.ge website

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Getting Started
To get a local copy up and running follow these steps.

### Prerequisites
* Python v3.10+
* Chrome browser v: 111+
* Chrome webdriver v:111.0.5563.64 https://chromedriver.storage.googleapis.com/index.html?path=111.0.5563.64/

### Installation
 
1. clone the repository git clone lukachrk/selenium-project
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
head to testcases/Auth_Test.py and on the line 10, change the path to your chrome driver location!

for the time being, test cases are written only for authorization only

open up cmd, type: `python main.py`

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Roadmap

- [ ] Add test cases for the main page components
- [ ] Add test cases for the profile page components
- [ ] add the ability to automatically detect chrome webdriver


<p align="right">(<a href="#readme-top">back to top</a>)</p>
