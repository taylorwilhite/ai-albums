from textgenrnn import textgenrnn

textgen = textgenrnn('./weights/albums.hdf5')

# textgen.train_from_file('albumnames.txt', num_epochs=1)
# textgen.save('./weights/albums.hdf5')
album_names = textgen.generate(n=100, temperature=0.5, return_as_list=True)

with open('generated_albums_05.txt', 'w') as f:
  for name in album_names:
    f.write(f'{name}\n')
  f.close()