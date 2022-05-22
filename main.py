import discord
from discord.ext import commands

#variaveis ( TIRANDO O TOKEN E A RESPOSTA AS OUTRAS SAO FUTEIS )
token = 'OTUyNDA3ODQ3NzQ3MDkyNTAx.Yi1k7Q.eJ0EOIBCWFubMyyU4PvWxr9kh9w'
resposta = 'Olá mande as suas duvidas na DM do meu criador: stryx今#7108'
ola = 'Olá estou ativo cuidando esse canal'
inicio = 'Inicializando em 3,2,1...'
receba = 'Rengar saiu para caçar'

#prefixo inexistente ( SEMPRE ATIVADO )
bot = commands.Bot(command_prefix="")

#evento de inicialização ( MENSAGENS NO CONSOLE )
@bot.event
async def on_ready():
    print('Bibliotecas instaladas')
    print('Extensões prontas')

#evento de mensagens ( MENSAGENS QUE SAO EXCLUIDAS )  
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "seu preto" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "pr3to" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "viado" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "v1ado" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "vi4do" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "macaco" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "mamaco" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "m4caco" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "mac4co" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "macac0" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "vadia" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "v4dia" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "puta" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "put4" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "cachorra" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "vagabunda" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "v4gabunda" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "biscate" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "putão" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "traveco" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, não aceitamos atitudes que discriminem alguém"
        )

        await message.delete()

    if "fudido" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!")

        await message.delete()

    if "babuino" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "baitola" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "escravo" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "escr4vo" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "escr@vo" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "escrav0" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "travecao" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "mulher de 3 pernas" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "baitolinha" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "vsf" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!")

        await message.delete()

    if "vai se fude" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!")

        await message.delete()

    if "vai toma no cu" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!")

        await message.delete()

    if "picole de pixi" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!, nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "sabonete de mecanico" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!,  nao aceitamos atitudes que discriminem alguem"
        )

        await message.delete()

    if "tinha que ser mulher" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!")

        await message.delete()

    if "filha da puta" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!")

        await message.delete()

    if "putinha" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!")

        await message.delete()

    if "preto" in message.content:
        await message.channel.send(
            f"Por favor,{message.author.name}, mantenha seus modos por aqui!")

        await message.delete()

    if "lista de palavras banidas" in message.content:

        await message.channel.send(
            "https://discord.com/channels/927020729214574652/955826292232695890/955827947544117358"
        )

    await bot.process_commands(message)

#comando de ajuda ( MENSAGEM DIRETA )
@bot.command(name="ajuda", case_insensitive="true")
async def support(ctx):

    await ctx.send(resposta)

    await message.delete()

#comando para testar atividade ( MENSAGEM DIRETA )
@bot.command(name="rengar", case_insensitive="true")
async def most_valuable(ctx):

    await ctx.send(ola)

    await message.delete()


bot.run(token)
