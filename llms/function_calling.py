"""LLM Function calling"""

# from config import env
import os
import dotenv
import json
from typing import Literal
from openai import OpenAI

dotenv.load_dotenv()


def get_current_weather(
    location, unit: Literal["celsius", "fahrenheit"] = "fahrenheit"
) -> dict:
    """
    Augment the LLM with the current weather details as its training data limits it.
    In this example we hardcoded the information.
    """
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)


def function_definition() -> list:
    return [
        {
            "name": "get_current_weather",
            "description": "Get the current weather for the given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state of the location",
                    },
                    "units": {"type": "string", "enum": ["celsius", "fareinheit"]},
                },
                "required": ["location"],
            },
        }
    ]


def main():
    messages = [{"role": "user", "content": "What is the weather in Cape Town"}]
    client = OpenAI(api_key=os.environ["OPENAI_APIKEY"])
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        functions=function_definition(),
        stream=True,
        function_call="auto",
    )
    print(response)


if __name__ == "__main__":
    main()


"""
When using function calls you can, you can modify the tool calling behavior using
1. auto - model automatically decides
2. none - no functions are called
3. function_call = {"name": "name of the function you want to call"} - specify which function should be called
"""
