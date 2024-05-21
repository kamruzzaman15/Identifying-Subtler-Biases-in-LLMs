# Paper
This work has been accepted at ACL 2024. You can find the paper related to this work https://arxiv.org/abs/2309.08902

# How to run

Running this project consists of three different steps.
- Creating the dataset
- Evaluating the dataset with different large language models
- Generating report for the output of each model

## Install necessary dependencies
To run the project, you need to install some necessary dependencies first. For that we will be using virtual environment.

- Create and activate virtual environment (for more info on virtual environment: https://docs.python.org/3/library/venv.html)
- Install the dependencies using the requirements.txt file with the following command: `pip install -r requirements.txt`

## Create dataset
Creating the dataset is straightforward. All you need to do is to run the following command: `python3 create_dataset.py`.
This file looks for the input json files inside `input_attributes` and finally creates the dataset combining all the data from the input_attributes directory. Once done, it stores the output dataset in the `outputs/dataset.csv` file.

## Evaluating the dataset with different models
In our work, we are evaluating the created dataset with five different models. They are:
- GPT-3.5
- GPT-4
- Google PALM 2 and 
- Llama-2 13B
- Mistral 7B

We have four different script for evaluating these models against our created dataset. All of them look for our created dataset inside outputs directory, evaluate the specific model with out dataset and finally creates two csv files (valid response and invalid response) for each model. They will also be stored in the outputs directory just like the dataset. The valid response denotes that the response that we got from the model matches with one of our provided options, while an invalid response means the opposite.

To run a model, you need to execute the specific file for that model. For example, to run the model for googlepalm, you need to run `python3 googlepalm.py` and so on.

## Generate reports

This file generates different reports from the output of a specific model that denotes the overall performance of that model. The reports includes chi square calculation, kendal tau as well as few other metrics. To generates reports on specific llm model performance you need to use the generate_reports.py file along with specifying the input file for that particular model. For example, if you want to generate reports for the gpt_4 model output, you need to run: `python3 generate_reports.py gpt_4_valid.csv`. Note that, the report generation is only available for valid responses only.

## Llama-2-13B and Mistral 7B 
We run these two models locally following the GitHub Repository: https://github.com/genelkim/local_llm_demos
