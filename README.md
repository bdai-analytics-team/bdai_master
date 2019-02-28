# bdai_master
## Overview
BDAI's repo containing all code ready to be deployed. 
Miniconda (lighteweight Anaconda) environments will be used for managing and isolating Python and R dependencies.
Docker will be used to containerize the high-level divisions of pipeline, analysis, and application.
Docker Compose will be used at the top level to manage the containers beneath it.

This repository is for scripting and deployable code.  Notebooks, data, and random files don't belong in this repository.
File and directory structure is completely up to your best judgement, though I may come through and clean up once in a while.  Script naming convention will be snake-case, e.g. my_python_script.py or analysis_results.R

## Repository Structure
The master branch will solely be for deployed code.  The dev branch is for code that is waiting to be approved and other small fixes that don't require a full deployment. 

Each feature will require a new branch to be made.  For example, if I was going to work on the Stock data Websockets implementation I would take the following steps:
1. Start a branch called "StockWebsockets"
2. Work on my code and make sure it is solid
3. Create a pull request into dev
4. Have someone else review my pull request
5. Merge my code into dev
6. Wait for dev to be periodically be merged into master
