class Quote():
    '''
    This class represents a plain old data object response from the 
    https://api.iextrading.com/1.0/stock/aapl/quote api
    It holds stock pricing information for one company

    Throws:
    ValueError: If JSON doesn't have required attributes
    '''
    def __init__(self, api_response_dictionary={}):
        self.symbol = ""
        self.open = None #float: share price at open of market
        self.latestPrice = None # float: most recent price of a share
        self.error = ""

        #validation
        required_attributes = ["symbol", "open", "latestPrice"] #required attributes in api response
        for attribute in required_attributes:
            if attribute in api_response_dictionary:
                setattr(self, attribute, api_response_dictionary[attribute])
            else:
                error = "Required attribute for "
                error += self.__class__.__name__
                error += " not found in JSON response. The JSON response schema might have changed"
                self.error = error
                break
            