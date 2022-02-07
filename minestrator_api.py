import requests

class Client:

    def __init__(self,token) -> None: 
        self.headers = {'Authorization': token}
        self._actionPossible = ["start","stop","restart","kill"]

    def getServersList(self):
        """Get a list of servers of the user."""
        rsp = requests.get("https://rest.minestrator.com/api/v1/server/list", headers=self.headers)
        return rsp.json()["data"]

    def getServerInfo(self,hashsupport):
        """
        Get information about a server.
            - Take hashsupport as an id of the server
        """
        #print(f"https://rest.minestrator.com/api/v1/server/data/{hashsupport}")
        rsp = requests.get(f"https://rest.minestrator.com/api/v1/server/data/{hashsupport}", headers=self.headers)
        return rsp.json()["data"]
    
    def getServerState(self,hashsupport):
        """
        Get the state of a server.
            - Take hashsupport as an id of the server
        """
        rsp = requests.get(f"https://rest.minestrator.com/api/v1/server/ressources/{hashsupport}", headers=self.headers)
        return rsp.json()["data"]

    def getServerContents(self,hashsupport):
        """
        Get the contents of a server.
            - Take hashsupport as an id of the server
        """
        rsp = requests.get(f"https://rest.minestrator.com/api/v1/server/content/{hashsupport}", headers=self.headers)
        return rsp.json()["data"]

    def setServerPower(self,hashsupport,action):
        """
        Get the contents of a server.
            - Take hashsupport as an id of the server
            - Take action; it can be start stop restart kill
        """
        if not action in self._actionPossible: raise Exception(f"{action} is not a recognized action.")
        rsp = requests.post("https://rest.minestrator.com/api/v1/server/action", headers=self.headers,data={"hashsupport":hashsupport,"action":action})
        return rsp.json()["data"]