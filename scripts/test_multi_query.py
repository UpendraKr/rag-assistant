from app.services.query_generator import QueryGenerator

generator = QueryGenerator()

generated_queries = generator.generate(
    "What is ranking of iit delhi in 2021 for engineering?"
)

for index, query in enumerate(generated_queries, start=1):

    print(f"{index}. {query}")