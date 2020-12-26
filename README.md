# TOC LineBot

### Prerequisite
* Python 3.6
* conda
* google translate api
* HTTPS Server

#### Install Dependency
```sh
# after install Miniconda or Anaconda
conda create --name line python=3.6
conda deactivate
conda activate line
conda install pygraphviz
pip install -r requirements
```




#### Secret Data
Please midify  `.env` file to set Environment Variables refer to TA's `.env.sample`.
`LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` **MUST** be set to proper values.
Besides, you need another json file for google cloud translation api's authorization. And remember to set the path of the json file in `.env`.

#### Use ngrok to run it
for mac users, use homebrew:
```sh
brew cask install ngrok
```

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever ( in your environment )

```sh
python app.py
```


## Finite State Machine
![fsm](./fsm.png)

## Usage
The initial state is set to `user`.

You have several choices: go to translate state; go to latex state; go to metaphysics state, or show fsm graph.

#### State: user

- go to **translate** state 
    - press the corresponding button or type "translate"
- go to **metaphysics** state 
    - press the corresponding button or type "metaphysics"
- go to **latex** state 
    - press the corresponding button or type "latex"
- show **fsm** graph
    - type "fsm"

#### State: translate

- go to **transToEnglish** state
    - press the corresponding button or type "trans to en"
- go to **transToMandarin** state
    - press the corresponding button or type "trans to zh"
- go to **transToRussian** state
    - press the corresponding button or type "trans to ru"
- show **fsm** graph
    - type "fsm"
- exit
    - press  the corresponding button or type "exit!!"

#### State: transToXXX

- type something and the bot will translate it to the target language.
- type "fsm" to show **fsm** graph
- type "exit!!" to **exit**.

#### State: metaphysics

- type something and the bot will give you the forecast result.
- type "fsm" to show **fsm** graph
- type "exit!!" to **exit**.

#### State latex

- type simple latex formula and the bot will give you rendered formula graph.
- type "fsm" to show **fsm** graph
- type "exit!!" to **exit**.



