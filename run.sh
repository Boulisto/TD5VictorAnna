
#!/bin/bash

if [[ -d .env ]]
then
	    echo "This directory exists on your filesystem."
    else
	    python3 -m venv .env
	    source .env/bin/activate

fi

pip install -r requirements.txt


python3 main.py


