from config import CustomAgent
from prompt import VerticalPrompt
import json
import os

# # initialize Agent
VerticalAgent = CustomAgent()



# initialize prompt
prompt = VerticalPrompt()

user_input=prompt.user_prompt(client_name="Datamatter",client_description="We Are Data migration service providing company provide buch of servises releted to data migration",website_content="https://www.datamatter.tech/")
system_input=prompt.system_prompt()


response = VerticalAgent.invoke_agent(
    user_input= user_input,
    system_input= system_input,
    model_name="google",
    output_parser="json",
    verbose=True,
    model_variant="gemini-1.5-flash"

)

print("response :",response)
print("+++++++++")
print("type of response :",type(response))

# Path to the file
file_path = 'VerticalAgent_Output.json'

# Check if the file exists
if os.path.exists(file_path):
    # Read the existing data from the file
    with open(file_path, 'r') as file:
        existing_data = json.load(file)
        # If the existing data is not a list, make it one
        if not isinstance(existing_data, list):
            existing_data = [existing_data]
else:
    # If the file doesn't exist, start with an empty list
    existing_data = []

# Append the new response to the existing data (which should now be a list)
existing_data.append(response)

# Write the updated data back to the file
with open(file_path, 'w') as file:
    json.dump(existing_data, file, indent=4)