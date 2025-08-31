from crewai import LLM
from dotenv import load_dotenv
import time


load_dotenv()

# llm = LLM(
#     model="groq/deepseek-r1-distill-llama-70b",
#     temperature=0.0,
#     rpm = 30,
# )


# SOLUTION 2: Custom wrapper with sleep between calls
class RateLimitedLLM(LLM):
    def __init__(self, *args, sleep_duration=2.0, **kwargs):
        super().__init__(*args, **kwargs)
        self.sleep_duration = sleep_duration
        self.last_call_time = 0
    
    def call(self, *args, **kwargs):
        # Calculate time since last call
        current_time = time.time()
        time_since_last_call = current_time - self.last_call_time
        
        # Sleep if needed to maintain minimum interval
        if time_since_last_call < self.sleep_duration:
            sleep_time = self.sleep_duration - time_since_last_call
            print(f"Rate limiting: sleeping for {sleep_time:.2f} seconds...")
            time.sleep(sleep_time)
        
        # Make the call and update last call time
        result = super().call(*args, **kwargs)
        self.last_call_time = time.time()
        return result

# Use the rate-limited LLM
llm = RateLimitedLLM(
      model="groq/deepseek-r1-distill-llama-70b",
      temperature=0.0,
      sleep_duration=40.0  # 3 seconds between calls
)