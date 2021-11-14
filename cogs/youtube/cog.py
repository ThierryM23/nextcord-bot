import re
from discord.ext import commands
import urllib.request
import urllib.parse





'''
@bot.command()
async def ytm(ctx, *, search):
    query_string = urllib.parse.urlencode({'q': search})
    html_content = urllib.request.urlopen('https://music.youtube.com/search?' + query_string)
    await ctx.send('Todavia en construccion')
    # search_results = re.findall('watch\?v=(.{11})', html_content.read().decode('utf-8'))
    # print(search_results)
    # await ctx.send('https://music.youtube.com/watch?v=' + search_results[0])
    # await ctx.send('https://music.youtube.com/watch?v=' + search_results[1])

<div class="message">Lamentablemente, YouTube\xc2\xa0Music no est\xc3\xa1 optimizado para tu navegador. 
Verifica si hay actualizaciones o usa Google\xc2\xa0Chrome.</div><div class="cta-wrapper">
<a class="cta" href="http://www.google.com/chrome/index.html">Descargar Chrome</a></div></div></body></html>'
'''



class Youtube(commands.Cog, name="Youtube"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="yt")
    async def yt(self, ctx: commands.Context, *, search):
        """A search command in youtube library.
        Usage:
        ```
        ?yt "The doors"
        ```
        """
        query_string = urllib.parse.urlencode({'search_query': search})
        html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
        search_results = re.findall('watch\?v=(.{11})', html_content.read().decode('utf-8'))
        print(search_results)
        # respond to the message
        await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])
        if search_results[0] != search_results[1]:
            await ctx.send('https://www.youtube.com/watch?v=' + search_results[1])

        #await ctx.send(embed=embed_success("Pong!"))


# This function will be called when this extension is loaded.
# It is necessary to add these functions to the bot.
def setup(bot: commands.Bot):
    bot.add_cog(Youtube(bot))
