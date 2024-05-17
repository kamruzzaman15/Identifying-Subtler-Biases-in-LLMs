# Paper
You can find the paper related to this work https://arxiv.org/abs/2309.08902

## Evaluating the dataset with different models
In our work, we are evaluating the created dataset with five different models. They are:
- GPT-3.5
- GPT-4
- Google PALM 2 and 
- Llama-2 13B
- Mistral 7B

## Run the this benchmark with API Providers
### Installation 

#### 1. Create a virtual environment (Optional)

<details>
<summary>macOS and Linux</summary>

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt requirements_remote.txt
```

</details>

<details>

<summary>Windows</summary>

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt requirements_remote.txt
```

</details>

#### 2. Choose your API Provider and supported model [here](https://docs.litellm.ai/docs/providers)

Example: Groq and llama-2-70b-4096

Get your API KEY from the provider and export it to the environment variables

```bash
export GROQ_API_KEY=xxx
export MODEL=groq/llama2-70b-4096
```

**Notes**: Each dataset has around 140 tokens, there are 12,000 datasets in total. A 7B model will cost around $0.2, while a 70B model will cost around $2.

#### 3. Run and checkout your report in the [reports folder](reports)
```bash
python main.py
```

## Run this bias benchmark locally
### Installation 

#### 1. Create a virtual environment (Optional)

<details>
<summary>macOS and Linux</summary>

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt requirements_remote.txt
```

</details>

<details>

<summary>Windows</summary>

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt requirements_remote.txt
```

</details>