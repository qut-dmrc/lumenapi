# lumenapi
Python client for the Lumen database API

## Usage

        # Initialise API client with your API key
        lumen = Lumen(api_key='YOUR_API_KEY')
        
        # Construct a dictionary of search terms; e.g.:
        search_dict = {'recipient_name': 'youtube', 'per_page': 100, 'sort_by': 'date_received desc'}
        
        # Search and return JSON results as a dictionary
        results = lumen.search(search_dict)
        
