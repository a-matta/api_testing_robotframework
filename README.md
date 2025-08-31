# api_testing_robotframework

A short description of the project

---

*Documentation**: [https://a-matta.github.io/api_testing_robotframework](https://a-matta.github.io/api_testing_robotframework)

**Source Code**: [https://github.com/a-matta/api_testing_robotframework](https://github.com/a-matta/api_testing_robotframework)

---

## Development

* Requirements:
  * [Poetry](https://python-poetry.org/)
  * Python 3.12+
  * [Install Allure Report](https://allurereport.org/docs/install/)
* Clone this repository
* Create a virtual environment and activate it
  ```sh
  poetry shell
  ```
* Install the dependencies
  ```sh
  poetry install
  ```
* Install playwright dependencies
  ```sh
  playwright install
  ```
* Running the tests
  ```sh
  # Uses PyInvoke
  inv tests
  ```
* To view the allure reports.
  ```sh
  allure serve allure-results
  ```

---

This project was generated using the [playwright-python-cookiecutter](https://github.com/a-matta/playwright-python-cookiecutter) template.
