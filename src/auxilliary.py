"""
Author: Godwin Chierika Eke
Email: https://mailto:ekegodwinc@gmail.com
Github: https://githubcom/GodwinEke

get_integer: Assumes prompt as None by default,
             Takes in prompt and converts to string,
             Reads input from user and returns data if data is an integer, 

formatted: Assumes word as str,
           Returns the word in lowercase 
           and stripped from whitespaces or trailing spaces.

requests: Perform HTTP requests via aiohttp

"""


import asyncio
import aiohttp

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_integer(prompt=None):
    """
    Assumes prompt as None by default,
    Takes in prompt and converts to string,
    Reads input from user and returns data if data is an integer, 
    """
    if prompt is None:
        prompt = 'Number: '
    while True:
        try:
            num = int(input(str(prompt)))
            if type(num) == int:
                return num
        except ValueError:
            print('\nInvalid number\n')
            continue
    
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
def formatted(word) -> str:
    """"
    Assumes word as str,
    Returns the word in lowercase and stripped from whitespaces or trailing spaces.
    """
    return word.strip().lower()

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
async def _request(session, url):
    """
    Assumes url as str,
    Makes a GET request to url,
    Returns a JSON file
    """
    async with session.get(url) as response:
        return await response.json()


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
async def _get_tasks(session, urls):
    """
    Collectively creates a task to be added to the
    event loop to execute all tasks simultaneously
    """
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(_request(session, url)))
    
    return await asyncio.gather(*tasks)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
async def requests(urls, key=None):
    """Perform HTTP requests via aiohttp"""
    
    if key is not None:
        async with aiohttp.ClientSession(auth=aiohttp.BasicAuth('apikey', key)) as session:
            data = await _get_tasks(session, urls)
    else:
        async with aiohttp.ClientSession() as session:
            data = await _get_tasks(session, urls)
    return data
