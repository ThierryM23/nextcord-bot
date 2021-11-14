from nextcord.ext import commands
from src.utils.embedder import embed_success
from bs4 import BeautifulSoup
import requests


class Crypto(commands.Cog, name="crypto"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="crypto")
    async def crypto(self, ctx: commands.Context, moneda=''):
        """A command to receive information about the mos importante Crypto
        Usage:
        ```
        ?crypto          # da la cotizacion de BTC y ETH
        ?crypto 10       #las 10 primeras crypto
        ?crypto ripple   # da la cotizacion de la moneda escrita
        ```
        """

        # respond to the message
        await ctx.send(f"a su ordenes <@{ctx.author.id}>")

        if moneda == '':
            response = f' {self.coin_scraping("bitcoin")}'
            await ctx.send(embed=embed_success(response))
            response = f'{self.coin_scraping("ethereum")}'
            await ctx.send(embed=embed_success(response))
        else:
            if moneda.isnumeric():
                coin = 12 if int(moneda) > 10 else int(moneda)
                response = f'{self.coinmarket(coin)}'
                await ctx.send(response)
            else:
                response = f'{self.coin_scraping(moneda)}'
                await ctx.send(embed=embed_success(response))

    def coin_scraping(self, crypto):
        url = requests.get('https://awebanalysis.com/es/coin-details/' + crypto + '/')
        soup = BeautifulSoup(url.content, 'html.parser')
        html = BeautifulSoup(url.text, "html.parser")
        result = soup.find('td', {'class': 'wbreak_word align-middle coin_price'})
        format_result = result.text
        tabla = html.find_all(class_='table table-striped mb-0')
        contenido = [i.get_text(strip=True) for i in tabla[0].find_all('td')]
        contenido = [item for item in contenido if item != '']
        print(contenido)
        textocoin = crypto + '\nPrecio Actual USD :' + contenido[0].rjust(12) + '\n% de Cambio 1 hora:' + contenido[
            2].rjust(12) + '\n% de Cambio 24h    :' + contenido[3].rjust(12)
        return textocoin

    def rellenar(self, texto, donde, cant: int):
        largo = len(texto)
        cant = largo if cant < largo else cant
        if donde == 'R' or donde == 'r':
            texto = texto.ljust(cant, ' ')
        elif donde == 'L' or donde == 'l':
            texto = texto.rjust(cant, ' ')
        else:
            texto = texto.rjust(cant / 2, ' ').ljust(cant, ' ')
        return texto

    # def coinmarket(self, crypto):
    #     url = requests.get('https://coinmarketcap.com/es/all/views/all/')
    #     # soup = BeautifulSoup(url.content, 'html.parser')
    #     # result = soup.find('tr', {'class': 'cmc-table-row'})
    #     html = BeautifulSoup(url.text, "html.parser")
    #     tabla = html.find_all(class_='cmc-table-row')
    #     # linea = [i.get_text(strip=True) for i in tabla[0].find_all('tr')]
    #     textocoin = ' {:<4} {:<20} {:<5} {:<15} {:<10} {:<10} {:<10} \n'.format('Top',
    #                                                                             self.rellenar('nombre', 'R', 20),
    #                                                                             self.rellenar('Símbolo', 'R', 5),
    #                                                                             self.rellenar('Precio', 'L', 15),
    #                                                                             self.rellenar('% 1h', 'L', 10),
    #                                                                             self.rellenar('% 24h', 'L', 10),
    #                                                                             self.rellenar('% 7d', 'L', 10))
    #
    #     largo = int(crypto) if len(tabla) > int(crypto) else len(tabla)
    #     for j in range(largo):
    #         contenido = [i.get_text(strip=True) for i in tabla[j].find_all('td')]
    #         contenido = [item for item in contenido if item != '']
    #         # print(contenido)
    #         name = contenido[1]
    #         b = 0
    #         for a in name:
    #             if a.isupper() == True:
    #                 b += 1
    #             else:
    #                 break
    #         name = contenido[1][b - 1:]
    #         textocoin = textocoin + ' {:<4} {:<20} {:<5} {:<15} {:<10} {:<10} {:<10} \n'.format(contenido[0],
    #                                                                                             self.rellenar(name, 'R', 20),
    #                                                                                             self.rellenar(contenido[2],
    #                                                                                                      'R', 5),
    #                                                                                             self.rellenar(contenido[4],
    #                                                                                                      'L', 15),
    #                                                                                             self.rellenar(contenido[7],
    #                                                                                                      'L', 10),
    #                                                                                             self.rellenar(contenido[8],
    #                                                                                                      'L', 10),
    #                                                                                             self.rellenar(contenido[9],
    #                                                                                                      'L', 10))
    #         print(textocoin)
    #
    #     return textocoin

    @commands.command(name='crypto')
    async def crypto(self, ctx, moneda=''):
        await ctx.send(f"a su ordenes <@{ctx.author.id}>")
        if moneda == '':
            response = f' {self.coin_scraping("bitcoin")}'
            await ctx.send(response)
            response = f'{self.coin_scraping("ethereum")}'
            await ctx.send(response)
        else:
            if moneda.isnumeric():
                url = requests.get('https://coinmarketcap.com/es/all/views/all/')
                # soup = BeautifulSoup(url.content, 'html.parser')
                # result = soup.find('tr', {'class': 'cmc-table-row'})
                html = BeautifulSoup(url.text, "html.parser")
                tabla = html.find_all(class_='cmc-table-row')
                largo = int(moneda) if len(tabla) > int(moneda) else len(tabla)
                for j in range(
                        largo):  # loop par aimprimir la x crypto, se hace una por una por que esta limitada la string de respuesta
                    contenido = [i.get_text(strip=True) for i in tabla[j].find_all('td')]
                    contenido = [item for item in contenido if item != '']
                    # print(contenido)
                    name = contenido[1]
                    b = 0
                    for a in name:
                        if a.isupper() == True:
                            b += 1
                        else:
                            break
                    name = contenido[1][b - 1:]
                    textocoin = ' {:<3} - {:<20} {:<5}  Cotizacion USD:  {:<15} \n %1h: {:<10} -- %24h: {:<10} -- %7d: {:<10} \n'.format(
                        contenido[0],
                        name,
                        contenido[2],
                        contenido[4],
                        contenido[7],
                        contenido[8],
                        contenido[9])
                    await ctx.send(textocoin)
            else:
                response = f'{self.coin_scraping(moneda)}'
                await ctx.send(response)


# This function will be called when this extension is loaded.
# It is necessary to add these functions to the bot.
def setup(bot: commands.Bot):
    bot.add_cog(Crypto(bot))
