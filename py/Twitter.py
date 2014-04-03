import Twitter_Oauth

Consumer_Key = 'jkITE2vTsnbZbO4isffog'
Consumer_Secret = 'VAUmkrC3Tjj1OgVMLrtkSoNtvD7k4SZ6PhG0elBWHUw'

bearer_token = get_bearer_token(Consumer_Key,Consumer_Secret) # generates a bearer token
search_results = search_for_a_tweet(bearer_token, 'test') # does a very basic search
print search_results # prints results form the search
