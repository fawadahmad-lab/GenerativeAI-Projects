from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
    template="""
    You are an AI research assistant helping summarize and explain research papers.

    📌 **Research Paper**: {paper_input}
    📖 **Style Preference**: {style_input}
    📏 **Explanation Length**: {length_input}

    Please provide an explanation that aligns with the selected paper, style, and length. 
    - If **Maths Heavy**, focus on mathematical formulations, equations, and theoretical details.
    - If **Code Heavy**, include code snippets or implementation details.
    - If **Beginner Friendly**, explain concepts in a simple, accessible way.

    Ensure the explanation is well-structured, informative, and aligned with the research paper's main ideas.
    """,
    input_variables=['paper_input','style_input','length_input'],
    validate_template=True
)
template.save('template.json')
