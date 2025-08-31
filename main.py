from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from agents import search_queries_reccomendation_agent, search_queries_recommendation_task, procurement_report_author_agent, procurement_report_author_task, scraping_agent, scraping_task, search_engine_agent, search_engine_task
from dotenv import load_dotenv
import agentops



load_dotenv()



agentops.init(
    skip_auto_end_session=True,
    default_tags=['crewai']
)

print(agentops.get_client().config.exporter_endpoint)

about_company = "Rankyx is a company that provides AI solutions to help websites refine their search and recommendation systems."



company_context = StringKnowledgeSource(
    content=about_company
)


rankyx_crew = Crew(
    agents=[
        search_queries_reccomendation_agent,
        search_engine_agent,
        scraping_agent,
        procurement_report_author_agent,
    ],
    tasks=[
        search_queries_recommendation_task,
        search_engine_task,
        scraping_task,
        procurement_report_author_task,
    ],
    process=Process.sequential,
    knowledge_sources=[company_context]
    )

crew_results = rankyx_crew.kickoff(
    inputs={
        "product_name": "coffee machine for the office",
        "websites_list": ["www.amazon.eg", "www.jumia.com.eg", "www.noon.com/egypt-en"],
        "country_name": "Egypt",
        "no_keywords": 10,
        "language": "English",
        "score_th": 0.10,
        "top_recommendations_no": 10
    }
)

print(crew_results)