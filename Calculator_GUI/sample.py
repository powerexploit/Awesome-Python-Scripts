"""Intentionally insecure sample used to exercise Rudra's detectors.
Do NOT copy any of this into real code."""
import os
import pickle

import openai
from flask import request
from langchain.agents import load_tools
from langchain_experimental.tools import PythonREPLTool

openai.api_key = "sk-proj-AbC123DeF456ghi789JkL012mno345PqR"  # LLM02: hardcoded key


def summarize():
    user_text = request.args.get("q")                       # untrusted input
    resp = openai.chat.completions.create(                  # LLM10: no max_tokens
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Summarize: {user_text}"}],  # LLM01
    )
    code = resp.choices[0].message.content
    return eval(code)                                       # LLM05: output -> eval


def load_model(path):
    with open(path, "rb") as fh:
        return pickle.load(fh)                              # LLM04: unsafe deserialize


def build_agent(llm):
    tools = load_tools(["terminal", "llm-math"])            # LLM06: dangerous tool
    repl = PythonREPLTool()                                 # LLM06: code execution
    return tools, repl
