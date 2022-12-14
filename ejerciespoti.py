playlist={}

def ingresa_artista (playlist):

  artista =input ('Ingresa El nombre de la Artista-->')
  playlist.update({artista:{}})
  print(playlist)

  album = input('Ingresa El nombre del Album-->') 
  año = input('Ingresa el año del album-->')
  genero = input('Ingresa el Genero-->')
  duracion = int (input(" ingrese las la duracion-->00:00"))
  playlist.update({artista:{ "album-->":album, "año-->":año, "duracion-->": duracion}})
  
  # return playlist
  
ingresa_artista(playlist)
ingresa_artista(playlist)
print(playlist)

#while true:
print('eliminar artista')
print('ingresar ')
def eliminar_artista (artista):
  for a in playlist.keys():
    if a == artista:
      del playlist[a]
      break
eliminar_artista('a') 
print(playlist)
