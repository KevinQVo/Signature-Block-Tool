import streamlit as st
from tickers import *  #Tickers with associated Fund Name
from singular_signatures import *   # Formatting Each Individual Blocks

# Define the collection of all blocks. If there are any additional blocks. 
# Please MAINTAIN THE ORDER OF THE LIST BASED ON THE DICTIONARY. 
# THIS CODE IS READ FROM TOP TO BOTTOM
#Please add it here!
all_dicts = [
    block101, block100, block99, block98, block97, block95, block94,
    block93, block92, block91, block90, block89,
    block85, block84, block83, block82, block81, blockinactive1, blockinactive2, block_seven, block_eight, block_nine,
    block_ten, block_seventeen, block_nineteen, block_inactive1, 
]

# Mapping from block names to their corresponding signature functions
block_name_to_function = {
    'block_seven': print_block7signature,
    'block_eight': print_block8signature,
    'block_nine': print_block9signature,
    'block_ten': print_block10signature,
    'block_seventeen': print_block17signature,
    'block_nineteen': print_block19signature,
    'block101': print_block101signature,
    'block100': print_block100signature,
    'block99': print_block99signature,
    'block98': print_block98signature,
    'block97': print_block97signature,
    'block95': print_block95signature,
    'block94': print_block94signature,
    'block93': print_block93signature,
    'block92': print_block92signature,
    'block91': print_block91signature,
    'block90': print_block90signature,
    'block89': print_block89signature,
    'block85': print_block85signature,
    'block84': print_block84signature,
    'block83': print_block83signature,
    'block82': print_block82signature,
    'block81': print_block81signature,
    'blockinactive1': print_inactiveblock1signature,
    'blockinactive2': print_inactiveblock2signature,
    'block_inactive1': print_blockinactive1,
    # If there are any changes, please add the mapping here
}

# Function to retrieve data by ticker
def get_data_by_ticker(ticker):
    for block_dict in all_dicts:
        if ticker in block_dict:
            return block_dict[ticker]
    return None

# Streamlit application interface
st.title(" Signature Block Tool! ")
st.caption('Created By: Kevin Vo :sunglasses:')
 

def find_block_name_by_ticker(ticker):
    for block_dict in all_dicts:
        if ticker in block_dict:
            # Identify the block name based on the global variable matching the block_dict
            for name, block in globals().items():
                if block is block_dict and name.startswith('block'):
                    return name
    return None



# User input
user_input = st.text_area("Please enter tickers(Comma-Separated Or List): ")


if user_input:
    user_input_normalized = user_input.replace('\r\n', '\n').replace('\r', '\n')
    
    # First split by newline, then check each line for commas and split further if needed
    tickers = [ticker.strip() for line in user_input_normalized.split('\n') for ticker in line.split(',') if ticker.strip()]
    processed_blocks = set()
    block_ticker_data = {}
    bad_tickers = []  # List to collect bad tickers

    for ticker in tickers:
        block_name = find_block_name_by_ticker(ticker)
        if block_name:
            ticker_data = get_data_by_ticker(ticker)
            if ticker_data:
                # Collecting ticker data under its block name
                if block_name not in block_ticker_data:
                    block_ticker_data[block_name] = []
                block_ticker_data[block_name].extend(ticker_data)
        else:
            # If the ticker does not belong to any block, it's considered bad. Appending to the list.
            bad_tickers.append(ticker)
            
    if bad_tickers:
         with st.container():
            st.error(f"**INVAILD TICKERS ENTERED:** {', '.join(bad_tickers)}")
    
    # Display the information for valid tickers
    for block_name, data in block_ticker_data.items():
        for info in data:
        # 'info' contains the value you want to display in bold. This correlates to the fund name (Tickers.py)   
                st.markdown(f"**{info}**")  # This makes the text bold
        if block_name not in processed_blocks:
            if block_name in block_name_to_function:
                block_name_to_function[block_name]()
                processed_blocks.add(block_name)

        # Check and display block signature if not already processed
        if block_name not in processed_blocks:
            if block_name in block_name_to_function:
                block_name_to_function[block_name]()
                processed_blocks.add(block_name)
