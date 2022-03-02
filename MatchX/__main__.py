# -*- coding: utf-8 -*-

import os
import re
import json
import requests
import concurrent.futures
from MatchX.core import logger
from MatchX.core.logger import banner
from colorama import Fore, Style
from MatchX.core.logger import blue, reset, green, yellow
from MatchX.core.cli import url, urls, match_regex, match_words, method, data , timeout, verify, user_agent, threads, output, cookies, verbose
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from importlib.metadata import version
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

matchx_version = version('matchx')
print(banner)
print("[" + blue + 'INF' + reset + "]",f'MatchX Engine ({green}v{matchx_version}{reset})')
print("[" + yellow + 'WRN' + reset + "]",'Developers assume no liability and are not responsible for any misuse or damage.')
print('')

if url:
    url = url.strip()
    pass
elif urls:
    pass
else:
    os.system('matchx -h')
    exit()

dict = {
    "URL": "",
    "Status": None,
    "Matched": False,
}

if urls:
    try:
        with open(urls) as _urls:
            read_urls = _urls.read().splitlines()
    except FileNotFoundError:
        logger.error(f'{urls} not found!')
        exit()
if match_regex:
    try:
        with open(match_regex) as _match_regex:
            read_regex = _match_regex.read().splitlines()
    except FileNotFoundError:
        logger.error(f'{match_regex} not found!')
        exit()
if match_words:
    try:
        with open(match_words) as _match_words:
            read_words = _match_words.read().splitlines()
    except FileNotFoundError:
        logger.error(f'{match_words} not found!')
        exit()


def scan(url, match):
    try:
        if method == "GET":
            req = requests.get(url, timeout=timeout, verify=verify,headers=user_agent, cookies=cookies)
            code = req.status_code
            content = req.text
        elif method == "POST":
            req = requests.post(url, data=data, timeout=timeout, verify=verify, headers=user_agent, cookies=cookies)
            code = req.status_code
            content = req.text
        else:
            pass
    except requests.exceptions.HTTPError as errh:
        logger.error('HTTP Error: '+errh)
    except requests.exceptions.ConnectionError as errc:
        logger.error('Connection Error: '+errc)
    except requests.exceptions.Timeout as errt:
        logger.error("Timeout Error: "+errt)
    except requests.exceptions.RequestException as err:
        logger.error("Unexpected Error: "+err)
    except KeyboardInterrupt:
        logger.error("Interrupt (CTRL+C).")

    if not code == 404 or 403:
        if match_regex:
            findit = re.findall(fr'{match}', content)
            if findit:
                logger.good(f"{Fore.CYAN}{Style.BRIGHT} [{match}]{Style.RESET_ALL} " + url+f' [{Fore.YELLOW}{len(findit)} time matched{Style.RESET_ALL}]')
                dict["URL"] = url
                dict["Status"] = code
                dict["Regex"] = match
                dict["Matched"] = True

                json_object = json.dumps(dict, indent=4)

                with open(output, "a") as outfile:
                    outfile.write(json_object)
                    outfile.write('\n')
            else:
                if verbose:
                    logger.info(f'{Fore.CYAN} [{match}]{Style.RESET_ALL} {Style.DIM}'+url +f'{Style.RESET_ALL} {Fore.RED}{Style.BRIGHT}[Not found]{Style.RESET_ALL}')
                else:
                    pass
        elif match_words:
            if match in content:
                logger.good(f"{Fore.CYAN}{Style.BRIGHT} [{match}]{Style.RESET_ALL} " + url)

                dict["URL"] = url
                dict["Status"] = code
                dict["Word"] = match
                dict["Matched"] = True

                json_object = json.dumps(dict, indent=4)

                with open(output, "a") as outfile:
                    outfile.write(json_object)
                    outfile.write('\n')
            else:
                if verbose:
                    logger.info(f'{Fore.CYAN} [{match}]{Style.RESET_ALL} {Style.DIM}'+url +f'{Style.RESET_ALL} {Fore.RED}{Style.BRIGHT}[Not found]{Style.RESET_ALL}')
                else:
                    pass
    else:
        logger.error('404/403: '+url)


def main():
    try:
        global url
        global urls

        if url:
            if match_regex:
                with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                    for regex in read_regex:
                        executor.submit(scan, url, regex)
            elif match_words:
                with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                    for word in read_words:
                        executor.submit(scan, url, word)
            else:
                logger.error("String/Regex not Specified!")
                exit()

        elif urls:
            if match_regex:
                with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                    for url in read_urls:
                        for regex in read_regex:
                            executor.submit(scan, url.strip(), regex)
            elif match_words:
                with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
                    for url in read_urls:
                        for word in read_words:
                            executor.submit(scan, url.strip(), word)
            else:
                logger.error("String/Regex not Specified!")
                exit()
    except KeyboardInterrupt:
        logger.error("Interrupt (CTRL+C).")
