import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'original'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # Extraer elementos "a" por cada pais
        countries = response.xpath('//td/a')

        # Hacer un "bucle for" a la lista "countries"
        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # URL Absoluto
            # absolute_url = f'https://www.worldometers.info/{link}'  # concatenar los links con "cadenas f"
            # absolute_url = response.urljoin(link)  # concatenar los links con urljoin
            # yield scrapy.Request(url=absolute_url)  # enviar una solicitud con el url absoluto

            # Devolver URL relativo (enviar una solicitud con el url relativo)
            yield response.follow(url=link, callback=self.parse_country, meta={'country':country_name})

    # Obtener data dentro del "link"
    def parse_country(self, response):
        # Obtener el nombre del pais (country) y cada fila (rows) dentro de la tabla poblacion
        country = response.request.meta['country']
        rows = response.xpath("(//table[contains(@class,'table')])[1]/tbody/tr")  # Tambien puesdes usar el valor de clase completo --> response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        # Hacer un "bucle for" a la lista "rows"
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            # Devolver URL relativo
            yield {
                'country':country,
                'year': year,
                'population':population,
            }


