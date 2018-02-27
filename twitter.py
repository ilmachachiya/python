from tweepy import *
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "vxKlX4Wart7NHF3nRp2q23tSv",
    "consumer_secret"     : "9nf3zvLUAjYl368jJkHzUk5gkQ09wKzJ0oM9uSw64lMTQbUsLX",
    "access_token"        : "967251530196930560-1mfzpVeRilrRWUgRWenXjdLiDOMt82C",
    "access_token_secret" :  "PSEACgq1qzdLIKVUeHG4JbMxi7QRMFkg11FCQnilDAavI"
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
