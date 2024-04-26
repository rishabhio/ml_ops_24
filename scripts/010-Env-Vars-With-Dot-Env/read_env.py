


from dotenv import load_dotenv 
import os 
load_dotenv()


one = os.getenv("ENV_VAR_ONE") 
print( one ) 

two = os.getenv("ENV_VAR_TWO") 
print( two ) 