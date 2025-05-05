For the installation of AutoGen, I used conda as package and and environment manager, below are the steps I went through to set up [AutoGen](https://github.com/microsoft/autogen) with AutoGen Studio.

The setup uses Microsoft Speech SDK, so a speech resource needs to be configured on Azure. For more info on Microsoft Speech services: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/
and click on `Text to speech/Get started with text to speech' .

##  Installation (conda)
After installing [Miniconda](https://www.anaconda.com/download/success), go to the cloned repository and run in a terminal:

    :: create a new environment `autogen' with all the necessary packages
    conda env create --file environment.yml
    conda activate autogen

## Setting up the environment variables
The project uses the Microsoft Speech SDK for Python to handle text to speech (TTS) and speech to text (STT) when running the team. It uses gpt-4o-mini as chat completion client with an OpenAI API key. Environment variables can be set using `conda' in a terminal:

    conda env config vars set OPENAI_API_KEY=<your-openai-api-key>
Also set SPEECH_KEY, SPEECH_REGION to the Speech resource key and region,  and set SPEECH_ENDPOINT. Don't forget to reactivate the environment before proceeding to the next step:

    conda activate autogenv0.4

## Launching the UI
Go to a working directory of your choice, then run:

    autogenstudio ui --port 8081 --appdir ./myapp

the application will be saved to a subfolder `myapp' and the AutoGen Studio GUI will run on port 8081. Click the link that appears in the terminal output to access AutoGen Studio via your internet browser.

## Loading the components

![Opening JSON editor view](https://github.com/pavelmdescamps1002/autogen-ML-assistant/blob/main/autogen-component-init.png "Opening JSON editor view")


Open the JSON editor view and simply copy-paste the contents of the team-config.json file into the JSON editor. When switching back to visual builder, the team should have appeared and is ready to run!

You can test the team by pressing the blue Run button. Alternatively, you can go to Playground and use the drop-down menu next to New Session to create a chat that's not deleted afterwards.

# Components

## Listen tool

## Speech tool

## Agent prompts
