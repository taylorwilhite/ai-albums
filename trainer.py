from textgenrnn import textgenrnn

def trainBands():
  textgen = textgenrnn()
  textgen.train_from_file('bandnames.txt', num_epochs=5)
  textgen.save('./weights/pitchfork.hdf5')

def trainAlbums():
  textgen = textgenrnn()
  textgen.train_from_file('albumnames.txt', num_epochs=1)
  textgen.save('./weights/albums.hdf5')