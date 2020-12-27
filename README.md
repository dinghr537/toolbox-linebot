# TOC LineBot

### Prerequisite
* Python 3.6
* conda
* google translate api
* HTTPS Server
* latex

#### Install Dependency
```sh
# after install Miniconda or Anaconda
conda create --name line python=3.6
conda deactivate
conda activate line
conda install pygraphviz
# install latex
sudo apt-get install texlive-full

pip install -r requirements.txt
```


#### Secret Data
Please modify  `.env` file to set Environment Variables refer to TA's `.env.sample`.
`LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` **MUST** be set to proper values.
Besides, you need another json file for google cloud translation api's authorization. And remember to set the path of the json file in `.env`.


### Finite State Machine
![fsm](./fsm.png)

### Usage
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

---

### Deploy

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

Then Run the app

```sh
python app.py
```

#### deploy it on the GCP Virtual Private Server

首先需要有一個自己的域名（買也好，嫖也好，總之是要有一個）

然後設定DNS解析將域名解析到你的server的ip

之後用GitHub上的`acme.sh`從letsencrypt生成證書。

> https://github.com/acmesh-official/acme.sh

之後從GitHub將repo clone下來，按照 Install Dependency 進行環境準備

然後進到`app.py `裡，將`URL`修改為你的域名，並在最下面運行處設定端口，以及之前的`xxx.crt`&`xxx.key` .

之後讓其在背景運行即可可以使用gunicorn，也可以用nohup之類的，隨意就好