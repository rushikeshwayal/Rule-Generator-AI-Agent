from config import Vertical
import json
import os

# # initialize Agent
VerticalAgent = Vertical()

# # get the list of models
models = VerticalAgent.model_list()
print(models)

# # get the list of output parsers
output_parsers = VerticalAgent.output_parser_list()
print(output_parsers)

# open json file get prompt
with open('VerticalAgent\Prompt.json') as file:
    data = json.load(file)

user_input = data[0].get('user_input')
system_input = data[0].get('system_msg')
print(user_input)  # Ensure this is not None
print("=======")
print(system_input)

# get the response from the agent

response = VerticalAgent.invoke_vertical(
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