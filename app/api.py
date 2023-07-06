import requests, json, os

url = 'https://discord.com/api/v9/interactions'

discord_access_token = os.getenv('VIP_TOKEN')
server_id = os.getenv('SERVER_ID')
channel_id = os.getenv('CHANNEL_ID')

headers = {
    'Authorization': discord_access_token,
    'Content-Type': 'application/json'
}

def post(params: str):
	data = {
			'type': 2,
			'application_id': '1111163463528611881',
			'guild_id': server_id,
			'channel_id': channel_id,
			'session_id': 'b9c60564ee12feead0c19fa90978aeaf',
			'data': {
					'version': '1113702779941310597',
					'id': '1113508671079587937',
					'name': 'dj',
					'type': 1,
					'options': [
							{
									'type': 1,
									'name': 'v5_1',
									'options': [
											{
													'type': 3,
													'name': 'prompt',
													'value': params
											}
									]
							}
					]
			}
	}

	requests.post(url, headers=headers, data=json.dumps(data))