import json
from faq.models import FAQCategory, FAQ


def run():
    # Load the JSON data
    with open('faq_data.json') as f:
        data = json.load(f)

        for category_data in data:
            # Create or get the FAQ category
            category, created = FAQCategory.objects.get_or_create(
                name=category_data['category']
            )

            # For each question in the category, create FAQ records
            for question_data in category_data['questions']:
                FAQ.objects.get_or_create(
                    category=category,
                    question=question_data['question'],
                    answer=question_data['answer']
                )
