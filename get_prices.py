import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

def is_content_valid(content, bestbuy_content=False) -> bool:
    if content is None:
        return False
    
    if bestbuy_content:
        if content.find(class_='priceView-customer-price') is None:
            return False
        elif content.find(class_='priceView-customer-price').find('span') is None:
            return False

    else:
        if content.find(class_='price-current') is None:
            return False
        elif content.find(class_='price-current').find('strong') is None:
            return False


def get_newegg_price(url) -> float:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    response = requests.get(url, headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')

    if content is not None:
        price = 0.0
        if content.find(class_='price-current') is not None and content.find(class_='price-current').find('strong') is not None:
            price = content.find(class_='price-current').find('strong').text
        else:
            print('Error: price not found for url: ' + url)
            return price
        price = price.replace(',', '')
        price = price.replace('$', '')
        price = float(price)
        return price
    else:
        print('Error: content is None for url: ' + url)
        return None

def get_newegg_prices(product_names) -> dict:
    prices = {}
    for product_name in product_names:
        product_name_url = product_name.replace(' ', '+')
        url = 'https://www.newegg.com/p/pl?d=' + product_name_url
        price = get_newegg_price(url)
        if price is not None:
            print(product_name + ': ' + str(price))
        prices[product_name] = price
    return prices

#database file: "FPS Video Games.csv"
#sample of the FPS databse:
#id,CpuName,CpuNumberOfCores,CpuNumberOfThreads,CpuBaseClock,CpuCacheL1,CpuCacheL2,CpuCacheL3,CpuDieSize,CpuFrequency,CpuMultiplier,CpuMultiplierUnlocked,CpuProcessSize,CpuTDP,CpuNumberOfTransistors,CpuTurboClock,GpuName,GpuArchitecture,GpuBandwidth,GpuBaseClock,GpuBoostClock,'GpuBus,GpuNumberOfComputeUnits,GpuDieSize,GpuDirectX,GpuNumberOfExecutionUnits,GpuFP32Performance,GpuMemoryBus,GpuMemorySize,GpuMemoryType,GpuOpenCL,GpuOpenGL,GpuPixelRate,GpuProcessSize,GpuNumberOfROPs,GpuShaderModel,GpuNumberOfShadingUnits,GpuNumberOfTMUs,GpuTextureRate,GpuNumberOfTransistors,GpuVulkan,GameName,GameResolution,GameSetting,Dataset,FPS
#1,Intel Core i7-920,4,8,133,256,1024,8,0.000263,2666,20,0,45,130,731,2933,AMD Radeon RX 480,GCN 4.0,256000,1120,1266,PCIe 3.0 x16,36,0.000232,12,?,5834000,256,8000,GDDR5,2,4.6,40510,14,32,6.4,2304,144,182300,5700,1.2.131,counterStrikeGlobalOffensive,1080,low,userbenchmark,70

def get_data():
    df = pd.read_csv('FPS Video Games.csv', low_memory=False)
    return df

def get_all_gpu_names():
    db = get_data()
    gpu_names = db['GpuName'].unique()
    return gpu_names

def get_all_cpu_names():
    db = get_data()
    cpu_names = db['CpuName'].unique()
    return cpu_names

def make_gpu_prices_db():
    gpus = get_all_gpu_names()
    gpu_prices = get_newegg_prices(gpus)

    gpu_prices_df = pd.DataFrame(gpu_prices.items(), columns=['GpuName', 'Price'])
    gpu_prices_df.to_csv('gpu_prices.csv', index=False)

def make_cpu_prices_db():
    cpus = get_all_cpu_names()
    cpu_prices = get_newegg_prices(cpus)

    cpu_prices_df = pd.DataFrame(cpu_prices.items(), columns=['CpuName', 'Price'])
    cpu_prices_df.to_csv('cpu_prices.csv', index=False)

make_gpu_prices_db()
make_cpu_prices_db()