from deutschland import interpol
import time
from deutschland import interpol
from pprint import pprint
from deutschland.interpol.api import default_api
from deutschland.interpol.model.red_notice_detail import RedNoticeDetail
from deutschland.interpol.model.red_notice_detail_images import RedNoticeDetailImages
from deutschland.interpol.model.red_notices import RedNotices
# Defining the host is optional and defaults to https://ws-public.interpol.int
# See configuration.py for a list of all supported configuration parameters.
configuration = interpol.Configuration(
    host = "https://ws-public.interpol.int"
)



# Enter a context with an instance of the API client
with interpol.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    forename = "DANIELA" # str | First name (optional)
name = "Klette" # str | Last name (optional)
nationality = "DE" # str | Two digit country code (optional)
age_max = 120 # int | maximum age (optional)
age_min = 18 # int | minimum age (optional)
free_text = "" # str | Free text query (optional)
sex_id = "F" # str | Free text query (optional)
arrest_warrant_country_id = "DE" # str | Two digit country code (optional)
page = 1 # int | pagination - starts with 1 (optional)
result_per_page = 200 # int | resultPerPage (optional)

try:
	# Get Red Notices
	api_response = api_instance.notices_v1_red_get(forename=forename, name=name, nationality=nationality, age_max=age_max, age_min=age_min, free_text=free_text, sex_id=sex_id, arrest_warrant_country_id=arrest_warrant_country_id, page=page, result_per_page=result_per_page)
	pprint(api_response)
except interpol.ApiException as e:
	print("Exception when calling DefaultApi->notices_v1_red_get: %s\n" % e)