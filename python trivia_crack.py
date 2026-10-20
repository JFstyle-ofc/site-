import tkinter as tk
from tkinter import font, messagebox
import random
import math
import json
import os
from datetime import datetime

# Tentar importar winsound apenas no Windows
try:
    import winsound
    SOUND_ENABLED = True
except:
    SOUND_ENABLED = False

# ===== BANCO DE PERGUNTAS COMPLETO =====
PERGUNTAS = {
    "Esportes": [
        {"pergunta": "Quantos jogadores tem um time de futebol em campo?", "opcoes": ["11", "10", "9", "12"], "resposta": "11", "dificuldade": "Fácil", "emoji": "⚽"},
        {"pergunta": "Em que esporte se usa uma 'cesta' para marcar pontos?", "opcoes": ["Basquete", "Vôlei", "Futebol", "Tênis"], "resposta": "Basquete", "dificuldade": "Fácil", "emoji": "🏀"},
        {"pergunta": "Qual desses é um esporte aquático?", "opcoes": ["Natação", "Ciclismo", "Atletismo", "Ginástica"], "resposta": "Natação", "dificuldade": "Fácil", "emoji": "🏊"},
        {"pergunta": "Uma partida de vôlei é disputada em melhor de quantos sets?", "opcoes": ["5", "3", "7", "9"], "resposta": "5", "dificuldade": "Fácil", "emoji": "🏐"},
        {"pergunta": "Qual país é popularmente chamado de 'país do futebol'?", "opcoes": ["Brasil", "Argentina", "Alemanha", "Espanha"], "resposta": "Brasil", "dificuldade": "Fácil", "emoji": "🇧🇷"},
        {"pergunta": "Qual desses é um esporte de raquete?", "opcoes": ["Tênis", "Futebol", "Basquete", "Vôlei"], "resposta": "Tênis", "dificuldade": "Fácil", "emoji": "🎾"},
        {"pergunta": "Em qual esporte se usa um taco para rebater uma bola?", "opcoes": ["Beisebol", "Futebol", "Basquete", "Natação"], "resposta": "Beisebol", "dificuldade": "Fácil", "emoji": "⚾"},
        {"pergunta": "Qual desses é um esporte de combate?", "opcoes": ["Judô", "Futebol", "Vôlei", "Basquete"], "resposta": "Judô", "dificuldade": "Fácil", "emoji": "🥋"},
        {"pergunta": "Qual esporte é praticado em uma pista de gelo?", "opcoes": ["Patinação", "Natação", "Atletismo", "Ciclismo"], "resposta": "Patinação", "dificuldade": "Fácil", "emoji": "⛸️"},
        {"pergunta": "Qual desses é um esporte olímpico?", "opcoes": ["Atletismo", "Xadrez", "Pôquer", "Damas"], "resposta": "Atletismo", "dificuldade": "Fácil", "emoji": "🏃"},
        {"pergunta": "Em que cidade brasileira ocorreram as Olimpíadas de 2016?", "opcoes": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"], "resposta": "Rio de Janeiro", "dificuldade": "Médio", "emoji": "🏅"},
        {"pergunta": "Qual tenista brasileiro venceu Roland Garros três vezes?", "opcoes": ["Gustavo Kuerten", "Thomaz Bellucci", "João Fonseca", "Marcelo Melo"], "resposta": "Gustavo Kuerten", "dificuldade": "Médio", "emoji": "🎾"},
        {"pergunta": "Quantos anéis tem a bandeira olímpica?", "opcoes": ["5", "4", "6", "7"], "resposta": "5", "dificuldade": "Médio", "emoji": "🔄"},
        {"pergunta": "Quais países sediarão a Copa do Mundo de 2026?", "opcoes": ["EUA, México e Canadá", "Brasil e Argentina", "Catar e Arábia Saudita", "Alemanha e França"], "resposta": "EUA, México e Canadá", "dificuldade": "Médio", "emoji": "🌍"},
        {"pergunta": "Qual foi o primeiro país a sediar uma Copa do Mundo de futebol?", "opcoes": ["Uruguai", "Brasil", "Itália", "França"], "resposta": "Uruguai", "dificuldade": "Médio", "emoji": "🏆"},
        {"pergunta": "Qual a distância oficial de uma maratona?", "opcoes": ["42,195 km", "40 km", "45 km", "50 km"], "resposta": "42,195 km", "dificuldade": "Médio", "emoji": "🏃"},
        {"pergunta": "Qual esporte usa a expressão 'touchdown'?", "opcoes": ["Futebol Americano", "Rugby", "Futebol", "Basquete"], "resposta": "Futebol Americano", "dificuldade": "Médio", "emoji": "🏈"},
        {"pergunta": "Em que ano foi realizada a primeira Copa do Mundo de futebol?", "opcoes": ["1930", "1920", "1940", "1950"], "resposta": "1930", "dificuldade": "Médio", "emoji": "🌎"},
        {"pergunta": "Qual jogador é conhecido como 'Rei do Futebol'?", "opcoes": ["Pelé", "Maradona", "Messi", "Cristiano Ronaldo"], "resposta": "Pelé", "dificuldade": "Médio", "emoji": "👑"},
        {"pergunta": "Quantos pontos vale um arremesso de 3 pontos no basquete?", "opcoes": ["3", "2", "1", "4"], "resposta": "3", "dificuldade": "Médio", "emoji": "🏀"},
        {"pergunta": "Quem é o maior artilheiro da história das Copas do Mundo de futebol?", "opcoes": ["Miroslav Klose", "Pelé", "Ronaldo Fenômeno", "Lionel Messi"], "resposta": "Miroslav Klose", "dificuldade": "Difícil", "emoji": "⚽"},
        {"pergunta": "Em que ano o futebol masculino brasileiro conquistou seu primeiro ouro olímpico?", "opcoes": ["2016", "2012", "2008", "2004"], "resposta": "2016", "dificuldade": "Difícil", "emoji": "🥇"},
        {"pergunta": "Qual seleção venceu a primeira Copa do Mundo feminina de futebol?", "opcoes": ["Estados Unidos", "China", "Noruega", "Alemanha"], "resposta": "Estados Unidos", "dificuldade": "Difícil", "emoji": "🇺🇸"},
        {"pergunta": "Quantas Copas do Mundo a Alemanha já conquistou?", "opcoes": ["4", "3", "5", "2"], "resposta": "4", "dificuldade": "Difícil", "emoji": "🇩🇪"},
        {"pergunta": "Quem detém o recorde de mais medalhas olímpicas?", "opcoes": ["Michael Phelps", "Usain Bolt", "Larisa Latynina", "Carl Lewis"], "resposta": "Michael Phelps", "dificuldade": "Difícil", "emoji": "🏊"},
        {"pergunta": "Qual é o esporte mais antigo do mundo?", "opcoes": ["Atletismo", "Natação", "Luta", "Arco e Flecha"], "resposta": "Atletismo", "dificuldade": "Difícil", "emoji": "🏃"},
        {"pergunta": "Em que modalidade a ginasta Simone Biles é famosa?", "opcoes": ["Ginástica Artística", "Ginástica Rítmica", "Trampolim", "Acrobática"], "resposta": "Ginástica Artística", "dificuldade": "Difícil", "emoji": "🤸"},
        {"pergunta": "Qual país é o maior vencedor da Copa do Mundo de Rugby?", "opcoes": ["Nova Zelândia", "África do Sul", "Austrália", "Inglaterra"], "resposta": "Nova Zelândia", "dificuldade": "Difícil", "emoji": "🏉"},
        {"pergunta": "Quantas voltas tem uma corrida de Fórmula 1 em Mônaco?", "opcoes": ["78", "70", "80", "65"], "resposta": "78", "dificuldade": "Difícil", "emoji": "🏎️"},
        {"pergunta": "Qual boxeador é conhecido como 'The Greatest'?", "opcoes": ["Muhammad Ali", "Mike Tyson", "Joe Frazier", "George Foreman"], "resposta": "Muhammad Ali", "dificuldade": "Difícil", "emoji": "🥊"},
    ],
    "Entretenimento": [
        {"pergunta": "Qual desses é um personagem da Disney?", "opcoes": ["Mickey Mouse", "Batman", "Homem-Aranha", "Wolverine"], "resposta": "Mickey Mouse", "dificuldade": "Fácil", "emoji": "🐭"},
        {"pergunta": "Em qual plataforma se assiste séries de streaming?", "opcoes": ["Netflix", "Spotify", "WhatsApp", "PayPal"], "resposta": "Netflix", "dificuldade": "Fácil", "emoji": "📺"},
        {"pergunta": "Qual é o protagonista de 'Harry Potter'?", "opcoes": ["Harry Potter", "Ron Weasley", "Draco Malfoy", "Neville"], "resposta": "Harry Potter", "dificuldade": "Fácil", "emoji": "⚡"},
        {"pergunta": "Qual desses é um instrumento musical?", "opcoes": ["Violão", "Pincel", "Martelo", "Régua"], "resposta": "Violão", "dificuldade": "Fácil", "emoji": "🎸"},
        {"pergunta": "Quem interpretou o Coringa em 2019?", "opcoes": ["Joaquin Phoenix", "Heath Ledger", "Jared Leto", "Jack Nicholson"], "resposta": "Joaquin Phoenix", "dificuldade": "Fácil", "emoji": "🎭"},
        {"pergunta": "Qual desses é um filme de animação da Pixar?", "opcoes": ["Toy Story", "Shrek", "Ice Age", "Madagascar"], "resposta": "Toy Story", "dificuldade": "Fácil", "emoji": "🎬"},
        {"pergunta": "Qual banda é conhecida como 'The Beatles'?", "opcoes": ["Inglesa", "Americana", "Australiana", "Alemã"], "resposta": "Inglesa", "dificuldade": "Fácil", "emoji": "🎵"},
        {"pergunta": "Qual desses é um gênero cinematográfico?", "opcoes": ["Comédia", "Laranja", "Azul", "Verde"], "resposta": "Comédia", "dificuldade": "Fácil", "emoji": "🎭"},
        {"pergunta": "Qual personagem usa um martelo como arma?", "opcoes": ["Thor", "Capitão América", "Homem de Ferro", "Hulk"], "resposta": "Thor", "dificuldade": "Fácil", "emoji": "🔨"},
        {"pergunta": "Qual desses é um jogo de tabuleiro?", "opcoes": ["Xadrez", "Futebol", "Basquete", "Vôlei"], "resposta": "Xadrez", "dificuldade": "Fácil", "emoji": "♟️"},
        {"pergunta": "Onde mora o Bob Esponja?", "opcoes": ["Fenda do Biquíni", "Atlântida", "Coral Ridge", "Baía dos Corais"], "resposta": "Fenda do Biquíni", "dificuldade": "Médio", "emoji": "🧽"},
        {"pergunta": "Em qual universo se passa 'Game of Thrones'?", "opcoes": ["Westeros", "Terra Média", "Narnia", "Hogwarts"], "resposta": "Westeros", "dificuldade": "Médio", "emoji": "🐉"},
        {"pergunta": "Quem dirigiu 'Titanic' e 'Avatar'?", "opcoes": ["James Cameron", "Steven Spielberg", "Christopher Nolan", "Tim Burton"], "resposta": "James Cameron", "dificuldade": "Médio", "emoji": "🎥"},
        {"pergunta": "Qual álbum mais vendido de Michael Jackson?", "opcoes": ["Thriller", "Bad", "Dangerous", "Off the Wall"], "resposta": "Thriller", "dificuldade": "Médio", "emoji": "🎵"},
        {"pergunta": "Em que ano estreou 'Star Wars'?", "opcoes": ["1977", "1980", "1975", "1983"], "resposta": "1977", "dificuldade": "Médio", "emoji": "🌌"},
        {"pergunta": "Qual ator interpretou o Homem de Ferro?", "opcoes": ["Robert Downey Jr.", "Chris Evans", "Chris Hemsworth", "Scarlett Johansson"], "resposta": "Robert Downey Jr.", "dificuldade": "Médio", "emoji": "🤖"},
        {"pergunta": "Qual é o gênero musical do rock 'n' roll?", "opcoes": ["Rock", "Samba", "Forró", "Funk"], "resposta": "Rock", "dificuldade": "Médio", "emoji": "🎸"},
        {"pergunta": "Qual desses é um estúdio de animação japonês?", "opcoes": ["Studio Ghibli", "Disney", "Pixar", "DreamWorks"], "resposta": "Studio Ghibli", "dificuldade": "Médio", "emoji": "🎌"},
        {"pergunta": "Qual filme ganhou o Oscar de Melhor Filme em 2020?", "opcoes": ["Parasita", "1917", "O Irlandês", "Joker"], "resposta": "Parasita", "dificuldade": "Médio", "emoji": "🏆"},
        {"pergunta": "Qual cantora é conhecida como 'Rainha do Pop'?", "opcoes": ["Madonna", "Britney Spears", "Lady Gaga", "Beyoncé"], "resposta": "Madonna", "dificuldade": "Médio", "emoji": "👑"},
        {"pergunta": "Qual filme venceu o Oscar de Melhor Filme em 1994?", "opcoes": ["A Lista de Schindler", "Forrest Gump", "Filadélfia", "O Fugitivo"], "resposta": "A Lista de Schindler", "dificuldade": "Difícil", "emoji": "🎬"},
        {"pergunta": "Quem compôs a trilha de 'O Poderoso Chefão'?", "opcoes": ["Nino Rota", "John Williams", "Hans Zimmer", "Ennio Morricone"], "resposta": "Nino Rota", "dificuldade": "Difícil", "emoji": "🎵"},
        {"pergunta": "Qual foi o primeiro longa da Disney?", "opcoes": ["Branca de Neve", "Pinóquio", "Fantasia", "Dumbo"], "resposta": "Branca de Neve", "dificuldade": "Difícil", "emoji": "🏰"},
        {"pergunta": "Quem escreveu 'O Senhor dos Anéis'?", "opcoes": ["J.R.R. Tolkien", "C.S. Lewis", "George R.R. Martin", "J.K. Rowling"], "resposta": "J.R.R. Tolkien", "dificuldade": "Difícil", "emoji": "📚"},
        {"pergunta": "Qual atriz venceu mais vezes o Oscar?", "opcoes": ["Katharine Hepburn", "Meryl Streep", "Bette Davis", "Ingrid Bergman"], "resposta": "Katharine Hepburn", "dificuldade": "Difícil", "emoji": "🏆"},
        {"pergunta": "Qual diretor é famoso por filmes de terror?", "opcoes": ["Alfred Hitchcock", "Stanley Kubrick", "Quentin Tarantino", "Martin Scorsese"], "resposta": "Alfred Hitchcock", "dificuldade": "Difícil", "emoji": "🎥"},
        {"pergunta": "Qual série venceu mais Emmys de Melhor Série?", "opcoes": ["Game of Thrones", "Breaking Bad", "Mad Men", "West Wing"], "resposta": "Game of Thrones", "dificuldade": "Difícil", "emoji": "📺"},
        {"pergunta": "Qual música é considerada a mais tocada da história?", "opcoes": ["Happy Birthday", "Imagine", "Yesterday", "Let It Be"], "resposta": "Happy Birthday", "dificuldade": "Difícil", "emoji": "🎵"},
        {"pergunta": "Qual ator interpretou o Coringa em 'Batman' (1989)?", "opcoes": ["Jack Nicholson", "Joaquin Phoenix", "Heath Ledger", "Jared Leto"], "resposta": "Jack Nicholson", "dificuldade": "Difícil", "emoji": "🎭"},
        {"pergunta": "Qual é a obra mais famosa de Michelangelo?", "opcoes": ["David", "Pietà", "Moisés", "Capela Sistina"], "resposta": "David", "dificuldade": "Difícil", "emoji": "🎨"},
    ],
    "Arte": [
        {"pergunta": "Qual dessas é uma cor primária?", "opcoes": ["Azul", "Verde", "Roxo", "Laranja"], "resposta": "Azul", "dificuldade": "Fácil", "emoji": "🎨"},
        {"pergunta": "Qual instrumento Beethoven tocava?", "opcoes": ["Piano", "Violino", "Flauta", "Bateria"], "resposta": "Piano", "dificuldade": "Fácil", "emoji": "🎹"},
        {"pergunta": "Onde se veem obras de arte expostas?", "opcoes": ["Museu", "Estádio", "Hospital", "Aeroporto"], "resposta": "Museu", "dificuldade": "Fácil", "emoji": "🏛️"},
        {"pergunta": "Qual técnica de pintura usa pequenos pontos?", "opcoes": ["Pontilhismo", "Cubismo", "Realismo", "Abstrato"], "resposta": "Pontilhismo", "dificuldade": "Fácil", "emoji": "🎨"},
        {"pergunta": "Qual dessas é uma obra tridimensional?", "opcoes": ["Estátua", "Sinfonia", "Romance", "Poema"], "resposta": "Estátua", "dificuldade": "Fácil", "emoji": "🗿"},
        {"pergunta": "Quem pintou 'Monalisa'?", "opcoes": ["Da Vinci", "Michelangelo", "Rafael", "Donatello"], "resposta": "Da Vinci", "dificuldade": "Fácil", "emoji": "🖼️"},
        {"pergunta": "Qual é a técnica de pintura com tinta a óleo?", "opcoes": ["Óleo", "Aquarela", "Guache", "Acrílica"], "resposta": "Óleo", "dificuldade": "Fácil", "emoji": "🖌️"},
        {"pergunta": "Qual movimento artístico é conhecido como 'Renascimento'?", "opcoes": ["Renascimento", "Barroco", "Rococó", "Impressionismo"], "resposta": "Renascimento", "dificuldade": "Fácil", "emoji": "🎭"},
        {"pergunta": "Quem esculpiu 'O Pensador'?", "opcoes": ["Rodin", "Michelangelo", "Donatello", "Bernini"], "resposta": "Rodin", "dificuldade": "Fácil", "emoji": "🗿"},
        {"pergunta": "Qual é o material da escultura 'David'?", "opcoes": ["Mármore", "Bronze", "Madeira", "Ferro"], "resposta": "Mármore", "dificuldade": "Fácil", "emoji": "⛰️"},
        {"pergunta": "Quem pintou 'A Noite Estrelada'?", "opcoes": ["Van Gogh", "Monet", "Picasso", "Dalí"], "resposta": "Van Gogh", "dificuldade": "Médio", "emoji": "🌙"},
        {"pergunta": "Em que país nasceu Pablo Picasso?", "opcoes": ["Espanha", "Itália", "França", "Portugal"], "resposta": "Espanha", "dificuldade": "Médio", "emoji": "🇪🇸"},
        {"pergunta": "Michelangelo pintou qual capela?", "opcoes": ["Capela Sistina", "Basílica de São Pedro", "Catedral de Milão", "Panteão"], "resposta": "Capela Sistina", "dificuldade": "Médio", "emoji": "⛪"},
        {"pergunta": "A qual movimento Dalí está associado?", "opcoes": ["Surrealismo", "Cubismo", "Impressionismo", "Barroco"], "resposta": "Surrealismo", "dificuldade": "Médio", "emoji": "🌪️"},
        {"pergunta": "Quem esculpiu 'O Pensador'?", "opcoes": ["Auguste Rodin", "Michelangelo", "Donatello", "Bernini"], "resposta": "Auguste Rodin", "dificuldade": "Médio", "emoji": "🗿"},
        {"pergunta": "Qual pintor é famoso pelos 'Nenúfares'?", "opcoes": ["Monet", "Van Gogh", "Renoir", "Degas"], "resposta": "Monet", "dificuldade": "Médio", "emoji": "🌺"},
        {"pergunta": "Qual é a obra mais famosa de Picasso?", "opcoes": ["Guernica", "Les Demoiselles d'Avignon", "O Beijo", "A Persistência da Memória"], "resposta": "Guernica", "dificuldade": "Médio", "emoji": "🖼️"},
        {"pergunta": "Qual movimento artístico valoriza a luz e a cor?", "opcoes": ["Impressionismo", "Cubismo", "Surrealismo", "Abstrato"], "resposta": "Impressionismo", "dificuldade": "Médio", "emoji": "☀️"},
        {"pergunta": "Quem pintou 'O Grito'?", "opcoes": ["Munch", "Van Gogh", "Monet", "Picasso"], "resposta": "Munch", "dificuldade": "Médio", "emoji": "😱"},
        {"pergunta": "Qual escultura famosa está em Milão?", "opcoes": ["Pietà", "David", "Moisés", "Laocoonte"], "resposta": "Pietà", "dificuldade": "Médio", "emoji": "⛪"},
        {"pergunta": "Qual artista brasileira pintou 'Abaporu'?", "opcoes": ["Tarsila do Amaral", "Anita Malfatti", "Di Cavalcanti", "Djanira"], "resposta": "Tarsila do Amaral", "dificuldade": "Difícil", "emoji": "🇧🇷"},
        {"pergunta": "A qual movimento pertence Mondrian?", "opcoes": ["Neoplasticismo", "Impressionismo", "Barroco", "Rococó"], "resposta": "Neoplasticismo", "dificuldade": "Difícil", "emoji": "⬜"},
        {"pergunta": "Qual pintor cortou a própria orelha?", "opcoes": ["Van Gogh", "Rembrandt", "Vermeer", "Bosch"], "resposta": "Van Gogh", "dificuldade": "Difícil", "emoji": "👂"},
        {"pergunta": "Quem pintou 'A Escola de Atenas'?", "opcoes": ["Rafael", "Michelangelo", "Da Vinci", "Ticiano"], "resposta": "Rafael", "dificuldade": "Difícil", "emoji": "🏛️"},
        {"pergunta": "Junto com Picasso, quem é precursor do Cubismo?", "opcoes": ["Georges Braque", "Henri Matisse", "Paul Cézanne", "Edgar Degas"], "resposta": "Georges Braque", "dificuldade": "Difícil", "emoji": "🎨"},
        {"pergunta": "Qual é o mais famoso afresco de Michelangelo?", "opcoes": ["A Criação de Adão", "O Juízo Final", "A Última Ceia", "A Escola de Atenas"], "resposta": "A Criação de Adão", "dificuldade": "Difícil", "emoji": "✝️"},
        {"pergunta": "Qual pintor é conhecido como 'o mestre do claro-escuro'?", "opcoes": ["Caravaggio", "Rembrandt", "Vermeer", "Bosch"], "resposta": "Caravaggio", "dificuldade": "Difícil", "emoji": "🎭"},
        {"pergunta": "Qual obra de arte foi roubada e recuperada em 1911?", "opcoes": ["Mona Lisa", "A Noite Estrelada", "O Grito", "Guernica"], "resposta": "Mona Lisa", "dificuldade": "Difícil", "emoji": "🖼️"},
        {"pergunta": "Quem fundou o movimento impressionista?", "opcoes": ["Monet", "Renoir", "Degas", "Manet"], "resposta": "Monet", "dificuldade": "Difícil", "emoji": "🌅"},
        {"pergunta": "Qual é o museu de arte mais visitado do mundo?", "opcoes": ["Louvre", "British Museum", "Metropolitan", "Museu do Vaticano"], "resposta": "Louvre", "dificuldade": "Difícil", "emoji": "🏛️"},
    ],
    "História": [
        {"pergunta": "Quem foi o primeiro imperador do Brasil?", "opcoes": ["Dom Pedro I", "Dom Pedro II", "Getúlio Vargas", "Tiradentes"], "resposta": "Dom Pedro I", "dificuldade": "Fácil", "emoji": "👑"},
        {"pergunta": "Em que continente ficava o Egito Antigo?", "opcoes": ["África", "Ásia", "Europa", "América"], "resposta": "África", "dificuldade": "Fácil", "emoji": "🌍"},
        {"pergunta": "Qual civilização construiu as pirâmides?", "opcoes": ["Egípcia", "Romana", "Grega", "Maia"], "resposta": "Egípcia", "dificuldade": "Fácil", "emoji": "🔺"},
        {"pergunta": "Em que ano começou a Segunda Guerra Mundial?", "opcoes": ["1939", "1914", "1945", "1929"], "resposta": "1939", "dificuldade": "Fácil", "emoji": "💣"},
        {"pergunta": "Tiradentes liderou qual movimento?", "opcoes": ["Inconfidência Mineira", "Revolta da Vacina", "Guerra do Paraguai", "Balaiada"], "resposta": "Inconfidência Mineira", "dificuldade": "Fácil", "emoji": "⚔️"},
        {"pergunta": "Qual foi a primeira capital do Brasil?", "opcoes": ["Salvador", "Rio de Janeiro", "Brasília", "Recife"], "resposta": "Salvador", "dificuldade": "Fácil", "emoji": "🏙️"},
        {"pergunta": "Em que ano o Brasil se tornou república?", "opcoes": ["1889", "1822", "1500", "1900"], "resposta": "1889", "dificuldade": "Fácil", "emoji": "🇧🇷"},
        {"pergunta": "Quem foi o principal líder da Revolução Russa?", "opcoes": ["Lênin", "Stálin", "Trotsky", "Marx"], "resposta": "Lênin", "dificuldade": "Fácil", "emoji": "☭"},
        {"pergunta": "Qual tratado encerrou a Primeira Guerra?", "opcoes": ["Tratado de Versalhes", "Tratado de Tordesilhas", "Tratado de Paris", "Acordo de Yalta"], "resposta": "Tratado de Versalhes", "dificuldade": "Fácil", "emoji": "📜"},
        {"pergunta": "Quem foi a rainha egípcia associada a César?", "opcoes": ["Cleópatra", "Nefertiti", "Hatshepsut", "Ísis"], "resposta": "Cleópatra", "dificuldade": "Fácil", "emoji": "👑"},
        {"pergunta": "Qual tratado dividiu o Novo Mundo em 1494?", "opcoes": ["Tratado de Tordesilhas", "Tratado de Versalhes", "Tratado de Utrecht", "Tratado de Madrid"], "resposta": "Tratado de Tordesilhas", "dificuldade": "Médio", "emoji": "🌍"},
        {"pergunta": "Qual imperador romano se converteu ao cristianismo?", "opcoes": ["Constantino", "Nero", "Júlio César", "Augusto"], "resposta": "Constantino", "dificuldade": "Médio", "emoji": "✝️"},
        {"pergunta": "Qual evento iniciou a Primeira Guerra Mundial?", "opcoes": ["Assassinato de Francisco Ferdinando", "Invasão da Polônia", "Queda do Muro de Berlim", "Revolução Russa"], "resposta": "Assassinato de Francisco Ferdinando", "dificuldade": "Médio", "emoji": "🔫"},
        {"pergunta": "Em que ano foi assinada a Lei Áurea?", "opcoes": ["1888", "1889", "1822", "1850"], "resposta": "1888", "dificuldade": "Médio", "emoji": "📜"},
        {"pergunta": "Qual dinastia governava a China no século XVI?", "opcoes": ["Dinastia Ming", "Dinastia Qing", "Dinastia Tang", "Dinastia Song"], "resposta": "Dinastia Ming", "dificuldade": "Médio", "emoji": "🏯"},
        {"pergunta": "Quem foi o primeiro presidente dos EUA?", "opcoes": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], "resposta": "George Washington", "dificuldade": "Médio", "emoji": "🇺🇸"},
        {"pergunta": "Qual foi a maior guerra da antiguidade?", "opcoes": ["Guerras Púnicas", "Guerra de Tróia", "Invasão Persa", "Conquista de Alexandre"], "resposta": "Guerras Púnicas", "dificuldade": "Médio", "emoji": "⚔️"},
        {"pergunta": "Qual civilização inventou a escrita?", "opcoes": ["Suméria", "Egípcia", "Chinesa", "Indiana"], "resposta": "Suméria", "dificuldade": "Médio", "emoji": "✍️"},
        {"pergunta": "Em que ano caiu o Muro de Berlim?", "opcoes": ["1989", "1987", "1990", "1985"], "resposta": "1989", "dificuldade": "Médio", "emoji": "🧱"},
        {"pergunta": "Quem descobriu a América em 1492?", "opcoes": ["Cristóvão Colombo", "Américo Vespúcio", "Fernão de Magalhães", "Pedro Álvares Cabral"], "resposta": "Cristóvão Colombo", "dificuldade": "Médio", "emoji": "⛵"},
        {"pergunta": "Qual batalha foi decisiva para a independência do Brasil?", "opcoes": ["Independência da Bahia", "Batalha de Pirajá", "Guerra dos Farrapos", "Revolução Pernambucana"], "resposta": "Independência da Bahia", "dificuldade": "Difícil", "emoji": "⚔️"},
        {"pergunta": "Quem foi o último faraó do Egito?", "opcoes": ["Cleópatra VII", "Ramsés II", "Tutancâmon", "Akhenaton"], "resposta": "Cleópatra VII", "dificuldade": "Difícil", "emoji": "👑"},
        {"pergunta": "Qual império foi o maior da história em extensão?", "opcoes": ["Império Mongol", "Império Britânico", "Império Romano", "Império Russo"], "resposta": "Império Mongol", "dificuldade": "Difícil", "emoji": "🌏"},
        {"pergunta": "Em que ano ocorreu a Revolução Francesa?", "opcoes": ["1789", "1776", "1800", "1799"], "resposta": "1789", "dificuldade": "Difícil", "emoji": "🇫🇷"},
        {"pergunta": "Quem foi o fundador do Império Maia?", "opcoes": ["Kukulcán", "Pacal", "Jasaw Chan K'awiil", "Yax K'uk' Mo'"], "resposta": "Kukulcán", "dificuldade": "Difícil", "emoji": "🌴"},
        {"pergunta": "Qual civilização construiu Machu Picchu?", "opcoes": ["Inca", "Maia", "Asteca", "Chibcha"], "resposta": "Inca", "dificuldade": "Difícil", "emoji": "🏔️"},
        {"pergunta": "Em que ano ocorreu a Guerra de Secessão nos EUA?", "opcoes": ["1861", "1865", "1776", "1812"], "resposta": "1861", "dificuldade": "Difícil", "emoji": "🇺🇸"},
        {"pergunta": "Quem foi o líder da Revolução Cubana?", "opcoes": ["Fidel Castro", "Che Guevara", "Raúl Castro", "Camilo Cienfuegos"], "resposta": "Fidel Castro", "dificuldade": "Difícil", "emoji": "🇨🇺"},
        {"pergunta": "Qual foi a primeira cidade do mundo?", "opcoes": ["Çatalhöyük", "Jericó", "Ur", "Babilônia"], "resposta": "Çatalhöyük", "dificuldade": "Difícil", "emoji": "🏛️"},
        {"pergunta": "Quem foi o primeiro imperador romano?", "opcoes": ["Augusto", "Júlio César", "Tibério", "Calígula"], "resposta": "Augusto", "dificuldade": "Difícil", "emoji": "👑"},
    ],
    "Ciência": [
        {"pergunta": "Qual é o maior planeta do Sistema Solar?", "opcoes": ["Júpiter", "Saturno", "Terra", "Netuno"], "resposta": "Júpiter", "dificuldade": "Fácil", "emoji": "🪐"},
        {"pergunta": "Quantos ossos tem o corpo humano adulto?", "opcoes": ["206", "300", "150", "250"], "resposta": "206", "dificuldade": "Fácil", "emoji": "🦴"},
        {"pergunta": "Qual gás os humanos respiram?", "opcoes": ["Oxigênio", "Gás carbônico", "Nitrogênio", "Hidrogênio"], "resposta": "Oxigênio", "dificuldade": "Fácil", "emoji": "💨"},
        {"pergunta": "Qual órgão filtra o sangue?", "opcoes": ["Rim", "Fígado", "Coração", "Pulmão"], "resposta": "Rim", "dificuldade": "Fácil", "emoji": "🫘"},
        {"pergunta": "Qual é um estado físico da matéria?", "opcoes": ["Sólido", "Cor", "Som", "Cheiro"], "resposta": "Sólido", "dificuldade": "Fácil", "emoji": "🧊"},
        {"pergunta": "Qual é o menor planeta do Sistema Solar?", "opcoes": ["Mercúrio", "Vênus", "Marte", "Plutão"], "resposta": "Mercúrio", "dificuldade": "Fácil", "emoji": "☿️"},
        {"pergunta": "Qual é a distância da Terra ao Sol?", "opcoes": ["150 milhões km", "200 milhões km", "100 milhões km", "300 milhões km"], "resposta": "150 milhões km", "dificuldade": "Fácil", "emoji": "🌞"},
        {"pergunta": "Qual é a fórmula da água?", "opcoes": ["H2O", "CO2", "NaCl", "HCl"], "resposta": "H2O", "dificuldade": "Fácil", "emoji": "💧"},
        {"pergunta": "Qual é o maior órgão do corpo humano?", "opcoes": ["Pele", "Fígado", "Coração", "Pulmão"], "resposta": "Pele", "dificuldade": "Fácil", "emoji": "🧍"},
        {"pergunta": "Qual força mantém os planetas em órbita?", "opcoes": ["Gravidade", "Magnetismo", "Eletricidade", "Fricção"], "resposta": "Gravidade", "dificuldade": "Fácil", "emoji": "🌌"},
        {"pergunta": "Quem propôs a teoria da relatividade?", "opcoes": ["Albert Einstein", "Isaac Newton", "Galileu Galilei", "Stephen Hawking"], "resposta": "Albert Einstein", "dificuldade": "Médio", "emoji": "🧠"},
        {"pergunta": "Qual processo as plantas usam para energia?", "opcoes": ["Fotossíntese", "Respiração", "Fermentação", "Digestão"], "resposta": "Fotossíntese", "dificuldade": "Médio", "emoji": "🌱"},
        {"pergunta": "Quantos planetas tem o Sistema Solar?", "opcoes": ["8", "9", "7", "10"], "resposta": "8", "dificuldade": "Médio", "emoji": "🪐"},
        {"pergunta": "Quem é o pai da genética moderna?", "opcoes": ["Gregor Mendel", "Charles Darwin", "Louis Pasteur", "James Watson"], "resposta": "Gregor Mendel", "dificuldade": "Médio", "emoji": "🧬"},
        {"pergunta": "Qual unidade mede corrente elétrica?", "opcoes": ["Ampère", "Volt", "Watt", "Ohm"], "resposta": "Ampère", "dificuldade": "Médio", "emoji": "⚡"},
        {"pergunta": "Qual é a velocidade da luz?", "opcoes": ["300.000 km/s", "150.000 km/s", "500.000 km/s", "100.000 km/s"], "resposta": "300.000 km/s", "dificuldade": "Médio", "emoji": "💡"},
        {"pergunta": "Qual elemento químico tem símbolo 'O'?", "opcoes": ["Oxigênio", "Ouro", "Ósmio", "Oxalato"], "resposta": "Oxigênio", "dificuldade": "Médio", "emoji": "🧪"},
        {"pergunta": "Qual é o ponto de ebulição da água?", "opcoes": ["100°C", "0°C", "50°C", "200°C"], "resposta": "100°C", "dificuldade": "Médio", "emoji": "🌡️"},
        {"pergunta": "Qual é a estrutura do DNA?", "opcoes": ["Dupla hélice", "Tripla hélice", "Espiral", "Círculo"], "resposta": "Dupla hélice", "dificuldade": "Médio", "emoji": "🧬"},
        {"pergunta": "Qual é o principal componente do ar?", "opcoes": ["Nitrogênio", "Oxigênio", "Argônio", "Gás carbônico"], "resposta": "Nitrogênio", "dificuldade": "Médio", "emoji": "💨"},
        {"pergunta": "Qual partícula dá massa às outras?", "opcoes": ["Bóson de Higgs", "Quark", "Fóton", "Nêutron"], "resposta": "Bóson de Higgs", "dificuldade": "Difícil", "emoji": "⚛️"},
        {"pergunta": "Quem descobriu a penicilina?", "opcoes": ["Alexander Fleming", "Louis Pasteur", "Robert Koch", "Marie Curie"], "resposta": "Alexander Fleming", "dificuldade": "Difícil", "emoji": "💊"},
        {"pergunta": "Qual é o número atômico do carbono?", "opcoes": ["6", "8", "12", "4"], "resposta": "6", "dificuldade": "Difícil", "emoji": "🔬"},
        {"pergunta": "Quem formulou as leis da gravitação?", "opcoes": ["Isaac Newton", "Albert Einstein", "Galileu Galilei", "Johannes Kepler"], "resposta": "Isaac Newton", "dificuldade": "Difícil", "emoji": "🍎"},
        {"pergunta": "Qual processo gera células reprodutivas?", "opcoes": ["Meiose", "Mitose", "Osmose", "Difusão"], "resposta": "Meiose", "dificuldade": "Difícil", "emoji": "🧬"},
        {"pergunta": "Qual é a unidade de medida da força?", "opcoes": ["Newton", "Joule", "Watt", "Pascal"], "resposta": "Newton", "dificuldade": "Difícil", "emoji": "⚡"},
        {"pergunta": "Qual é a partícula subatômica com carga negativa?", "opcoes": ["Elétron", "Próton", "Nêutron", "Pósitron"], "resposta": "Elétron", "dificuldade": "Difícil", "emoji": "⚛️"},
        {"pergunta": "Qual é o elemento mais abundante no universo?", "opcoes": ["Hidrogênio", "Hélio", "Oxigênio", "Carbono"], "resposta": "Hidrogênio", "dificuldade": "Difícil", "emoji": "🌌"},
        {"pergunta": "Qual é a constante de Avogadro?", "opcoes": ["6,02 x 10^23", "6,02 x 10^22", "6,02 x 10^24", "6,02 x 10^21"], "resposta": "6,02 x 10^23", "dificuldade": "Difícil", "emoji": "🔢"},
        {"pergunta": "Quem descobriu a radioatividade?", "opcoes": ["Marie Curie", "Henri Becquerel", "Albert Einstein", "Ernest Rutherford"], "resposta": "Marie Curie", "dificuldade": "Difícil", "emoji": "☢️"},
    ],
    "Geografia": [
        {"pergunta": "Qual é o maior continente?", "opcoes": ["Ásia", "África", "América", "Europa"], "resposta": "Ásia", "dificuldade": "Fácil", "emoji": "🌏"},
        {"pergunta": "Em qual continente fica o Brasil?", "opcoes": ["América do Sul", "América do Norte", "África", "Europa"], "resposta": "América do Sul", "dificuldade": "Fácil", "emoji": "🇧🇷"},
        {"pergunta": "Qual é o menor país do mundo?", "opcoes": ["Vaticano", "Mônaco", "San Marino", "Liechtenstein"], "resposta": "Vaticano", "dificuldade": "Fácil", "emoji": "⛪"},
        {"pergunta": "Qual deserto é famoso na África?", "opcoes": ["Saara", "Gobi", "Atacama", "Kalahari"], "resposta": "Saara", "dificuldade": "Fácil", "emoji": "🏜️"},
        {"pergunta": "Quantos estados tem o Brasil?", "opcoes": ["26", "27", "25", "28"], "resposta": "26", "dificuldade": "Fácil", "emoji": "🇧🇷"},
        {"pergunta": "Qual é a capital da França?", "opcoes": ["Paris", "Lyon", "Marselha", "Nice"], "resposta": "Paris", "dificuldade": "Fácil", "emoji": "🇫🇷"},
        {"pergunta": "Qual rio passa pelo Cairo?", "opcoes": ["Nilo", "Amazonas", "Tigre", "Eufrates"], "resposta": "Nilo", "dificuldade": "Fácil", "emoji": "🌊"},
        {"pergunta": "Qual país tem formato de bota?", "opcoes": ["Itália", "Grécia", "Espanha", "Portugal"], "resposta": "Itália", "dificuldade": "Fácil", "emoji": "👢"},
        {"pergunta": "Qual é a cordilheira mais extensa?", "opcoes": ["Andes", "Himalaias", "Alpes", "Montanhas Rochosas"], "resposta": "Andes", "dificuldade": "Fácil", "emoji": "🏔️"},
        {"pergunta": "Qual estreito separa Europa e África?", "opcoes": ["Gibraltar", "Bering", "Bósforo", "Messina"], "resposta": "Gibraltar", "dificuldade": "Fácil", "emoji": "🌊"},
        {"pergunta": "Qual é a capital da Austrália?", "opcoes": ["Camberra", "Sydney", "Melbourne", "Perth"], "resposta": "Camberra", "dificuldade": "Médio", "emoji": "🇦🇺"},
        {"pergunta": "Qual é o maior país em área?", "opcoes": ["Rússia", "Canadá", "China", "EUA"], "resposta": "Rússia", "dificuldade": "Médio", "emoji": "🇷🇺"},
        {"pergunta": "Qual é a montanha mais alta do mundo?", "opcoes": ["Everest", "K2", "Kanchenjunga", "Lhotse"], "resposta": "Everest", "dificuldade": "Médio", "emoji": "🏔️"},
        {"pergunta": "Qual é o maior oceano?", "opcoes": ["Pacífico", "Atlântico", "Índico", "Ártico"], "resposta": "Pacífico", "dificuldade": "Médio", "emoji": "🌊"},
        {"pergunta": "Qual é a capital do Canadá?", "opcoes": ["Ottawa", "Toronto", "Vancouver", "Montreal"], "resposta": "Ottawa", "dificuldade": "Médio", "emoji": "🇨🇦"},
        {"pergunta": "Qual é o rio mais longo do mundo?", "opcoes": ["Nilo", "Amazonas", "Yangtzé", "Mississippi"], "resposta": "Nilo", "dificuldade": "Médio", "emoji": "🌊"},
        {"pergunta": "Qual país tem a maior população?", "opcoes": ["Índia", "China", "EUA", "Indonésia"], "resposta": "Índia", "dificuldade": "Médio", "emoji": "👥"},
        {"pergunta": "Qual é a capital da Argentina?", "opcoes": ["Buenos Aires", "Santiago", "Lima", "Montevidéu"], "resposta": "Buenos Aires", "dificuldade": "Médio", "emoji": "🇦🇷"},
        {"pergunta": "Qual país tem a maior costa litorânea?", "opcoes": ["Canadá", "Indonésia", "Rússia", "Austrália"], "resposta": "Canadá", "dificuldade": "Médio", "emoji": "🏖️"},
        {"pergunta": "Qual é a maior ilha do mundo?", "opcoes": ["Groenlândia", "Nova Guiné", "Bornéu", "Madagascar"], "resposta": "Groenlândia", "dificuldade": "Médio", "emoji": "🏝️"},
        {"pergunta": "Qual é o ponto mais baixo da Terra?", "opcoes": ["Mar Morto", "Vale da Morte", "Depressão de Qattara", "Mar Cáspio"], "resposta": "Mar Morto", "dificuldade": "Difícil", "emoji": "🌊"},
        {"pergunta": "Qual país tem mais vizinhos?", "opcoes": ["China e Rússia", "Brasil e EUA", "França e Alemanha", "Índia e Paquistão"], "resposta": "China e Rússia", "dificuldade": "Difícil", "emoji": "🌍"},
        {"pergunta": "Qual é a capital da Islândia?", "opcoes": ["Reykjavik", "Oslo", "Helsinque", "Estocolmo"], "resposta": "Reykjavik", "dificuldade": "Difícil", "emoji": "🇮🇸"},
        {"pergunta": "Qual é o lago mais profundo do mundo?", "opcoes": ["Baikal", "Tanganica", "Vitória", "Superior"], "resposta": "Baikal", "dificuldade": "Difícil", "emoji": "🏞️"},
        {"pergunta": "Qual é a capital da Nova Zelândia?", "opcoes": ["Wellington", "Auckland", "Christchurch", "Hamilton"], "resposta": "Wellington", "dificuldade": "Difícil", "emoji": "🇳🇿"},
        {"pergunta": "Qual país tem o maior número de fusos horários?", "opcoes": ["França", "Rússia", "EUA", "Canadá"], "resposta": "França", "dificuldade": "Difícil", "emoji": "⏰"},
        {"pergunta": "Qual é a capital da África do Sul?", "opcoes": ["Pretória", "Cidade do Cabo", "Joanesburgo", "Durban"], "resposta": "Pretória", "dificuldade": "Difícil", "emoji": "🇿🇦"},
        {"pergunta": "Qual estreito é o mais movimentado do mundo?", "opcoes": ["Estreito de Dover", "Estreito de Gibraltar", "Estreito de Malaca", "Bósforo"], "resposta": "Estreito de Dover", "dificuldade": "Difícil", "emoji": "⛴️"},
        {"pergunta": "Qual é a maior cidade do mundo em população?", "opcoes": ["Tóquio", "Nova York", "Xangai", "Mumbai"], "resposta": "Tóquio", "dificuldade": "Difícil", "emoji": "🏙️"},
        {"pergunta": "Qual é a altitude média do Brasil?", "opcoes": ["600m", "300m", "800m", "1000m"], "resposta": "600m", "dificuldade": "Difícil", "emoji": "⛰️"},
    ],
    "Tecnologia": [
        {"pergunta": "Qual empresa criou o Windows?", "opcoes": ["Microsoft", "Apple", "Google", "IBM"], "resposta": "Microsoft", "dificuldade": "Fácil", "emoji": "🖥️"},
        {"pergunta": "Qual desses é um sistema operacional?", "opcoes": ["Windows", "Word", "Excel", "PowerPoint"], "resposta": "Windows", "dificuldade": "Fácil", "emoji": "💻"},
        {"pergunta": "Qual site é conhecido como 'o Google'?", "opcoes": ["Google", "Bing", "Yahoo", "DuckDuckGo"], "resposta": "Google", "dificuldade": "Fácil", "emoji": "🔍"},
        {"pergunta": "Qual desses é um smartphone?", "opcoes": ["iPhone", "MacBook", "iPad", "iMac"], "resposta": "iPhone", "dificuldade": "Fácil", "emoji": "📱"},
        {"pergunta": "Qual linguagem é usada para criar sites?", "opcoes": ["HTML", "Python", "Java", "C++"], "resposta": "HTML", "dificuldade": "Fácil", "emoji": "🌐"},
        {"pergunta": "Qual é a rede social mais popular?", "opcoes": ["Facebook", "Instagram", "Twitter", "LinkedIn"], "resposta": "Facebook", "dificuldade": "Fácil", "emoji": "📱"},
        {"pergunta": "Qual empresa criou o iPhone?", "opcoes": ["Apple", "Samsung", "Google", "Microsoft"], "resposta": "Apple", "dificuldade": "Fácil", "emoji": "🍎"},
        {"pergunta": "Qual desses é um browser?", "opcoes": ["Chrome", "Windows", "MacOS", "Linux"], "resposta": "Chrome", "dificuldade": "Fácil", "emoji": "🌐"},
        {"pergunta": "Qual é a memória volátil do computador?", "opcoes": ["RAM", "ROM", "HD", "SSD"], "resposta": "RAM", "dificuldade": "Fácil", "emoji": "🧠"},
        {"pergunta": "Qual desses é um dispositivo de entrada?", "opcoes": ["Teclado", "Monitor", "Impressora", "Caixa de som"], "resposta": "Teclado", "dificuldade": "Fácil", "emoji": "⌨️"},
        {"pergunta": "Qual linguagem é usada para inteligência artificial?", "opcoes": ["Python", "Java", "C++", "JavaScript"], "resposta": "Python", "dificuldade": "Médio", "emoji": "🤖"},
        {"pergunta": "Qual é a maior empresa de tecnologia do mundo?", "opcoes": ["Apple", "Microsoft", "Google", "Amazon"], "resposta": "Apple", "dificuldade": "Médio", "emoji": "🏢"},
        {"pergunta": "Qual sistema operacional é open source?", "opcoes": ["Linux", "Windows", "MacOS", "iOS"], "resposta": "Linux", "dificuldade": "Médio", "emoji": "🐧"},
        {"pergunta": "Qual é o modelo de desenvolvimento ágil?", "opcoes": ["Scrum", "Cascata", "Espiral", "V-Model"], "resposta": "Scrum", "dificuldade": "Médio", "emoji": "🔄"},
        {"pergunta": "Qual é a arquitetura de computadores mais comum?", "opcoes": ["Von Neumann", "Harvard", "CISC", "RISC"], "resposta": "Von Neumann", "dificuldade": "Médio", "emoji": "🏗️"},
        {"pergunta": "Qual é o principal protocolo da internet?", "opcoes": ["TCP/IP", "HTTP", "FTP", "SMTP"], "resposta": "TCP/IP", "dificuldade": "Médio", "emoji": "🌐"},
        {"pergunta": "Qual é a tecnologia de realidade virtual?", "opcoes": ["VR", "AR", "MR", "XR"], "resposta": "VR", "dificuldade": "Médio", "emoji": "🥽"},
        {"pergunta": "Qual linguagem é usada no desenvolvimento Android?", "opcoes": ["Java", "Swift", "Kotlin", "Python"], "resposta": "Java", "dificuldade": "Médio", "emoji": "📱"},
        {"pergunta": "Qual é a tecnologia de criptografia mais usada?", "opcoes": ["AES", "RSA", "DES", "3DES"], "resposta": "AES", "dificuldade": "Médio", "emoji": "🔐"},
        {"pergunta": "Qual é o formato de imagem com compressão sem perda?", "opcoes": ["PNG", "JPEG", "GIF", "BMP"], "resposta": "PNG", "dificuldade": "Médio", "emoji": "🖼️"},
        {"pergunta": "Qual linguagem é usada no desenvolvimento de sistemas embarcados?", "opcoes": ["C", "Python", "Java", "Ruby"], "resposta": "C", "dificuldade": "Difícil", "emoji": "🔧"},
        {"pergunta": "Qual é o principal algoritmo de ordenação?", "opcoes": ["QuickSort", "BubbleSort", "MergeSort", "InsertionSort"], "resposta": "QuickSort", "dificuldade": "Difícil", "emoji": "📊"},
        {"pergunta": "Qual é a complexidade do algoritmo de busca binária?", "opcoes": ["O(log n)", "O(n)", "O(n²)", "O(2n)"], "resposta": "O(log n)", "dificuldade": "Difícil", "emoji": "🔍"},
        {"pergunta": "Qual foi o primeiro computador eletrônico?", "opcoes": ["ENIAC", "UNIVAC", "Colossus", "ABC"], "resposta": "ENIAC", "dificuldade": "Difícil", "emoji": "🖥️"},
        {"pergunta": "Qual é o sistema de gerenciamento de banco de dados mais usado?", "opcoes": ["MySQL", "PostgreSQL", "Oracle", "MongoDB"], "resposta": "MySQL", "dificuldade": "Difícil", "emoji": "🗄️"},
        {"pergunta": "Qual é o protocolo de e-mail mais usado?", "opcoes": ["SMTP", "POP3", "IMAP", "HTTP"], "resposta": "SMTP", "dificuldade": "Difícil", "emoji": "📧"},
        {"pergunta": "Qual é a tecnologia de internet sem fio de curto alcance?", "opcoes": ["Bluetooth", "WiFi", "ZigBee", "NFC"], "resposta": "Bluetooth", "dificuldade": "Difícil", "emoji": "📶"},
        {"pergunta": "Qual é a unidade básica de armazenamento digital?", "opcoes": ["Bit", "Byte", "KB", "MB"], "resposta": "Bit", "dificuldade": "Difícil", "emoji": "💾"},
        {"pergunta": "Qual foi o primeiro sistema operacional da Microsoft?", "opcoes": ["MS-DOS", "Windows 1.0", "Windows 3.1", "Windows 95"], "resposta": "MS-DOS", "dificuldade": "Difícil", "emoji": "💻"},
        {"pergunta": "Qual é a linguagem de programação mais antiga em uso?", "opcoes": ["FORTRAN", "COBOL", "LISP", "ALGOL"], "resposta": "FORTRAN", "dificuldade": "Difícil", "emoji": "📟"},
    ],
    "Cinema": [
        {"pergunta": "Quem dirigiu 'Titanic'?", "opcoes": ["James Cameron", "Steven Spielberg", "Christopher Nolan", "Tim Burton"], "resposta": "James Cameron", "dificuldade": "Fácil", "emoji": "🚢"},
        {"pergunta": "Qual ator interpretou o Homem de Ferro?", "opcoes": ["Robert Downey Jr.", "Chris Evans", "Chris Hemsworth", "Scarlett Johansson"], "resposta": "Robert Downey Jr.", "dificuldade": "Fácil", "emoji": "🤖"},
        {"pergunta": "Qual filme venceu o Oscar de Melhor Filme em 2020?", "opcoes": ["Parasita", "1917", "O Irlandês", "Joker"], "resposta": "Parasita", "dificuldade": "Fácil", "emoji": "🏆"},
        {"pergunta": "Qual atriz é famosa por 'O Diabo Veste Prada'?", "opcoes": ["Meryl Streep", "Anne Hathaway", "Emily Blunt", "Stanley Tucci"], "resposta": "Meryl Streep", "dificuldade": "Fácil", "emoji": "👠"},
        {"pergunta": "Qual é o estúdio por trás de 'Star Wars'?", "opcoes": ["Lucasfilm", "Disney", "Paramount", "Warner Bros"], "resposta": "Lucasfilm", "dificuldade": "Fácil", "emoji": "🌌"},
        {"pergunta": "Qual filme de animação é da Pixar?", "opcoes": ["Toy Story", "Shrek", "Madagascar", "Ice Age"], "resposta": "Toy Story", "dificuldade": "Fácil", "emoji": "🧸"},
        {"pergunta": "Qual ator é conhecido como 'O Espanta Tubarão'?", "opcoes": ["Mark Ruffalo", "Chris Evans", "Chris Hemsworth", "Robert Downey Jr."], "resposta": "Mark Ruffalo", "dificuldade": "Fácil", "emoji": "🦈"},
        {"pergunta": "Qual filme tem a música 'My Heart Will Go On'?", "opcoes": ["Titanic", "Avatar", "O Rei Leão", "Ghost"], "resposta": "Titanic", "dificuldade": "Fácil", "emoji": "🎵"},
        {"pergunta": "Qual atriz é a 'Rainha do Drama'?", "opcoes": ["Meryl Streep", "Cate Blanchett", "Viola Davis", "Frances McDormand"], "resposta": "Meryl Streep", "dificuldade": "Fácil", "emoji": "👑"},
        {"pergunta": "Qual filme de 1994 é conhecido por sua trilha sonora?", "opcoes": ["O Rei Leão", "Forrest Gump", "Pulp Fiction", "The Shawshank Redemption"], "resposta": "O Rei Leão", "dificuldade": "Fácil", "emoji": "🎵"},
        {"pergunta": "Qual diretor é famoso por filmes de terror?", "opcoes": ["Alfred Hitchcock", "Stanley Kubrick", "Quentin Tarantino", "Martin Scorsese"], "resposta": "Alfred Hitchcock", "dificuldade": "Médio", "emoji": "🎥"},
        {"pergunta": "Qual filme venceu o Oscar de Melhor Filme em 1994?", "opcoes": ["A Lista de Schindler", "Forrest Gump", "Filadélfia", "O Fugitivo"], "resposta": "A Lista de Schindler", "dificuldade": "Médio", "emoji": "🎬"},
        {"pergunta": "Qual ator interpretou o Coringa em 1989?", "opcoes": ["Jack Nicholson", "Joaquin Phoenix", "Heath Ledger", "Jared Leto"], "resposta": "Jack Nicholson", "dificuldade": "Médio", "emoji": "🎭"},
        {"pergunta": "Qual é o filme mais longo de todos os tempos?", "opcoes": ["Florentina Hubaldo", "Gone with the Wind", "Lawrence of Arabia", "The Godfather"], "resposta": "Florentina Hubaldo", "dificuldade": "Médio", "emoji": "🎬"},
        {"pergunta": "Qual estúdio criou 'O Senhor dos Anéis'?", "opcoes": ["New Line Cinema", "Warner Bros", "Universal", "Paramount"], "resposta": "New Line Cinema", "dificuldade": "Médio", "emoji": "🧝"},
        {"pergunta": "Qual atriz venceu mais Oscars?", "opcoes": ["Katharine Hepburn", "Meryl Streep", "Bette Davis", "Ingrid Bergman"], "resposta": "Katharine Hepburn", "dificuldade": "Médio", "emoji": "🏆"},
        {"pergunta": "Qual filme tem a maior bilheteria de todos os tempos?", "opcoes": ["Avatar", "Titanic", "Star Wars", "Endgame"], "resposta": "Avatar", "dificuldade": "Médio", "emoji": "💰"},
        {"pergunta": "Qual diretor é conhecido por filmes de ação?", "opcoes": ["Michael Bay", "James Cameron", "Steven Spielberg", "Christopher Nolan"], "resposta": "Michael Bay", "dificuldade": "Médio", "emoji": "💥"},
        {"pergunta": "Qual é o filme de maior sucesso da Marvel?", "opcoes": ["Vingadores: Ultimato", "Vingadores: Guerra Infinita", "Homem de Ferro", "Capitão América"], "resposta": "Vingadores: Ultimato", "dificuldade": "Médio", "emoji": "🦸"},
        {"pergunta": "Qual ator interpretou o Wolverine?", "opcoes": ["Hugh Jackman", "Ryan Reynolds", "Chris Evans", "Chris Hemsworth"], "resposta": "Hugh Jackman", "dificuldade": "Médio", "emoji": "🐾"},
        {"pergunta": "Qual filme foi o primeiro a ganhar 5 Oscars?", "opcoes": ["It Happened One Night", "Gone with the Wind", "The Godfather", "Titanic"], "resposta": "It Happened One Night", "dificuldade": "Difícil", "emoji": "🏆"},
        {"pergunta": "Qual diretor é famoso por filmes de ficção científica?", "opcoes": ["Steven Spielberg", "James Cameron", "Christopher Nolan", "Ridley Scott"], "resposta": "Steven Spielberg", "dificuldade": "Difícil", "emoji": "👽"},
        {"pergunta": "Qual filme tem a melhor trilha sonora de todos os tempos?", "opcoes": ["O Poderoso Chefão", "Star Wars", "Titanic", "The Sound of Music"], "resposta": "O Poderoso Chefão", "dificuldade": "Difícil", "emoji": "🎵"},
        {"pergunta": "Qual ator venceu o Oscar de Melhor Ator em 1997?", "opcoes": ["Jack Nicholson", "Tom Hanks", "Dustin Hoffman", "Al Pacino"], "resposta": "Jack Nicholson", "dificuldade": "Difícil", "emoji": "🏆"},
        {"pergunta": "Qual é o filme mais antigo em exibição contínua?", "opcoes": ["The Rocky Horror Picture Show", "The Sound of Music", "Gone with the Wind", "The Wizard of Oz"], "resposta": "The Rocky Horror Picture Show", "dificuldade": "Difícil", "emoji": "🎭"},
        {"pergunta": "Qual diretor nunca ganhou um Oscar?", "opcoes": ["Alfred Hitchcock", "Stanley Kubrick", "Quentin Tarantino", "Christopher Nolan"], "resposta": "Alfred Hitchcock", "dificuldade": "Difícil", "emoji": "🎥"},
        {"pergunta": "Qual filme é considerado o primeiro blockbuster?", "opcoes": ["Tubarão", "Star Wars", "Titanic", "E.T."], "resposta": "Tubarão", "dificuldade": "Difícil", "emoji": "🦈"},
        {"pergunta": "Qual atriz é a 'Rainha do Box Office'?", "opcoes": ["Scarlett Johansson", "Angelina Jolie", "Meryl Streep", "Jennifer Lawrence"], "resposta": "Scarlett Johansson", "dificuldade": "Difícil", "emoji": "👑"},
        {"pergunta": "Qual filme tem a cena mais longa de uma tomada?", "opcoes": ["Rope", "Birdman", "Russian Ark", "Victoria"], "resposta": "Russian Ark", "dificuldade": "Difícil", "emoji": "🎬"},
        {"pergunta": "Qual é o filme com o maior número de sequências?", "opcoes": ["Star Wars", "Harry Potter", "Marvel", "James Bond"], "resposta": "Marvel", "dificuldade": "Difícil", "emoji": "🦸"},
    ],
}

# ===== CORES E ÍCONES =====
CORES = {
    "Esportes": "#FF6B35",
    "Entretenimento": "#F1C40F",
    "Arte": "#9B59B6",
    "História": "#E74C3C",
    "Ciência": "#2ECC71",
    "Geografia": "#3498DB",
    "Tecnologia": "#00B4D8",
    "Cinema": "#FF0080",
}

ICONES = {
    "Esportes": "⚽",
    "Entretenimento": "🎬",
    "Arte": "🎨",
    "História": "🏛️",
    "Ciência": "🔬",
    "Geografia": "🌍",
    "Tecnologia": "💻",
    "Cinema": "🎬",
}

CONQUISTAS = {
    "primeiro_jogo": {"nome": "👶 Primeiro Passo", "desc": "Complete seu primeiro jogo", "desbloqueado": False},
    "perfeito": {"nome": "🎯 Perfeição", "desc": "Acerte 5 perguntas seguidas", "desbloqueado": False},
    "genio": {"nome": "🧠 Gênio", "desc": "Marque 100 pontos", "desbloqueado": False},
    "expert": {"nome": "💪 Expert", "desc": "Conclua o modo Expert", "desbloqueado": False},
    "maratona": {"nome": "🏃 Maratonista", "desc": "Complete o modo Maratona", "desbloqueado": False},
    "explorador": {"nome": "🗺️ Explorador", "desc": "Jogue em todas as categorias", "desbloqueado": False},
    "x10": {"nome": "🔥 X10", "desc": "Acerte 10 perguntas seguidas", "desbloqueado": False},
}

class SaveSystem:
    @staticmethod
    def salvar_dados(dados):
        try:
            with open("trivia_save.json", "w", encoding='utf-8') as f:
                json.dump(dados, f, indent=2, ensure_ascii=False)
        except:
            pass

    @staticmethod
    def carregar_dados():
        try:
            if os.path.exists("trivia_save.json"):
                with open("trivia_save.json", "r", encoding='utf-8') as f:
                    return json.load(f)
        except:
            pass
        return None

# ===== JOGO PRINCIPAL =====
class TriviaCrackPremium:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("🌟 TRIVIA CRACK - Premium Plus")
        self.janela.attributes('-fullscreen', True)
        self.janela.configure(bg="#0a0a1a")
        self.janela.resizable(False, False)
        self.janela.bind('<Escape>', self.alternar_tela_cheia)
        self.janela.bind('<F11>', self.alternar_tela_cheia)
        
        self.fonte_titulo = font.Font(family="Helvetica", size=24, weight="bold")
        self.fonte_sub = font.Font(family="Helvetica", size=16)
        self.fonte_normal = font.Font(family="Helvetica", size=13)
        self.fonte_btn = font.Font(family="Helvetica", size=13, weight="bold")
        self.fonte_pequena = font.Font(family="Helvetica", size=11)

        self.modo = None
        self.categoria_atual = None
        self.pergunta_atual = None
        self.pergunta_index = 0
        self.pontuacao = 0
        self.sequencia = 0
        self.rodada = 0
        self.jogando = False
        self.categorias_restantes = []
        self.perguntas = []
        self.tempo_restante = 30
        self.timer_id = None
        self.botoes_opcoes = []
        
        self.estatisticas = {
            "total_perguntas": 0,
            "acertos": 0,
            "erros": 0,
            "categorias_jogadas": [],
            "total_jogos": 0,
            "recordes": {"pontuacao": 0, "sequencia": 0}
        }
        self.conquistas = CONQUISTAS.copy()
        self.carregar_dados()
        
        self.frame_principal = tk.Frame(self.janela, bg="#0a0a1a")
        self.frame_principal.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        self.setup_cabecalho()
        
        self.conteudo = tk.Frame(self.frame_principal, bg="#0a0a1a")
        self.conteudo.pack(fill=tk.BOTH, expand=True)
        
        self.setup_rodape()
        
        self.mostrar_tela_inicial()
        self.janela.mainloop()

    def alternar_tela_cheia(self, event=None):
        is_fullscreen = self.janela.attributes('-fullscreen')
        self.janela.attributes('-fullscreen', not is_fullscreen)

    def carregar_dados(self):
        dados = SaveSystem.carregar_dados()
        if dados:
            if "estatisticas" in dados:
                self.estatisticas.update(dados["estatisticas"])
            if "conquistas" in dados:
                self.conquistas.update(dados["conquistas"])

    def salvar_dados(self):
        dados = {
            "estatisticas": self.estatisticas,
            "conquistas": self.conquistas
        }
        SaveSystem.salvar_dados(dados)

    def setup_cabecalho(self):
        self.canvas_cabecalho = tk.Canvas(self.frame_principal, height=80, bg="#0a0a1a", highlightthickness=0)
        self.canvas_cabecalho.pack(fill=tk.X, pady=(0, 8))
        
        # Gradiente no cabeçalho
        for i in range(80):
            r = int(10 + i * 0.4)
            g = int(5 + i * 0.3)
            b = int(30 + i * 0.5)
            cor = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas_cabecalho.create_rectangle(0, i, 2000, i + 1, fill=cor, outline="")
            
        self.canvas_cabecalho.create_text(700, 25, text="🌟 TRIVIA CRACK PREMIUM PLUS 🌟",
                                           font=self.fonte_titulo, fill="#FFD700")
        self.canvas_cabecalho.create_text(700, 52, text="🧠 O Desafio Definitivo de Conhecimento",
                                           font=self.fonte_pequena, fill="#aaa")
        
        self.pontos_header = self.canvas_cabecalho.create_text(1250, 25, text="🏆 0",
                                                                 font=self.fonte_sub, fill="#FFD700")
        self.nivel_header = self.canvas_cabecalho.create_text(1250, 50, text="⭐ Nível 1",
                                                               font=self.fonte_pequena, fill="#2ECC71")

    def setup_rodape(self):
        self.rodape = tk.Frame(self.frame_principal, bg="#0a0a1a")
        self.rodape.pack(fill=tk.X, pady=5)
        
        dicas = ["💡 Dica: Use o modo 'Sobrevivência' para testar sua velocidade!",
                 "🎯 Tente manter uma sequência para pontuações extras!",
                 "📚 Cada categoria tem perguntas de diferentes níveis!"]
        
        self.dica_label = tk.Label(self.rodape, text=random.choice(dicas),
                                    font=self.fonte_pequena, fg="#666", bg="#0a0a1a")
        self.dica_label.pack(side=tk.LEFT, padx=10)
        
        self.status_label = tk.Label(self.rodape, text="Pronto para jogar!",
                                      font=self.fonte_pequena, fg="#444", bg="#0a0a1a")
        self.status_label.pack(side=tk.LEFT, padx=20)
        
        tk.Label(self.rodape, text="v5.0 Premium Plus", font=self.fonte_pequena,
                 fg="#444", bg="#0a0a1a").pack(side=tk.RIGHT, padx=10)

    def limpar_conteudo(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

    def atualizar_pontos_header(self):
        self.canvas_cabecalho.itemconfig(self.pontos_header, text=f"🏆 {self.pontuacao}")
        nivel = min(10, (self.pontuacao // 20) + 1)
        self.canvas_cabecalho.itemconfig(self.nivel_header, text=f"⭐ Nível {nivel}")

    def play_sound(self, sound_type):
        if not SOUND_ENABLED:
            return
        try:
            if sound_type == "correct":
                winsound.Beep(800, 150)
                winsound.Beep(1000, 150)
            elif sound_type == "wrong":
                winsound.Beep(300, 300)
            elif sound_type == "tick":
                winsound.Beep(500, 50)
            elif sound_type == "gameover":
                winsound.Beep(400, 200)
                winsound.Beep(300, 200)
                winsound.Beep(200, 300)
        except:
            pass

    def mostrar_tela_inicial(self):
        self.limpar_conteudo()
        self.jogando = False
        self.atualizar_pontos_header()
        self.status_label.config(text="Menu Principal")
        
        card = tk.Frame(self.conteudo, bg="#1a1a2e", relief=tk.FLAT, bd=0)
        card.pack(expand=True, padx=15, pady=15)
        
        canvas_card = tk.Canvas(card, width=800, height=600, bg="#1a1a2e", highlightthickness=0)
        canvas_card.pack()
        
        # Borda dourada
        canvas_card.create_rectangle(10, 10, 790, 590, outline="#FFD700", width=2, fill="#1e1e3a")
        
        # Título
        canvas_card.create_text(400, 40, text="🧠 TESTE SEUS CONHECIMENTOS", 
                               font=self.fonte_titulo, fill="white")
        canvas_card.create_text(400, 75, text="Escolha seu modo de jogo:", 
                               font=self.fonte_sub, fill="#aaa")
        
        # Estatísticas
        stats = f"🎯 Jogos: {self.estatisticas['total_jogos']} | 🏆 Recorde: {self.estatisticas['recordes']['pontuacao']} pts"
        canvas_card.create_text(400, 105, text=stats, font=self.fonte_pequena, fill="#FFD700")
        
        # Botões dos modos de jogo
        botoes = [
            ("🎡 Modo Clássico", "#E67E22", self.iniciar_classico),
            ("⚡ Modo Desafio", "#2ECC71", self.iniciar_desafio),
            ("📚 Modo Maratona", "#3498DB", self.iniciar_todas),
            ("🎯 Modo Expert", "#E74C3C", self.iniciar_expert),
            ("⏰ Modo Sobrevivência", "#FF6B35", self.iniciar_sobrevivencia),
            ("👥 Modo Dueto", "#9B59B6", self.iniciar_dueto),
            ("🎲 Modo Paradoxal", "#8B008B", self.iniciar_paradoxal),
        ]
        
        y_start = 135
        y_step = 50
        
        for i, (texto, cor, cmd) in enumerate(botoes):
            x = 250 if i % 2 == 0 else 550
            y = y_start + (i // 2) * y_step
            
            btn = tk.Button(card, text=texto, font=self.fonte_btn, bg=cor, fg="white",
                           relief=tk.FLAT, padx=12, pady=8, cursor="hand2",
                           command=cmd, bd=0, width=22)
            btn_window = canvas_card.create_window(x, y, window=btn)
        
        # Botões inferiores
        y_botoes = 520
        btn_frame = tk.Frame(card, bg="#1e1e3a")
        canvas_card.create_window(400, y_botoes, window=btn_frame)
        
        for txt, cor, cmd in [("🏅 Conquistas", "#9B59B6", self.mostrar_conquistas),
                              ("📊 Estatísticas", "#3498DB", self.mostrar_estatisticas),
                              ("🚪 Sair", "#E74C3C", self.sair_jogo)]:
            btn = tk.Button(btn_frame, text=txt, font=self.fonte_btn, bg=cor, fg="white",
                           relief=tk.FLAT, padx=10, pady=6, cursor="hand2", command=cmd, bd=0)
            btn.pack(side=tk.LEFT, padx=3)

    # ===== MODOS DE JOGO =====
    def iniciar_classico(self):
        self.modo = "classico"
        self.categorias_restantes = list(PERGUNTAS.keys())
        self.rodada = 0
        self.pontuacao = 0
        self.sequencia = 0
        self.jogando = True
        self.status_label.config(text="Modo Clássico")
        self.proxima_rodada_classico()

    def iniciar_desafio(self):
        self.modo = "desafio"
        self.pontuacao = 0
        self.sequencia = 0
        self.jogando = True
        self.status_label.config(text="Modo Desafio")
        self.mostrar_escolha_categoria()

    def iniciar_todas(self):
        self.modo = "todas"
        self.categorias_restantes = list(PERGUNTAS.keys())
        self.pontuacao = 0
        self.sequencia = 0
        self.jogando = True
        self.status_label.config(text="Modo Maratona")
        self.proxima_categoria_todas()

    def iniciar_expert(self):
        self.modo = "expert"
        self.pontuacao = 0
        self.sequencia = 0
        self.jogando = True
        self.status_label.config(text="Modo Expert")
        
        # Pegar apenas perguntas difíceis
        perguntas_expert = []
        for cat_nome, cat_perguntas in PERGUNTAS.items():
            for p in cat_perguntas:
                if p["dificuldade"] == "Difícil":
                    p_copy = p.copy()
                    p_copy["categoria_original"] = cat_nome
                    perguntas_expert.append(p_copy)
        
        random.shuffle(perguntas_expert)
        self.perguntas = perguntas_expert[:10]
        self.pergunta_index = 0
        self.categoria_atual = self.perguntas[0].get("categoria_original", "Expert") if self.perguntas else "Expert"
        self.mostrar_pergunta()

    def iniciar_sobrevivencia(self):
        self.modo = "sobrevivencia"
        self.pontuacao = 0
        self.sequencia = 0
        self.tempo_restante = 30
        self.jogando = True
        self.mostrar_escolha_categoria()

    def iniciar_dueto(self):
        self.modo = "dueto"
        self.pontuacao = 0
        self.sequencia = 0
        self.jogando = True
        self.pontuacao_jogador1 = 0
        self.pontuacao_jogador2 = 0
        self.jogador_atual = 1
        self.mostrar_escolha_categoria()

    def iniciar_paradoxal(self):
        self.modo = "paradoxal"
        self.pontuacao = 0
        self.sequencia = 0
        self.jogando = True
        self.status_label.config(text="🎲 Modo Paradoxal")
        
        # Pegar perguntas aleatórias de todas as categorias
        todas = []
        for cat, perg in PERGUNTAS.items():
            for p in perg:
                p_copy = p.copy()
                p_copy["categoria_original"] = cat
                todas.append(p_copy)
        
        random.shuffle(todas)
        self.perguntas = todas[:15]
        self.pergunta_index = 0
        self.categoria_atual = self.perguntas[0].get("categoria_original", "Paradoxal") if self.perguntas else "Paradoxal"
        self.mostrar_pergunta()

    def mostrar_escolha_categoria(self):
        self.limpar_conteudo()
        self.atualizar_pontos_header()
        
        card = tk.Frame(self.conteudo, bg="#1a1a2e")
        card.pack(expand=True)
        
        canvas = tk.Canvas(card, width=600, height=500, bg="#1a1a2e", highlightthickness=0)
        canvas.pack()
        
        canvas.create_rectangle(15, 15, 585, 485, outline="#FFD700", width=2, fill="#1e1e3a")
        
        canvas.create_text(300, 40, text="🔍 ESCOLHA UMA CATEGORIA", 
                          font=self.fonte_titulo, fill="white")
        
        if self.modo == "sobrevivencia":
            canvas.create_text(300, 75, text=f"⏰ Tempo: {self.tempo_restante}s", 
                             font=self.fonte_sub, fill="#FF6B35")
        
        # Botões das categorias
        y = 110
        for cat in PERGUNTAS.keys():
            cor = CORES.get(cat, "#888")
            icon = ICONES.get(cat, "📚")
            
            btn = tk.Button(card, text=f"{icon} {cat}", font=self.fonte_btn, bg=cor, fg="white",
                           relief=tk.FLAT, padx=15, pady=8, cursor="hand2",
                           command=lambda c=cat: self.iniciar_categoria(c), bd=0)
            canvas.create_window(300, y, window=btn, width=300)
            y += 45
        
        # Botão voltar
        btn_voltar = tk.Button(card, text="🔙 Voltar", font=self.fonte_btn, bg="#555", fg="white",
                               relief=tk.FLAT, padx=15, pady=6, cursor="hand2",
                               command=self.mostrar_tela_inicial, bd=0)
        canvas.create_window(300, 450, window=btn_voltar)
        
        if self.modo == "sobrevivencia" and self.jogando:
            self.iniciar_timer_sobrevivencia()

    def iniciar_categoria(self, categoria):
        self.categoria_atual = categoria
        if categoria not in self.estatisticas["categorias_jogadas"]:
            self.estatisticas["categorias_jogadas"].append(categoria)
        
        self.perguntas = PERGUNTAS[categoria][:]
        random.shuffle(self.perguntas)
        self.pergunta_index = 0
        self.mostrar_pergunta()

    def iniciar_timer_sobrevivencia(self):
        if self.modo == "sobrevivencia" and self.jogando:
            if self.timer_id:
                self.janela.after_cancel(self.timer_id)
            self.atualizar_timer()

    def atualizar_timer(self):
        if self.modo == "sobrevivencia" and self.jogando:
            self.tempo_restante -= 1
            if self.tempo_restante <= 0:
                self.finalizar_jogo()
                return
            self.status_label.config(text=f"⏰ {self.tempo_restante}s restantes")
            self.play_sound("tick")
            self.timer_id = self.janela.after(1000, self.atualizar_timer)

    def proxima_rodada_classico(self):
        if not self.categorias_restantes:
            self.finalizar_jogo()
            return
        
        self.rodada += 1
        self.categoria_atual = random.choice(self.categorias_restantes)
        self.categorias_restantes.remove(self.categoria_atual)
        self.perguntas = PERGUNTAS[self.categoria_atual][:]
        random.shuffle(self.perguntas)
        self.pergunta_index = 0
        self.mostrar_roleta()

    def mostrar_roleta(self):
        self.limpar_conteudo()
        self.atualizar_pontos_header()
        
        cor = CORES.get(self.categoria_atual, "#FFD700")
        icon = ICONES.get(self.categoria_atual, "⭐")
        
        card = tk.Frame(self.conteudo, bg="#1a1a2e")
        card.pack(expand=True)
        
        canvas = tk.Canvas(card, width=600, height=450, bg="#1a1a2e", highlightthickness=0)
        canvas.pack()
        
        canvas.create_rectangle(15, 15, 585, 435, outline=cor, width=2, fill="#1e1e3a")
        
        canvas.create_text(300, 40, text="🎡 GIRANDO A ROLETA...", 
                          font=self.fonte_titulo, fill=cor)
        
        # Simulação simples da roleta
        canvas.create_oval(220, 120, 380, 280, fill=cor, outline="white", width=3)
        canvas.create_text(300, 200, text="?", font=("Arial", 30, "bold"), fill="white")
        
        canvas.create_text(300, 310, text=f"{icon} {self.categoria_atual}", 
                          font=self.fonte_titulo, fill=cor)
        
        btn = tk.Button(card, text="▶ RESPONDER", font=self.fonte_btn, bg=cor, fg="white",
                        relief=tk.FLAT, padx=15, pady=8, cursor="hand2",
                        command=self.mostrar_pergunta, bd=0)
        canvas.create_window(300, 370, window=btn)

    # ===== TELA DE PERGUNTA =====
    def mostrar_pergunta(self):
        if self.pergunta_index >= len(self.perguntas):
            if self.modo == "classico":
                self.proxima_rodada_classico()
            elif self.modo == "todas":
                self.proxima_categoria_todas()
            else:
                self.finalizar_jogo()
            return
        
        self.limpar_conteudo()
        self.atualizar_pontos_header()
        
        pergunta = self.perguntas[self.pergunta_index]
        self.pergunta_atual = pergunta
        
        cor = CORES.get(self.categoria_atual, "#FFD700")
        icon = ICONES.get(self.categoria_atual, "⭐")
        dificuldade = pergunta.get("dificuldade", "Médio")
        emoji = pergunta.get("emoji", "")
        
        card = tk.Frame(self.conteudo, bg="#1a1a2e")
        card.pack(expand=True, fill=tk.BOTH, padx=15, pady=8)
        
        canvas = tk.Canvas(card, width=800, height=520, bg="#1a1a2e", highlightthickness=0)
        canvas.pack(expand=True)
        
        canvas.create_rectangle(15, 15, 785, 505, outline=cor, width=2, fill="#1e1e3a")
        
        # Cabeçalho da pergunta
        canvas.create_text(400, 35, text=f"{icon} {self.categoria_atual} {emoji}", 
                          font=self.fonte_titulo, fill=cor)
        
        total = len(self.perguntas)
        canvas.create_text(400, 65, text=f"Pergunta {self.pergunta_index + 1}/{total} • {dificuldade}",
                          font=self.fonte_sub, fill="#aaa")
        
        # Barra de progresso
        progresso = (self.pergunta_index + 1) / total
        canvas.create_rectangle(100, 85, 700, 100, fill="#2a2a4a", outline="")
        canvas.create_rectangle(100, 85, 100 + int(600 * progresso), 100, fill=cor, outline="")
        
        # Sequência
        if self.sequencia >= 3:
            canvas.create_text(750, 35, text=f"🔥 x{self.sequencia}", 
                             font=("Arial", 14, "bold"), fill="#FF6B35")
        
        if self.modo == "sobrevivencia":
            canvas.create_text(750, 60, text=f"⏰ {self.tempo_restante}s", 
                             font=("Arial", 14, "bold"), fill="#FF6B35")
        
        # Pergunta
        canvas.create_text(400, 150, text=pergunta["pergunta"], 
                          font=("Helvetica", 15, "bold"), fill="white", width=700)
        
        # Opções
        opcoes = pergunta["opcoes"][:]
        random.shuffle(opcoes)
        
        y = 210
        self.botoes_opcoes = []
        
        for i, opcao in enumerate(opcoes):
            letra = chr(65 + i)
            
            btn = tk.Button(card, text=f"{letra}. {opcao}", font=self.fonte_normal,
                           bg="#2d2d44", fg="white", relief=tk.FLAT,
                           padx=15, pady=8, cursor="hand2",
                           command=lambda opt=opcao: self.verificar_resposta(opt, canvas),
                           activebackground="#3d3d5c", activeforeground="white", bd=0, width=45)
            canvas.create_window(400, y, window=btn)
            self.botoes_opcoes.append(btn)
            y += 50
        
        # Informações
        canvas.create_text(400, 470, 
                          text=f"🏆 {self.pontuacao} pts | 🔥 Sequência: {self.sequencia}",
                          font=self.fonte_sub, fill="#aaa")
        
        if self.modo == "dueto":
            canvas.create_text(400, 490, 
                             text=f"Jogador 1: {self.pontuacao_jogador1} pts | Jogador 2: {self.pontuacao_jogador2} pts",
                             font=self.fonte_pequena, fill="#FFD700")

    def verificar_resposta(self, opcao_escolhida, canvas):
        correta = self.pergunta_atual["resposta"]
        acertou = (opcao_escolhida == correta)
        
        # Desabilitar botões
        for btn in self.botoes_opcoes:
            btn.config(state=tk.DISABLED)
        
        self.estatisticas["total_perguntas"] += 1
        
        if acertou:
            self.estatisticas["acertos"] += 1
            bonus = 5 if self.sequencia >= 3 else 0
            pontos_ganhos = 10 + bonus
            self.pontuacao += pontos_ganhos
            self.sequencia += 1
            
            msg = f"✅ CORRETO! +{pontos_ganhos} pts"
            cor_msg = "#2ECC71"
            self.play_sound("correct")
            
            if self.sequencia >= 5:
                canvas.create_text(400, 340, text="🔥 SEQUÊNCIA DE FOGO! 🔥", 
                                 font=("Arial", 18, "bold"), fill="#FF6B35")
            
            if self.sequencia >= 10:
                canvas.create_text(400, 370, text="⚡ SEQUÊNCIA PERFEITA! ⚡", 
                                 font=("Arial", 18, "bold"), fill="#FFD700")
                self.verificar_conquistas()
        else:
            self.estatisticas["erros"] += 1
            self.sequencia = 0
            
            msg = f"❌ ERRADO! Resposta: {correta}"
            cor_msg = "#E74C3C"
            self.play_sound("wrong")
            
            if self.modo in ("desafio", "sobrevivencia", "expert"):
                self.finalizar_jogo()
                return
        
        self.pergunta_index += 1
        
        # Mostrar resultado
        canvas.create_text(400, 400, text=msg, font=("Arial", 20, "bold"), fill=cor_msg)
        
        # Botão próxima
        btn_prox = tk.Button(canvas, text="▶ PRÓXIMA", font=self.fonte_btn,
                             bg="#3498DB", fg="white", relief=tk.FLAT,
                             padx=20, pady=8, cursor="hand2",
                             command=self.proxima_pergunta, bd=0)
        canvas.create_window(400, 450, window=btn_prox)
        
        self.atualizar_pontos_header()
        
        # Atualizar recordes
        if self.pontuacao > self.estatisticas["recordes"]["pontuacao"]:
            self.estatisticas["recordes"]["pontuacao"] = self.pontuacao
        if self.sequencia > self.estatisticas["recordes"]["sequencia"]:
            self.estatisticas["recordes"]["sequencia"] = self.sequencia
        
        self.salvar_dados()

    def proxima_pergunta(self):
        self.mostrar_pergunta()

    def proxima_categoria_todas(self):
        if not self.categorias_restantes:
            self.finalizar_jogo()
            return
        
        self.categoria_atual = self.categorias_restantes.pop(0)
        self.perguntas = PERGUNTAS[self.categoria_atual][:]
        random.shuffle(self.perguntas)
        self.pergunta_index = 0
        self.mostrar_pergunta()

    def verificar_conquistas(self):
        if self.estatisticas["total_jogos"] >= 1 and not self.conquistas["primeiro_jogo"]["desbloqueado"]:
            self.conquistas["primeiro_jogo"]["desbloqueado"] = True
            self.status_label.config(text="🏅 Conquista: Primeiro Passo!")
        
        if self.sequencia >= 5 and not self.conquistas["perfeito"]["desbloqueado"]:
            self.conquistas["perfeito"]["desbloqueado"] = True
            self.status_label.config(text="🏅 Conquista: Perfeição!")
        
        if self.pontuacao >= 100 and not self.conquistas["genio"]["desbloqueado"]:
            self.conquistas["genio"]["desbloqueado"] = True
            self.status_label.config(text="🏅 Conquista: Gênio!")
        
        if self.sequencia >= 10 and not self.conquistas["x10"]["desbloqueado"]:
            self.conquistas["x10"]["desbloqueado"] = True
            self.status_label.config(text="🏅 Conquista: X10!")
        
        if len(self.estatisticas["categorias_jogadas"]) >= 8 and not self.conquistas["explorador"]["desbloqueado"]:
            self.conquistas["explorador"]["desbloqueado"] = True
            self.status_label.config(text="🏅 Conquista: Explorador!")
        
        self.salvar_dados()

    def mostrar_conquistas(self):
        self.limpar_conteudo()
        
        card = tk.Frame(self.conteudo, bg="#1a1a2e")
        card.pack(expand=True, fill=tk.BOTH, padx=15, pady=15)
        
        canvas = tk.Canvas(card, width=700, height=480, bg="#1a1a2e", highlightthickness=0)
        canvas.pack()
        
        canvas.create_rectangle(15, 15, 685, 465, outline="#FFD700", width=2, fill="#1e1e3a")
        
        canvas.create_text(350, 35, text="🏅 CONQUISTAS", font=self.fonte_titulo, fill="#FFD700")
        
        y = 80
        for chave, conquista in self.conquistas.items():
            status = "✅" if conquista["desbloqueado"] else "🔒"
            cor = "#2ECC71" if conquista["desbloqueado"] else "#666"
            
            canvas.create_text(350, y, text=f"{status} {conquista['nome']} - {conquista['desc']}",
                              font=self.fonte_normal, fill=cor)
            y += 35
        
        btn_voltar = tk.Button(card, text="🔙 Voltar", font=self.fonte_btn, bg="#3498DB", fg="white",
                               relief=tk.FLAT, padx=15, pady=8, cursor="hand2",
                               command=self.mostrar_tela_inicial, bd=0)
        canvas.create_window(350, 430, window=btn_voltar)

    def mostrar_estatisticas(self):
        self.limpar_conteudo()
        
        card = tk.Frame(self.conteudo, bg="#1a1a2e")
        card.pack(expand=True, fill=tk.BOTH, padx=15, pady=15)
        
        canvas = tk.Canvas(card, width=700, height=480, bg="#1a1a2e", highlightthickness=0)
        canvas.pack()
        
        canvas.create_rectangle(15, 15, 685, 465, outline="#3498DB", width=2, fill="#1e1e3a")
        
        canvas.create_text(350, 35, text="📊 ESTATÍSTICAS", font=self.fonte_titulo, fill="#3498DB")
        
        stats = [
            f"🎮 Total de Jogos: {self.estatisticas['total_jogos']}",
            f"📝 Perguntas Respondidas: {self.estatisticas['total_perguntas']}",
            f"✅ Acertos: {self.estatisticas['acertos']}",
            f"❌ Erros: {self.estatisticas['erros']}",
            f"🏆 Melhor Pontuação: {self.estatisticas['recordes']['pontuacao']}",
            f"🔥 Maior Sequência: {self.estatisticas['recordes']['sequencia']}",
            f"📚 Categorias Exploradas: {len(self.estatisticas['categorias_jogadas'])}/8",
        ]
        
        y = 80
        for stat in stats:
            canvas.create_text(350, y, text=stat, font=self.fonte_sub, fill="white")
            y += 35
        
        if self.estatisticas['total_perguntas'] > 0:
            taxa = (self.estatisticas['acertos'] / max(1, self.estatisticas['total_perguntas'])) * 100
            canvas.create_text(350, y + 15, text=f"🎯 Taxa de Acerto: {taxa:.1f}%", 
                             font=self.fonte_sub, fill="#FFD700")
        
        btn_voltar = tk.Button(card, text="🔙 Voltar", font=self.fonte_btn, bg="#3498DB", fg="white",
                               relief=tk.FLAT, padx=15, pady=8, cursor="hand2",
                               command=self.mostrar_tela_inicial, bd=0)
        canvas.create_window(350, 430, window=btn_voltar)

    def sair_jogo(self):
        self.salvar_dados()
        if messagebox.askyesno("Sair", "Deseja realmente sair do jogo?"):
            self.janela.destroy()

    def finalizar_jogo(self):
        self.jogando = False
        self.estatisticas["total_jogos"] += 1
        self.salvar_dados()
        
        if self.timer_id:
            self.janela.after_cancel(self.timer_id)
            self.timer_id = None
        
        self.play_sound("gameover")
        self.limpar_conteudo()
        
        card = tk.Frame(self.conteudo, bg="#1a1a2e")
        card.pack(expand=True)
        
        canvas = tk.Canvas(card, width=700, height=480, bg="#1a1a2e", highlightthickness=0)
        canvas.pack()
        
        canvas.create_rectangle(15, 15, 685, 465, outline="#FFD700", width=2, fill="#1e1e3a")
        
        canvas.create_text(350, 40, text="🏆 FIM DE JOGO!", font=self.fonte_titulo, fill="#FFD700")
        
        if self.modo == "dueto":
            canvas.create_text(350, 90, text=f"Jogador 1: {self.pontuacao_jogador1} pts", 
                             font=self.fonte_sub, fill="white")
            canvas.create_text(350, 115, text=f"Jogador 2: {self.pontuacao_jogador2} pts", 
                             font=self.fonte_sub, fill="white")
            
            if self.pontuacao_jogador1 > self.pontuacao_jogador2:
                vencedor = "🏆 Jogador 1 Venceu! 🏆"
            elif self.pontuacao_jogador2 > self.pontuacao_jogador1:
                vencedor = "🏆 Jogador 2 Venceu! 🏆"
            else:
                vencedor = "🤝 Empate!"
            
            canvas.create_text(350, 150, text=vencedor, font=("Arial", 18, "bold"), fill="#FFD700")
            pontuacao_final = max(self.pontuacao_jogador1, self.pontuacao_jogador2)
        else:
            canvas.create_text(350, 90, text=f"Pontuação final: {self.pontuacao}", 
                             font=("Arial", 24, "bold"), fill="white")
            canvas.create_text(350, 125, text=f"Maior sequência: {self.sequencia}", 
                             font=self.fonte_sub, fill="#aaa")
            canvas.create_text(350, 155, text=f"Recorde: {self.estatisticas['recordes']['pontuacao']} pts", 
                             font=self.fonte_sub, fill="#FFD700")
            pontuacao_final = self.pontuacao
        
        # Avaliação
        if pontuacao_final >= 150:
            avaliacao = "🌟 GÊNIO ABSOLUTO! 🌟"
            cor = "#FFD700"
        elif pontuacao_final >= 100:
            avaliacao = "🧠 EXCELENTE!"
            cor = "#2ECC71"
        elif pontuacao_final >= 60:
            avaliacao = "📚 MUITO BOM!"
            cor = "#3498DB"
        elif pontuacao_final >= 30:
            avaliacao = "💪 BOM! TENTE NOVAMENTE!"
            cor = "#F1C40F"
        else:
            avaliacao = "📖 CONTINUE PRATICANDO!"
            cor = "#E74C3C"
        
        canvas.create_text(350, 200, text=avaliacao, font=("Arial", 18, "bold"), fill=cor)
        
        # Verificar conquistas
        if self.modo == "expert" and self.estatisticas["acertos"] >= 8:
            self.conquistas["expert"]["desbloqueado"] = True
        if self.modo == "todas" and len(self.categorias_restantes) == 0:
            self.conquistas["maratona"]["desbloqueado"] = True
        
        # Botões
        btn_frame = tk.Frame(card, bg="#1a1a2e")
        canvas.create_window(350, 300, window=btn_frame)
        
        for txt, cor_btn, cmd in [("🔄 JOGAR NOVAMENTE", "#2ECC71", self.mostrar_tela_inicial),
                                   ("🔙 MENU", "#3498DB", self.mostrar_tela_inicial),
                                   ("🚪 SAIR", "#E74C3C", self.sair_jogo)]:
            btn = tk.Button(btn_frame, text=txt, font=self.fonte_btn, bg=cor_btn, fg="white",
                           relief=tk.FLAT, padx=12, pady=8, cursor="hand2", command=cmd, bd=0)
            btn.pack(side=tk.LEFT, padx=5)
        
        self.atualizar_pontos_header()
        self.verificar_conquistas()

# Inicialização do jogo
if __name__ == "__main__":
    try:
        print("🌟 Iniciando TRIVIA CRACK PREMIUM PLUS v5.0...")
        print("📚 Carregando banco de perguntas...")
        print("🎮 Preparando interface...")
        print("✅ Pronto para jogar!")
        
        jogo = TriviaCrackPremium()
    except Exception as e:
        print(f"❌ Erro ao iniciar o jogo: {e}")
        print("🔄 Verifique se o Python e Tkinter estão instalados corretamente.")
        input("Pressione Enter para sair...")