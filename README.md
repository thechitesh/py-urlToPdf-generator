# A simple python library to generate pdf document by passing the url
This is simple python library which helps in generating pdf from the url. 
The movitvation of the project is to make a server side pdf rendering there are nice tools available with node.js and phantomjs but since in real world scenario node.js is not always installed on the server machines and also have compatibility issue and phantomjs is going out of support. So, python comes to rescue as python comes installed by default with all linux machine. And this py-urlToPdf-generatore libarray works with python2 as well as python3.

## Add virtual environment
    python -m venv venv
## Activate virtual environment
    windows :- venv\Scripts\activate.bat (from cmd)
            :- venv\Scripts\Activate.ps1 (from powershell)
    Mac     :- source venv\bin\activate

    To activate the venv simply type 'deactivate'
## Now install all requirements for the project
    python install -r requirements.txt

Download chromedriver from the path :- https://chromedriver.chromium.org/downloads

### Command to run

'python get_pdf http://google.com output.pdf'

