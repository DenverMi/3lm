### How to run the scripts:

## Regenerating the RAG
- Execute these commands in order:

    python -m app.ingest

    python -m app.chunk

    python -m app.embed_store


## How to run the RAG in the bash
- Execute these commands

    python -m app.retrieve "You're question here?"

    python -m app.answer "You're question here?"


## How to run Streamlit GUI
- Execute this command:

    streamlit run streamlit_app.py


## How to run PDF to MD converter (PyPuPDF4LLM)
- Execute this script in the bas:

    python scripts/pdf_to_md.py "/path/to/QPRD.pdf"


## How to run HTML to MD converter (pandoc)
- Execute this script in the bash:    

    python scripts/html_to_md.py "data/bluetooth/policies/QPRD.html"

## How to clean-up the json email threads
- Execute the following script in the bash:

    For one file:
    python -m app.thread_json_to_readable_md "data/bluetooth/email_threads/thread_0057.json"

    For the whole folder:
    python -m app.thread_json_to_readable_md "data/bluetooth/email_threads"

    For the whole folder while saving in a new folder:
    python -m app.thread_json_to_readable_md "data/bluetooth/email_threads" -o "data/bluetooth/email_threads_readable"


## How to Clean-up the markdown document
- Execute this script in the bash:

    python scripts/clean_md.py "data/bluetooth/policies/QPRD.md"


## How to Clean-up a whole folder of markdown documents
- Execute this script in the bash:

    python scripts/clean_md.py "data/bluetooth/reference"


## How to move in .venv312 mode
- Execute these commands in the bash:

    cd 3lm
    source .venv312/bin/activate

## How to convert extract email threads and convert them into json file
- Execute these commands in the bash:

    python -m app.extract_threads "data/bluetooth/email/bqc.mbox"
    or
    python -m app.extract_threads "archive/email_exports/some_thread.eml"
    or
    python -m app.extract_threads "archive/email_exports/"

## When restarting a session, give this instruction:

    Before we start, let's set the ground rules:
    
    To save time, space and resources, let's do proceed one step at a time. I can't follow too many instructions/tasks all at once. So limit your instructions on what we're doing at hand. 
    
    Don't give too many instructions in one reply. One instructions first, I do it, and then next. 
    
    If there are codes to be edited, you can give me multiple instructions, but if it's too many, I want you to give it to me in parts or I want you to edit the code file yourself or give me instructions to do edit it one at a time. 
    
    Don't assume. If you're not sure about our code base, you should ask me to paste it or attach it (which ever you prefer) before attempting to revise it. 
    
    You may give suggestions, but not too many at once that I can't decide which one to do first. 
    
    Do not try to cheat or build a short cut that will not help our RAG system overall and in the long term. And please don't waste my time, since I don't have much to spend.
    
    Do you understand? 