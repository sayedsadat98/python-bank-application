# Simple Bank Application

This repository contains a simple bank account application implemented in Python. The application allows users to **create** a bank account, **deposit** funds, **withdraw** funds, and **check** the account balance. It also includes a suite of tests written using `pytest` to ensure the functionality of the application.

## Features

- Create a bank account with an initial balance.
- Deposit funds into the account.
- Withdraw funds from the account.
- Check the current balance of the account.
- Raise errors for invalid operations, such as depositing negative amounts or withdrawing more than the available balance.

## Installation

1. **Clone the Repository**:
   ```bash
   git https://github.com/sayedsadat98/python-bank-application/tree/main
   cd python-bank-application
   ```
2. Set Up a Virtual Environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install Dependencies:
    ```bash
     pip3 install -r requirements.txt
   ```

## Usage

1. Run the Application:
The main application code is in **main.py**. There is a demo code and you can run it directly to see the bank account operations
   ```bash
   python3 main.py
   ```

2. Run the tests:
Use `pytest` to run the test suite and verify the functionality.
   ```bash
   pytest
   ```
