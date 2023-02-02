import requests
import os
import json


class server_loader:

    def __init__(self, server_target_id: str):
        server_loader._create_file(server_target_id)
        servers_info_request = requests.get(
            "https://servers.realitymod.com/api/ServerInfo")
        if servers_info_request.ok:
            servers = list(servers_info_request.json()["servers"])
            for server in servers:
                if server["serverId"] == server_target_id:
                    self.server = server
                    server_loader._writeResonseToFile(
                        server_target_id, self.server)
        else:
            self.server = json.loads(
                server_loader._get_last_request(server_target_id))

    def _get_last_request(serverID: str):
        fileName = f"{serverID}.json"
        file = open(fileName, "r")
        file_content = file.read()
        file.close()
        return file_content

    def _create_file(serverID: str):
        fileName = f"{serverID}.json"
        if not os.path.exists(f"{serverID}.json"):
            open(fileName, "w").close()

    def _writeResonseToFile(serverID, response: dict):
        file = open(f"{serverID}.json", "w")
        file.write(json.dumps(response))
        file.close()

    def get_map_name(self):
        return self.get_properties()["mapname"]

    def get_host_name(self) -> str:
        return self.get_properties()["hostname"]

    def get_host_max_players(self) -> str:
        return self.get_properties()["maxplayers"]

    def get_game_type(self):
        return self.get_properties()["gametype"]

    def get_current_players_count(self):
        return self.get_properties()["numplayers"]

    def get_properties(self):
        return self.server["properties"]

    def get_team_one(self):
        return self.get_properties()["bf2_team1"]

    def get_team_two(self):
        return self.get_properties()["bf2_team2"]

    def get_map_size(self):
        return self.get_properties()["bf2_mapsize"]

    def get_players(self) -> list:
        return self.server["players"]
