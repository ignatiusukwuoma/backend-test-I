## Back-end Developer Test

### Devcenter Backend Developer Test I

The purpose of this test is not only to quickly gauge an applicant's abilities with writing codes, but also their approach to development.

Applicants may use whatever language they want to achieve the outcome.

## Task

Build a bot that extracts the following from people’s Twitter bio (on public/open accounts), into a Google spreadsheet:

* Twitter profile name 
* Number of followers

Target accounts using either of these criteria:
* Based on hashtags used
* Based on number of followers; Between 1,000 - 50,000

The bot is suppose to maintain a session and continously listen to the predefined hashtag

## Language
* Python 3.6.3

## Installation
Follow the steps below to install the application

1. Clone the repository from a terminal `git@github.com:ignatiusukwuoma/backend-test-I.git`

2. Navigate to the project directory `cd backend-test-I`

3. Create a `.env` file and copy the content of `.env.sample` into it. Provide a valid email in CLIENT_EMAIL 
and choose a SPREADSHEET_NAME. Information to obtain other values is provided below.

## Setup
To setup the application and get it ready to run, you will need to follow the instructions in
Twitter Setup and Google Spreadsheets Setup below.

### Twitter Setup

1. Create a New Twitter Account if you don't have one `https://twitter.com`

2. Visit `https://apps.twitter.com/` and click on `Create New App`

3. Complete the form to create a Twitter Application

4. Navigate to the `Keys and Access Tokens` tab to find your Consumer Key and Consumer Secret

5. Click on `Create my access token` at the base of the page to obtain your Access Token and Access Token Secret

6. Enter these values into the appropriate keys in your `.env`

### Google Spreadsheets Setup

1. Go to Google API Console `https://console.developers.google.com`

2. Create a New Project

3. Click on `Enable APIs and Services`, search for and enable Google Sheets API and Google Drive API

4. Go to `Credentials` and click `Create credentials` > `Service account key`

5. Select New service account and complete the form. For Role, select `Project` > `Owner`

6. Save the Private Key to your project root directory as `client_secret.json`

## Run the app
Before running the app: 

* Create a virtual environment and activate it
```commandline
python3 -m venv twitterly_env
source twitterly_env/bin/activate
```
Ensure to install requirements and run the test so you can be sure there are no issues.

* Install the project requirements 
```commandline
pip3 install -r requirements.txt
```

* Run the tests
```commandline
python3 -m unittest -v tests.test_bot tests.test_sheet
```

* Run the application
```commandline
python3 bot.py
```

## How to complete the task

1. Fork this repository into your own public repo.

2. Complete the project and commit your work. Make a screencast of how it works with the googlespread sheet and progam side-by-side. Please watch this sample video to see what your screencast should look like https://youtu.be/mwBqUUtBtlE

3. Send the URL of your own repository and the screencast to @kolawole.balogun on the Slack here bit.ly/dcs-slack.

## Show your working

If you choose to use build tools to compile your CSS and Javascript (such as SASS of Coffescript) please include the original files as well. You may update this README file outlining the details of what tools you have used.

## Clean code

This fictitious project is part of a larger plan to reuse templates for multiple properties. When authoring your CSS ensure that it is easy for another developer to find and change things such as fonts and colours.


## Good luck!

We look forward to seeing what you can do. Remember, although it is a test, there are no specific right or wrong answers that we are looking for - just do the job as best you can. Any questions - create an issue in the panel on the right (requires a Github account).


## Demo
![screen shot](https://user-images.githubusercontent.com/8668661/33088863-330b4250-ceef-11e7-9e9c-b4fd9ca299d8.gif)
