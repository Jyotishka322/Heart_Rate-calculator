# Heart Rate Calculator using Python

## 1. Project Overview

The Heart Rate Calculator is a Python command-line project. The Heart Rate Calculator calculates a persons heart rate in Beats Per Minute (BPM) from the number of heartbeats counted and the time taken to count them. The original project formula is:

**BPM = (Number of Beats / Time in Seconds) × 60**

The Heart Rate Calculator has been extended with input validation, heart‑rate classification, JSON history storage, testing, documentation and modular Python files.

## 2. Features

- The Heart Rate Calculator takes the users name.

- The Heart Rate Calculator takes the number of heartbeats counted.

- The Heart Rate Calculator takes the measurement time in seconds.

- The Heart Rate Calculator calculates BPM using the formula.

- The Heart Rate Calculator displays the calculation.

- The Heart Rate Calculator gives a BPM range message.

- The Heart Rate Calculator handles input.

- The Heart Rate Calculator saves calculation history in JSON.

- The Heart Rate Calculator includes automated tests.

- The Heart Rate Calculator uses Python modules.

## 3. Technologies Used

- Python 3.x

- Command Line / Terminal

- JSON

- Git and GitHub

- pytest for automated testing

## 4. Project Structure

```text

│

├── heart_rate_calculator.py

├── calculator.py

├── validator.py

├── classifier.py

├── display.py

├── history.py

├── config.py

├── requirements.txt

├── README.md

├── statement.md

│

├── data/

│   └── history.json

│

├── tests/

│   ├── test_calculator.py

│   └── test_validator.py

│

└── docs/

├── system_architecture.md

├── workflow.md

├── use_case.md

├── sequence.md

├── component.md

└── storage_design.md

```

## 5. How to Run

Open a terminal in the project folder and run:

```bash

python heart_rate_calculator.py

```

Enter:

1. Your name

2. Number of heartbeats counted

3. Time in seconds

## 6. Example

```text

enter your name: xyz

hello xyz!

enter the number of heartbeats counted : 60

enter the time in seconds: 60

YOUR RESULT

name: xyz

heartbeats counted: 60

time: 60 seconds

heart rate: 60.0 BPM

```

## 7. Formula

```text

BPM = (Number of Beats / Time, in Seconds) × 60

```

Example:

```text

BPM = (60 / 60) × 60

BPM = 60 BPM

```

## 8. Testing

If pytest is installed:

```bash

pytest

```

The tests check:

- BPM calculation

- Decimal results

- /normal/high classification

## 9. GitHub

```bash

git init

git add.

git commit -m "Complete heart rate calculator project"

git branch -M main

git remote add origin YOUR_GITHUB_REPOSITORY_URL

git push -u origin

```

## 10. Limitations

- The Heart Rate Calculator depends on the accuracy of user input.

- The Heart Rate Calculator does not use a sensor.

- The Heart Rate Calculator is not a diagnostic tool.

- The BPM range message is an educational classification.

## 11. Future Enhancements

- Add a graphical user interface.

- Connect a sensor.

- Add charts.

- Add CSV export.

- Add detailed user history.