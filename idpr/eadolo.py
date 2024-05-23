def get_api_call_data(url):
  """Returns the data from the API call to the given URL.

  Args:
    url: The URL to make the API call to.

  Returns:
    The data from the API call.
  """

  response = requests.get(url)
  response.raise_for_status()
  return response.json()
