import json
from datetime import datetime
import requests

class Auth():

    def __init__(self):

        self.secretsPath = 'secrets.json'

        self.loadSecrets()

        if self.checkAccessExpire() and not self.checkRefreshExpire():
            self.createAccessToken()

    def loadSecrets(self):

        with open(self.secretsPath) as f:

            self.secrets = json.load(f)

            self.accessToken = self.secrets['schwab']['access-token']
            self.accessTokenCreationDate = self.secrets['schwab']['access-token-creation-date']
            self.appKey = self.secrets['schwab']['app-key']
            self.appKeyBase64 = self.secrets['schwab']['app-key-base64']
            self.appKeySecretBase64 = self.secrets['schwab']['app-key-secret-base64']
            self.appSecret = self.secrets['schwab']['app-secret']
            self.appSecretBase64 = self.secrets['schwab']['app-secret-base64']
            self.authCode = self.secrets['schwab']['auth-code']
            self.redirectUrl = self.secrets['schwab']['redirect-url']
            self.refreshToken = self.secrets['schwab']['refresh-token']
            self.refreshTokenCreationDate = self.secrets['schwab']['refresh-token-creation-date']
            self.streamerInfo = self.secrets['schwab']['user-preferences']['streamer-info'][0]

    def getAccessToken(self):
        return self.accessToken

    def saveSecrets(self):

        with open(self.secretsPath, 'w') as file:
            json.dump(self.secrets, file, indent=4)

    def checkAccessExpire(self):

        currentUnixTimestamp = int(datetime.now().timestamp()) * 1000

        accessExpiredDate = self.accessTokenCreationDate + 1800000 # 30 minutes

        if currentUnixTimestamp > accessExpiredDate:
            return True
        
        return False
    
    def checkRefreshExpire(self):

        currentUnixTimestamp = int(datetime.now().timestamp()) * 1000

        # Calculate 7 days in milliseconds (7 days * 24 hours/day * 60 minutes/hour * 60 seconds/minute * 1000 ms/second)
        sevenDaysInMs = 7 * 24 * 60 * 60 * 1000

        refreshExpiredDate = self.refreshTokenCreationDate + sevenDaysInMs

        if currentUnixTimestamp > refreshExpiredDate:
            print("Info: Your schwab refresh token will expire in 1 day.")
            return True
        
        return False
    
    def checkDirtySecrets(self):

        with open(self.secretsPath) as f:

            testConfig = json.load(f)

        if json.dumps(testConfig, sort_keys=True) != json.dumps(self.secrets, sort_keys=True):
            print("Dirty Secrets Detected. Reloading secrets..")
            self.loadSecrets()

    def createAccessToken(self, generateRefreshToken=False):

        # NOTE TO SELF: The auth code that you get to first get a refresh token expires very quickly. 
        # eg. 30 seconds or less 

        tokenUrl = "https://api.schwabapi.com/v1/oauth/token"

        postData = {}

        if generateRefreshToken:
            postData = {
                "grant_type": "authorization_code",
                "code": self.authCode,
                "redirect_uri": self.redirectUrl
            }
        else:
            postData = {
                "grant_type": "refresh_token",
                "refresh_token": self.refreshToken
            }

        headers = {
            "Accept-Encoding": "gzip",
            "Accept-Language": "en-US",
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization" : "Basic " + self.appKeySecretBase64
        }

        res = requests.post(tokenUrl, headers=headers, data=postData)

        if res.status_code == 200:
            dirtySecrets = False
            resJson = json.loads(res.text)

            try:
                if 'refresh_token' in resJson.keys():
                    self.secrets['schwab']['refresh-token'] = resJson['refresh_token']
                    self.secrets['schwab']['refresh-token-creation-date'] = int(datetime.now().timestamp()) * 1000
                    dirtySecrets = True
                
                if 'access_token' in resJson.keys():
                    self.secrets['schwab']['access-token'] = resJson['access_token']
                    self.secrets['schwab']['access-token-creation-date'] = int(datetime.now().timestamp()) * 1000
                    dirtySecrets = True

                if dirtySecrets:
                    self.saveSecrets()
                    self.loadSecrets()

            except Exception as e:
                print("Error when trying to generate tokens")
                print(res.text)
                print(e)

    