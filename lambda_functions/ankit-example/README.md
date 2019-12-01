# Initial Setup
Required to have python3, pip, npm, and aws-cli pre-installed and configured. See directions below to set up AWS CLI.
If utilizing packages such as Pandas or NumPy then Docker is also required.

Make sure you have the following things installed before proceeding:
* Python 3.7
* Node.js
* Docker (If building numpy, pandas, or other packages with C dependencies)
* Serverless CLI
* serverless-python-requirements (install on NPM)
* Pipenv

## Configuring AWS CLI
To download visit: https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html
To configure visit: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration   
To get your API key and secret:
1. Sign in to your AWS account using IAM (directions in Slack)
2. Click on your username @ account_id
3. Click on "My Security Credentials"
4. Click "Create Access Key"
5. Copy and paste when prompted after running `aws configure`

## Developing
We will be using pipenv, best new alternative to virtualenv and anaconda.
Run `pipenv shell` to create your virtual environment tied to this lambda project.
In order to install new dependencies just run `pipenv install` instead of pip

## Deploying
Run `sls deploy` to push your function to AWS. This is using the specs in the serverless.yml config file.
Edit the event.json file and put inside the data you want for your test event.
Run `sls invoke -f <function-name> -p event.json` to run your function on AWS and see the output.
