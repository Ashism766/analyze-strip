## Analyze Strip [live](https://strip-analysis-modified.onrender.com/)
It's an Appilication which analyze [urine strip](https://en.wikipedia.org/wiki/Urine_test_strip) and show the RGB value of them in frontend.

After going to homepage you can upload your urine strip photo in jpeg, png format, later on click submit it'll show the RGB value of this strip.

## Usages
1. It can be widely used in medical field, because it'll able to indentify more color than a normal human being.
2. The labels (RGB values) can be used for machine learning model training to obtain accurate results about the patient's disease.

## Installation and Enviroment setup for local running

1. Clone the repository.
```bash
  git clone https://github.com/Ashism766/analyze-strip.git
```
2. Create virtual environment.
```bash
  cd mail-bot-ashis
  python -m venv venv
  cd venv
```
Activate the virtual enviroment
windows 
```bash
    ./Script/activate
    cd ..
```
For linux
```bash
    source ./bin/activate
    cd ..
```
3. Install the dependecies.

For installing dependencies use the below command
```bash
    pip install -r requirements.txt
```

4. Start the server

```bash
    python main.py
```
