## Build and up project:

1. Copy **scrapy.env** file and name it **.env**

2. Run command `./scripts/up.sh`

## Down project

`./scripts/down.sh`

## Run crawlers

1. Change the project name in **.env** file 
(project names can be found in the **scrapy/scrapy.cfg** file)

2. Run the command to display available spider names:
`./scripts/scrapy.sh list`

3. Use the following command to run the parsing:
`./scripts/scrapy.sh crawl <spider_name>`

4. Use the following command to run the ym parsing with proxy:
`./scripts/scrapy.sh crawl yandex_market -s CUSTOM_PROXY="<proxy>"`