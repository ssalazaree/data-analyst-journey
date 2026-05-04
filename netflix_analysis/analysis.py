import pandas as pd

import os

path = os.path.join(os.path.dirname(__file__), "netflix_titles.csv")
df = pd.read_csv(path)

#print(df.head())
#print(df.info())
#print(df.isnull().sum())

"""
RAZÕES PARA ANALISAR ESTE DATASET:

1.Que tipo de conteúdo domina o catálogo da Netflix (filmes vs séries, géneros)?

2.Que países e regiões têm maior presença no catálogo?

3.Como evoluiu o tipo de conteúdo ao longo do tempo?"""

"""
Analysis 1:
👉 Que colunas existem?
Existem 12 colunas. As colunas são: show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in e description.
Parece-me que a coluna "show_id" é um identificador único para cada título, enquanto as outras colunas fornecem informações sobre o tipo de título (filme ou série),
o título em si, o diretor, o elenco, o país de origem, a data em que foi adicionado à plataforma, o ano de lançamento, a classificação de idade, a duração, os gêneros
listados e uma descrição do título.

👉 Que tipo de dados tens? (texto, números, datas)
Os dados que temos são de vários tipos. Temos texto (colunas: type, title, director, cast, country, rating, listed_in e description), números (colunas: 
release_year), datas (coluna: date_added) e uma mistura de texto e números (coluna: duration, que pode conter a duração em minutos para filmes ou o número de temporadas para séries).

👉 Onde há valores em falta?
Em relação a valores em falta, temos os seguintes números:
- director: 2633 valores em falta
- cast: 2867 valores em falta
- country: 167 valores em falta
- date_added: 1 valor em falta
- rating: 86 valores em falta
- duration: 1 valor em falta

👉 Algo estranho ou interessante à primeira vista?
À primeira vista, é interessante notar que a coluna "director" tem um número significativo de valores em falta (2633), o que pode indicar que muitos títulos
não têm um diretor listado. Além disso, a coluna "cast" também tem um número considerável de valores em falta (2867), o que pode sugerir que muitos títulos
não têm um elenco listado. A coluna "country" tem 167 valores em falta, o que pode indicar que alguns títulos não têm um país de origem listado. A coluna
"date_added" tem apenas 1 valor em falta, o que é relativamente baixo. A coluna "rating" tem 86 valores em falta, o que pode indicar que alguns títulos
não têm uma classificação de idade listada. Por fim, a coluna "duration" tem apenas 1 valor em falta, o que é relativamente baixo.

O que é interessante é que, apesar de haver valores em falta em algumas colunas, a maioria dos títulos ainda tem informações suficientes para análise. 
No entanto, é importante considerar como lidar com os valores em falta, dependendo do tipo de análise que se pretende realizar

Feita esta primeira análise, podemos seguir para análises mais específicas, como por exemplo:
- A Netflix tem mais filmes ou séries — e o que isso indica sobre a estratégia da plataforma?
- Qual é a distribuição de gêneros listados? Esta plataforma tem uma variedade de gêneros ou é mais focada em alguns específicos? E como isso pode influenciar a atração de diferentes públicos?
- Que países dominam o catálogo — e existe concentração geográfica? E como isso pode influenciar a diversidade de conteúdo disponível para novos usuários?
- A Netflix adiciona conteúdo recente ou conteúdo antigo à plataforma?- E como isso pode afetar a experiência do usuário?
- Em relação à classificação de idade, a Netflix aposta mais em conteúdo para adultos ou para crianças? Em que medida isso pode influenciar a base de usuários?
- Qual é a distribuição de duração para filmes e séries? A aposta é maior em que formato? Será que a Netflix tem uma estratégia clara em relação à duração dos títulos que oferece?


E em termos de limpeza de dados, podemos considerar:
- Preencher os valores em falta com um valor padrão (por exemplo, "Desconecido" para colunas de texto ou dropna() para remover os registros que têm valores em falta).
- Analisar os registros com valores em falta para entender se há algum padrão ou motivo específico para a ausência de dados. em seguida, decidir como lidar com esses registros (por exemplo,
preenchendo os valores em falta com base em outras informações disponíveis ou removendo-os da análise).
"""

#print(df["type"].value_counts())

"""A Netflix tem mais filmes do que séries. Existem 5377 filmes e 2087 séries na plataforma. Isso pode indicar que a estratégia da Netflix é focada em oferecer uma variedade maior de filmes para
atrair um público mais amplo, enquanto as séries podem ser uma parte importante, mas não tão dominante do catálogo. No entanto, é importante considerar outros fatores, como a popularidade
e a qualidade dos títulos, para entender melhor a estratégia da plataforma."""

#print(df["listed_in"].value_counts())

"""A distribuição de gêneros listados na Netflix é bastante variada, com uma ampla gama de gêneros representados. Os gêneros mais comuns incluem "Dramas", "Comédias", "Filmes de Ação",
"Filmes de Suspense", "Filmes de Terror" e "Filmes de Ficção" entre outros. Isso indica que a Netflix tem uma estratégia de oferecer uma variedade de gêneros para atrair diferentes públicos.
A diversidade de gêneros pode ser um fator importante para a atração de novos usuários, pois permite que a plataforma atenda a uma ampla gama de interesses e preferências. Além disso,
a variedade de gêneros pode ajudar a manter os usuários engajados. Ainda assim, é de reparar que grande parte dos títulos listados tem em falta o gênero, o que pode dificultar a análise 
completa da distribuição de gêneros na plataforma e perceber até que ponto a Netflix tem uma estratégia clara em relação à variedade de gêneros que oferece. Portanto, é importante considerar
como lidar com os valores em falta na coluna "listed_in" para obter uma análise mais precisa da distribuição de gêneros na Netflix."""

#print(df["country"].value_counts())

"""Os países que dominam o catálogo da Netflix são os Estados Unidos, Índia, Reino Unido, Canadá e França. Isso indica que há uma concentração geográfica significativa de títulos provenientes
desses países. A presença dominante dos Estados Unidos pode ser atribuída à indústria cinematográfica e televisiva robusta do país, que produz uma grande quantidade de conteúdo para a plataforma.
A Índia também tem uma indústria de entretenimento vibrante, o que pode explicar sua presença significativa no catálogo da Netflix. O Reino Unido, Canadá e França também têm indústrias de
entretenimento ativas, o que pode contribuir para sua presença no catálogo. O facto de haver uma maior divulgação de títulos provenientes desses países pode influenciar a diversidade de conteúdo
disponível para os usuários, já que pode haver uma maior representação de culturas e estilos de produção"""

#print(df["release_year"].value_counts())

"""O catálogo da Netflix é mais focado em conteúdo recente, com a maioria dos títulos lançados nos últimos anos. Os anos mais comuns de lançamento são 2018, 2017, 2016 e 2019. Isso indica que a
Netflix tem uma estratégia de oferecer conteúdo atualizado e relevante para os usuários, o que pode ser um fator importante para atrair e reter assinantes. No entanto, também há uma presença
significativa de títulos lançados em anos anteriores, o que sugere que a plataforma também valoriza a diversidade de conteúdo, incluindo títulos clássicos e antigos. A presença de títulos lançados
em anos anteriores pode proporcionar aos usuários uma variedade de opções e permitir que eles explorem diferentes épocas e estilos de produção. Seria interessante cruzar com outro dataset para
perceber qual é a idade média de espectadores da Netflix e perceber se a aposta em conteúdo recente é mais direcionada para um público mais jovem ou se também atrai um público mais amplo."""

#print(df["rating"].value_counts())

"""Em relação à classificação de idade, a Netflix tem uma variedade de conteúdo para diferentes faixas etárias. Os títulos mais comuns são classificados como "TV-MA" (conteúdo para adultos), "TV-14"
(conteúdo para adolescentes) e "TV-PG" (conteúdo para crianças). Isso indica que a Netflix tem uma estratégia de oferecer conteúdo para uma ampla gama de públicos, incluindo adultos, adolescentes 
e crianças. A presença significativa de títulos classificados como "TV-MA" sugere que a plataforma tem uma forte aposta em conteúdo para adultos, o que pode ser um fator importante para atrair e
reter assinantes nessa faixa etária. No entanto, a presença de títulos classificados como "TV-14" e "TV-PG" também indica que a Netflix valoriza a diversidade de conteúdo e busca atender às 
necessidades de diferentes grupos demográficos. Isto poderá indicar que a Netflix tem uma estratégia clara em relação à oferta de conteúdo para diferentes faixas etárias, o que pode ser um fator importante
para a atração e retenção de assinantes."""

#print(df["duration"].value_counts())

"""A netflix tem uma variedade de durações para filmes e séries. Para filmes, as durações mais comuns são 90 min, 100 min, 80 min e 110 min. Para séries, as durações mais comuns são 1 Season, 
2 Seasons, 3 Seasons e 4 Seasons. Isso indica que a Netflix tem uma estratégia de oferecer uma variedade de formatos para atender às preferências dos usuários. A presença significativa de filmes
com durações em torno de 90 a 110 minutos sugere que a plataforma valoriza títulos que podem ser assistidos em uma única sessão, o que pode ser atraente para os usuários que buscam entretenimento
rápido e fácil. Por outro lado, a presença de séries com várias temporadas indica que a Netflix também valoriza conteúdo que pode manter os usuários engajados por um período mais longo, o que pode
ser um fator importante para a retenção de assinantes. A diversidade de durações para filmes e séries mostra que a Netflix tem uma estratégia clara em relação à oferta de diferentes formatos para
atender às necessidades e preferências dos usuários."""

"""Proximo passo: analisar a relação entre as colunas, por exemplo: 
-cruzar a coluna "type" com a coluna "duration" para perceber se há uma tendência clara em relação à duração dos filmes e séries oferecidos pela Netflix.
-cruzar a coluna "release_year" com a coluna "rating" para perceber se há uma tendência em relação à classificação de idade dos títulos lançados em diferentes anos.
-Além disso, seria interessante analisar a relação entre a coluna "country" e a coluna "listed_in" para perceber se há uma concentração de gêneros específicos em determinados países."""

print(df.groupby("type")["release_year"].mean())

"""Filmes são mais antigos que séries?
Em média, os filmes na Netflix foram lançados em 2015, enquanto as séries foram lançadas em 2017. Isso sugere que a Netflix tem uma estratégia de oferecer conteúdo mais recente para séries, 
enquanto os filmes podem incluir uma mistura de títulos mais antigos e recentes. A presença de filmes mais antigos pode ser atraente para os usuários que buscam títulos clássicos ou que desejam
explorar diferentes épocas de produção cinematográfica. Por outro lado, a aposta em séries mais recentes pode ser um fator importante para atrair e reter assinantes que buscam conteúdo atualizado 
e relevante."""

print(df.groupby("country")["type"].value_counts())

"""Que países produzem mais séries vs filmes? 
Os Estados Unidos produzem mais filmes do que séries, enquanto a Índia tem uma presença significativa tanto em filmes quanto em séries. O Reino Unido, Canadá
e França também têm uma presença significativa em ambos os tipos de conteúdo, mas a proporção entre filmes e séries pode variar."""

print(df.groupby("rating")["type"].value_counts())

#Conteúdo adulto é mais filme ou série?

print(df.groupby("release_year")["type"].value_counts().unstack())

#Séries estão a crescer ao longo do tempo?

print(df["listed_in"].str.split(", "))
print(df["listed_in"].str.split(", ").explode().value_counts())

"""Exemplo de uma boa análise de dados:

Insight:
Netflix tem mais filmes que séries.

Evidência:
5377 filmes vs 2087 séries.

Limitação:
Não sabemos se isto reflete estratégia atual ou histórico acumulado."""

"""“Alguns países produzem mais séries que filmes”"""

groupby_country_type = df.groupby("country")["type"].value_counts().unstack()
print(groupby_country_type)

"""Insight:

Existem diferenças na proporção de filmes e séries entre países.

Evidência:

A análise por país mostra que:

Estados Unidos e Índia têm uma forte predominância de filmes
Países como Reino Unido e Canadá apresentam uma distribuição mais equilibrada
Quando analisado em proporção (normalizado), alguns países têm relativamente mais séries do que aparenta nos números absolutos

Limitação:

A coluna country não garante o país real de produção, podendo incluir coproduções ou classificações inconsistentes, o que pode influenciar a interpretação."""

#Séries estão a crescer ao longo do tempo?

df.groupby("release_year")["type"].value_counts().unstack()
print(df.groupby("release_year")["type"].value_counts().unstack())  

"""Insight:

A proporção de séries tem vindo a aumentar ao longo do tempo.

Evidência:

A análise por release_year indica que:

Nos anos mais antigos, os filmes dominam claramente
Nos anos mais recentes, a percentagem de séries aumenta significativamente
Quando analisado em proporção (normalizado), observa-se um crescimento relativo das séries face aos filmes
Limitação:

A variável release_year representa o ano de lançamento original e não a data de entrada na Netflix (date_added), o que pode distorcer conclusões sobre a estratégia da plataforma ao longo do tempo."""

print(df.groupby("release_year")["type"].value_counts(normalize=True).unstack())