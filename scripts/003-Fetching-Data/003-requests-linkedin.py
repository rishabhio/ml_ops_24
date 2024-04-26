

import requests 
data = requests.get('https://www.linkedin.com/in/johnespirian/?originalSubdomain=uk')
print(data.text) # Print the HTML content of the page. 

