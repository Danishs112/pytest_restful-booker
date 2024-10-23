# Pytest API Framework

## Problem Solved

This test automation solution is a POC that needs to be implemented. The Application Under Test(AUT) for this POC is Restful Booker portal [https://restful-booker.herokuapp.com/apidoc/](https://restful-booker.herokuapp.com/apidoc/)

## Scenarios Covered

1. Generate 3 new bookings --> Log below scenarios to a log file
   - All available booking IDs 
   - Above added 3 new booking details
   
2.  Modify the total price for test1 to 1000 and test2 to 1500. Log this data to the same log file.

3. Delete one of the booking --> Log return status to the same file

4. Present the data in the log file as html report.

## Setup
 
- Clone this repo
- Navigate to project folder
- Open CLI
- Configure a virtual environment
- Run the below command to install the requirements for this project
    ```sh
        pip3 install -r requirements.txt
   ```

- Run the below the command to run all code
  ```sh
    pytest --html=report.html --self-contained-html --capture=tee-sys
  ```
