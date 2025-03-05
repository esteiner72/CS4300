### AI Use
OpenAI GPT-4-turbo was used for debugging & testing code fixes, in specific it was mostly used while I was trying to debug css & routing problem

### Requirements
To be blunt, the project does not fully meet requirements and is not visually appealing. I spent most of my time trying to fix the css issues and eventually gave up and cut my losses to focus on the other parts of the project. API endpoints are functional and can be navigated to from the homepage, serializers are setup, all three models work, and POST/GET are functional for each of the models when you navigate to those pages. However, for some reason the devedu app website does not work while navigating to API endpoints, but it works perfectly within the editor on port 3000 and port 8000. If you would like to test either, the turn-in has the following setting changed to 3000 but works on 8000 too.
'''
FORCE_SCRIPT_NAME = '/proxy/3000'
'''
And of course, all code is in my devedu.
