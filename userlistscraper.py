import discord
import json
import sys

bot = discord.Client()

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

token = config.get('token')


output_file = 'server_users.json'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    if len(sys.argv) != 2:
        print("Usage: python bot_script.py <SERVER_ID>")
        sys.exit(1)

    server_id = int(sys.argv[1])
    await collect_server_users(server_id)

async def collect_server_users(server_id):
    server_data = {}

    for guild in bot.guilds:
        if guild.id == server_id:
            print(f'Processing server: {guild.name}')
            server_data[guild.name] = {}

            for member in guild.members:
                user_name = str(member)
                user_id = member.id
                server_data[guild.name][user_name] = user_id

            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(server_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    bot.run(token)