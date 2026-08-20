from ollama import chat
from pydantic import BaseModel
import json

class SkillExtraction(BaseModel):
    skills: list[str]
    technologies: list[str]
    programming_languages: list[str]
def extract_skills(resume: str):
    schema = SkillExtraction.model_json_schema()
    prompt = f"""
You are a resume skill extraction system.
Extract skills, technologies, and programming languages that are explicitly mentioned or clearly demonstrated in the resume. Don't invent skills.

Resume:
{resume}
Return the information according to this JSON schema:
"""
    prompt += json.dumps(schema, indent=2)
    response = chat(model="llama3.2", messages=[{"role": "user","content": prompt}], format=schema,options={"temperature": 0})
    result = SkillExtraction.model_validate_json(response.message.content)
    return result

if __name__ == "__main__":
    resume = input("Enter candidate resume: ")
    result = extract_skills(resume)
    print("\nExtracted Skills:")
    print(result.model_dump_json(indent=2))