**Built with ❤️ by/ Ahmed Essam using CrewAI, DeepSeek, and Groq**

# Rankyx AI Procurement System

A multi-agent AI system powered by CrewAI that automates product research and procurement analysis. The system uses intelligent agents to search, scrape, and analyze product data from multiple e-commerce websites, generating comprehensive procurement reports.

## 🚀 Features

- **Multi-Agent Architecture**: Coordinated team of AI agents with specialized roles
- **Intelligent Search**: AI-powered search query generation and optimization
- **Web Scraping**: Automated data extraction from multiple e-commerce platforms
- **Procurement Analysis**: Comprehensive product comparison and recommendation reports
- **Rate Limiting**: Built-in protection against API rate limits
- **Flexible Configuration**: Environment-based settings for easy deployment

## 🏗️ Architecture

The system consists of four specialized agents working in sequence:

1. **Search Queries Recommendation Agent**: Generates optimized search queries
2. **Search Engine Agent**: Executes searches across target websites
3. **Scraping Agent**: Extracts product data and pricing information
4. **Procurement Report Author**: Creates detailed analysis reports

## 📋 Prerequisites

- Python 3.8+
- Groq API key for DeepSeek model access
- AgentOps account (optional, for monitoring)
- Internet connection for web scraping

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AhmedEssam29/AI_Agents_CREWAI.git
   cd rankyx-procurement-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

## 🔧 Configuration

Create a `.env` file in the project root with the following variables:

```env
# API Keys
GROQ_API_KEY=your_groq_api_key_here
AGENTOPS_API_KEY=your_agentops_key_here  # Optional

# Rate Limiting Configuration
GROQ_RPM=25                    # Requests per minute (stay below limit)
TASK_DELAY=3.0                 # Seconds between tasks
RETRY_DELAY=35.0               # Seconds to wait on rate limit

# Model Configuration
LLM_MODEL=groq/deepseek-r1-distill-llama-70b
MAX_RETRIES=3
```

## 📁 Project Structure

```
rankyx-procurement-system/
├── main.py                    # Main execution script
├── agents.py                  # Agent and task definitions
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
├── .env                      # Your environment variables (create this)
├── README.md                 # This file
└── utils/
    ├── rate_limiter.py       # Rate limiting utilities
    └── scraper_tools.py      # Web scraping tools
```

## 🚀 Usage

### Basic Usage

```python
from main import execute_procurement_analysis

# Run procurement analysis
results = execute_procurement_analysis(
    product_name="coffee machine for the office",
    websites=["www.amazon.eg", "www.jumia.com.eg", "www.noon.com/egypt-en"],
    country="Egypt",
    keywords_count=10,
    language="English",
    score_threshold=0.10,
    top_recommendations=10
)

print(results)
```

### Command Line Usage

```bash
# Basic execution
python main.py

# With custom parameters
python main.py --product "wireless headphones" --country "Egypt" --keywords 15
```

### Advanced Configuration

```python
from crewai import LLM
from main import RateLimitedCrew

# Custom LLM configuration
llm = LLM(
    model="groq/deepseek-r1-distill-llama-70b",
    rpm=25,
    max_retries=3,
    retry_delay=3.0
)

# Create crew with custom settings
crew = RateLimitedCrew(
    agents=your_agents,
    tasks=your_tasks,
    task_delay=5.0,  # Adjust based on rate limits
    knowledge_sources=[company_context]
)
```

## 📊 Input Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `product_name` | string | Product to search for | "coffee machine for the office" |
| `websites_list` | list | Target e-commerce websites | ["www.amazon.eg", "www.jumia.com.eg"] |
| `country_name` | string | Target country/market | "Egypt" |
| `no_keywords` | integer | Number of search keywords to generate | 10 |
| `language` | string | Language for search and results | "English" |
| `score_th` | float | Relevance score threshold | 0.10 |
| `top_recommendations_no` | integer | Number of top products to recommend | 10 |

## 📈 Output

The system generates a comprehensive procurement report including:

- **Product Recommendations**: Top-ranked products with scores
- **Price Comparison**: Pricing across different platforms
- **Feature Analysis**: Key product features and specifications
- **Availability Status**: Stock information per website
- **Procurement Insights**: AI-generated buying recommendations

## ⚠️ Rate Limiting

The system includes built-in rate limiting to handle API constraints:

- **Automatic Delays**: Configurable delays between API calls
- **Retry Logic**: Automatic retry with exponential backoff
- **Error Handling**: Graceful handling of rate limit errors
- **Monitoring**: Real-time tracking of API usage

### Rate Limit Error Solutions

If you encounter rate limit errors:

1. **Increase delays**: Adjust `TASK_DELAY` in your `.env` file
2. **Reduce RPM**: Lower the `GROQ_RPM` setting
3. **Upgrade tier**: Consider upgrading your Groq service tier

## 🔍 Monitoring

The system integrates with AgentOps for monitoring:

- **Agent Performance**: Track execution times and success rates
- **API Usage**: Monitor token consumption and costs
- **Error Tracking**: Detailed error logs and debugging info
- **Custom Tags**: Organized monitoring with 'crewai' tags

## 🛡️ Error Handling

Common issues and solutions:

| Error | Cause | Solution |
|-------|--------|----------|
| `RateLimitError` | API rate limit exceeded | Increase `TASK_DELAY` or reduce `GROQ_RPM` |
| `ConnectionError` | Network/website issues | Check internet connection and target URLs |
| `AuthenticationError` | Invalid API key | Verify `GROQ_API_KEY` in `.env` file |
| `TimeoutError` | Request timeout | Increase timeout values in agent configuration |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



