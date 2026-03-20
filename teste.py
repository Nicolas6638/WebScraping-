import requests

def buscar_pagina(url):
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    return response


if __name__ == "__main__":
    url = 'https://www.mercadolivre.com.br/apple-iphone-16-256-gb-preto-distribuidor-autorizado/p/MLB1040287796#polycard_client=search-desktop&search_layout=grid&position=2&type=product&tracking_id=962e90aa-c7f9-48ad-9a0a-4cfab0e325a5&wid=MLB3931272075&sid=search'

    url_2 = 'https://www.mercadolivre.com.br/console-playstation5-slim-digital-pacote-astro-bot-e-gran-turismo-7-branco/p/MLB57081243#polycard_client=search-desktop&search_layout=grid&position=1&type=product&tracking_id=23e12b8b-648f-49d9-b369-8d6bf12ee174&wid=MLB4214670787&sid=search'
    conteudo_pagina = buscar_pagina(url)
    conteudo_pagina2 = buscar_pagina(url_2)

    print(conteudo_pagina)
    print(conteudo_pagina2)