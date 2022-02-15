import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

has_dir=True;
current_dir = '/content/drive/MyDrive/Deep/project_2/data/renamepictagyolo'

# Percentage of images to be used for the test set
percentage_test = 5;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

def populate(dirs):
  # Populate train.txt and test.txt
    counter = 1
    index_test = round(100 / percentage_test)
    for pathAndFilename in glob.iglob(os.path.join(dirs, "*.*")):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        if ext != ".txt" :
          if counter == index_test:
              counter = 1
              file_test.write(dirs + "/" + title + ext + "\n")
          else:
              file_train.write(dirs + "/" + title + ext + "\n")
              counter = counter + 1
if has_dir:
  #get dirs
  for nameaa in os.listdir(current_dir):
    next_dir = current_dir + "/" + nameaa
    populate(next_dir)
else:
  populate(current_dir)
