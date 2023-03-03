# A simple ChatGPT frontend in Django using gpt-3.5-turbo model and API
by [Victor Donoso](https://github.com/victordonoso)

This project uses the new [gpt-3.5-turbo](https://platform.openai.com/docs/guides/chat/chat-completions-beta) model API from [OpenAI](https://openai.com/) and a [Django](https://www.djangoproject.com/) webserver to make a simple chatbot frontend to run it locally, consuming your own OpenAI credits by using your API Key.

Currently there are no models, just using the simplicity of Django as a webserver and using the OpenAI API to generate responses from prompts and a simple frontend to interact with the bot.

I've added Bootstrap to the frontend to make it look a bit nicer.

## Usage
1. Make sure you have a working account on [OpenAI](https://openai.com/) and have created an API key. Save it.
2. Add the API key to the `OPENAI_API_KEY` environment variable.
3. Install the requirements with `pip install -r requirements.txt` or alternatively create a virtual environment and install the requirements there. Make sure the environment variable is present in the virtual environment.
4. Run the server with `python manage.py runserver`.
5. Go to `http://localhost:8000/` to interact with the bot.

## TODO
- [ ] Dunno.

## License
[MIT](https://choosealicense.com/licenses/mit/)
