SELECT mus."Nome", mus."Duracao_Em_Segundos", artista."Nome"
FROM "Musica" mus
JOIN 
"ArtistaMusica" am
ON
am."MusicaId" = mus."Id"
JOIN 
"Artista" artista
ON
am."ArtistaId" = artista."Id" LIMIT 200

