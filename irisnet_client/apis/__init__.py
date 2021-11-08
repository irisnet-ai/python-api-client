
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.endpoints_for_ai_checks_api import EndpointsForAIChecksApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from irisnet_client.api.endpoints_for_ai_checks_api import EndpointsForAIChecksApi
from irisnet_client.api.endpoints_to_setup_the_ai_api import EndpointsToSetupTheAIApi
from irisnet_client.api.miscellaneous_operations_api import MiscellaneousOperationsApi
