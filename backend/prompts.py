def build_prompt(code: str, language: str) -> str:
    """
    Builds a structured prompt for the AI code review assistant.
    """

    prompt = f"""
You are an experienced software engineer and code reviewer.

Analyze the following {language} source code and provide:
1. Bugs or possible errors
2. Bad coding practices
3. Security vulnerabilities (if any)
4. Performance improvements
5. Clean code and readability suggestions

Give your response in clear bullet points using simple language.

Source Code:
{code}
"""
    return prompt.strip()
