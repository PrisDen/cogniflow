from app.db import get_engine
from app.config import settings
from app.models.prompts import prompts
from sqlalchemy import insert

engine = get_engine(settings.database_url)

sample_prompts = [
    "Write a function that reverses a string without using built-in reverse methods.",
    "Implement a simple calculator that supports addition, subtraction, multiplication, and division.",
    "Create a function that checks if a given string is a palindrome.",
    "Write a program that prints the Fibonacci sequence up to n terms.",
    "Implement a function that finds the largest number in an array."
]

with engine.connect() as conn:
    for prompt_text in sample_prompts:
        conn.execute(insert(prompts).values(text=prompt_text))
    conn.commit()
    
print(f"✅ Seeded {len(sample_prompts)} prompts")