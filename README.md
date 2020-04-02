# covid-19-sc-data
Análise de dados sobre a evolução da epidemia de COVID-19 em Santa Catarina

## Motivação
No Estado de Santa Catarina, as prefeituras têm tomado iniciativas distintas de políticas públicas relacionadas à contenção do espalhamento do novo coronavirus. Alguns municípios tomam medidas mais restritivas, ao passo que outros pretendem iniciar uma flexibilização. Isso torna importante uma análise temporal da evolução da doença a nível de município, de modo a permitir comparações e identificar a eficácia das medidas tomadas ao longo do tempo.

Os principais grupos de mídia em SC, a [NSC](https://www.nsctotal.com.br/coronavirus/mapa-de-evolucao-do-virus) e [RIC](https://ndmais.com.br/coronavirus/mapa-coronavirus), têm divulgado paineis (ou mapas) interativos com a evolução dos casos. Apesar de louváveis, as iniciativas ainda pecam por três motivos:

* Não permitir o *drill down* das séries temporais por município;
* Não incluir dados estruturados sobre as medidas que estão sendo tomadas em cada município;
* Não divulgar os dados brutos utilizados para a construção dos *dashboards*.

O governo de SC tampouco está sensível à disponibilização de dados brutos para facilitar esta análise por cidadãos comuns e a academia. As divulgações se resumem a boletins diários, com os dados perdidos no meio de boletins de texto ou, pior, em [imagens PNG](http://www.coronavirus.sc.gov.br/boletins/).

Assim, a ideia deste repositório é manter um *dataset* atualizado de casos, estruturado de acordo com as boas práticas de ciência de dados, além de notebooks com análises a partir destas informações.

## Notebooks com análises

* [Tutorial de uso e análise temporal simples](https://github.com/zelacerda/covid-19-sc-data/blob/master/corona_sc.ipynb)

## Dataset (atualizado com dados de 2/4)

* [Dataset](https://github.com/zelacerda/covid-19-sc-data/blob/master/dataset.csv)

## To-do

* Inclusão de dataset com medidas tomadas pelas prefeituras, se possível indicando a data em que elas entraram em vigor;
* Dados de evolução de mortes e recuperações, a medida em que forem sendo divulgados.
