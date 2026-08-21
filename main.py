from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from skill_extractor import extract_skills
from vector import retriever

model = OllamaLLM(model="llama3.2")
template = """
You are an expert in analysing candidate resumes and providing feedback.
Use the following relevant examples from the resume database:
{context}
Candidate's Resume:
{resume}

Analyse the candidate and provide:
1. Strengths
2. Weaknesses
3. Missing skills
4. Overall suitability (just give a score out of 10)
5. Recommendations
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


while True:
    resume = input("Enter the candidate's resume (or type 'exit' to quit): ")
    if resume.lower() == 'exit':
        break
    skills = extract_skills(resume)
    print("\nExtracted Skills:")
    print(skills.model_dump_json(indent=2))
    retrieved_docs = retriever.invoke(resume)
    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    result = chain.invoke({
    "context": context,
    "resume": resume,
    "skills": skills.model_dump_json(),
    })

    docs=retriever.invoke(resume)
    result = result.replace("**", "")
    print(result)