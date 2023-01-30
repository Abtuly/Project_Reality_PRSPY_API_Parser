import requests


class server_loader:
    server = None

    def __init__(self, server_target_id: str):
        servers = requests.get(
            "https://servers.realitymod.com/api/ServerInfo").json()["servers"]
        servers = list(servers)
        for server in servers:
            if server["serverId"] == server_target_id:
                self.server = server

    def get_map_name(self):
        return self.getProperties()["mapname"]

    def get_host_name(self) -> str:
        return self.getProperties()["hostname"]

    def get_host_max_players(self) -> str:
        return self.getProperties()["maxplayers"]

    def get_game_type(self):
        return self.getProperties()["gametype"]

    def get_current_players(self):
        return self.getProperties()["numplayers"]

    def getProperties(self):
        return self.server["properties"]

    def get_team_one(self):
        return self.getProperties()["bf2_team1"]

    def get_team_two(self):
        return self.getProperties()["bf2_team2"]

    def get_map_size(self):
        return self.getProperties()["bf2_mapsize"]
