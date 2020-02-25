from textgenrnn import textgenrnn

def genBand():
  textgen = textgenrnn('./weights/pitchfork.hdf5')
  bandnames = textgen.generate(n=1, temperature=0.3, return_as_list=True)
  return bandnames

  # with open('generated_03.txt', 'w') as f:
  #   for name in bandnames:
  #     f.write(f'{name}\n')
  #   f.close()

def genAlbum():
  textgen = textgenrnn('./weights/albums.hdf5')
  album_names = textgen.generate(n=1, temperature=0.3, return_as_list=True)
  return album_names

  # with open('generated_albums_05.txt', 'w') as f:
  #   for name in album_names:
  #     f.write(f'{name}\n')
  #   f.close()